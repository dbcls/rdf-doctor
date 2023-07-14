import os
import sys
import argparse
import gzip
import rdflib
import re
import csv
import codecs
import time
import datetime
import threading
import queue
from doctor.consts import VERSION_FILE, REPORT_FORMAT_SHEX, REPORT_FORMAT_MD, REPORT_FORMAT_MARKDOWN, \
                            TARGET_CLASS_ALL, EXTENSION_NT, EXTENSION_TTL, EXTENSION_GZ, PREFIXES_FILE_PATH, \
                            REFINE_CLASS_URIS_FILE_PATH, REFINE_PREFIX_URIS_FILE_PATH, HELP_LINK_URL
from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE, GZ, MIXED_INSTANCES
from unidecode import unidecode
from collections import defaultdict
from pathlib import Path


# Main processing of rdf-doctor
def doctor():
    args = get_command_line_args(sys.argv[1:])

    validation_result, error_msg = validate_command_line_args(args)
    if validation_result == False:
        print(error_msg)
        return

    compression_mode = get_compression_mode(args.input[0])
    if args.force_format:
        input_format = args.force_format
    else:
        input_format = get_input_format(args.input[0], compression_mode)

    result_queue = queue.Queue()

    try:
        # Processing branch by report format
        if args.report == REPORT_FORMAT_SHEX:
            # shex
            thread_calc = threading.Thread(target=get_shex_result, args=(args, input_format, compression_mode, result_queue,))

        elif args.report == REPORT_FORMAT_MARKDOWN or args.report == REPORT_FORMAT_MD:
            # markdown/md
            thread_calc = threading.Thread(target=get_markdown_result, args=(args, input_format, compression_mode, result_queue,))

        else:
            # Else case does not occur.
            # Prevented by validate_command_line_args function.
            raise ValueError('"' + args.report + '" is an unsupported report format. "' + REPORT_FORMAT_SHEX + '" and "' + REPORT_FORMAT_MD+ '"(same as "' + REPORT_FORMAT_MARKDOWN + '") are supported.')

        thread_calc.setDaemon(True)
        thread_calc.start()
        if args.verbose:
            # Thread for displaying dots during processing
            thread_monitor = threading.Thread(target=monitor_thread, args=(result_queue,))
            thread_monitor.setDaemon(True)
            thread_monitor.start()

        thread_calc.join()
        if args.verbose:
            thread_monitor.join()

        result_output = result_queue.get()
        if type(result_output) is list:
            # Normal case
            if args.output is None:
                # Standard output
                print_overwrite("".join(result_output))
            else:
                # Output to file
                with open(args.output, "w", encoding="utf-8") as f:
                    f.write("".join(result_output))

            if args.verbose:
                print_overwrite(get_dt_now() + " -- Done!")

        elif type(result_output) is IndexError or type(result_output) is Exception:
            # Error case
            raise result_output

        else:
            # Else case does not occur.
            raise Exception("An exception error has occurred. Not the expected processing result.")

    except ValueError as e:
        print(e)

    except IndexError as e:
        print(e)

    except KeyboardInterrupt:
        print ("Keyboard interrupt occurred.")

    except Exception as e:
        print(e)

    return


# Function for displaying dots during processing
def monitor_thread(result_queue):
    i = 0
    spin_char = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    while result_queue.empty():
        print(spin_char[i], end="\r")
        if i == len(spin_char) - 1:
            i = 0
        else:
            i += 1
        time.sleep(0.2)


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


# Parse command line arguments and get them as ArgumentParser
def get_command_line_args(args):
    parser = argparse.ArgumentParser(description="Home page: https://github.com/dbcls/rdf-doctor",
                                    usage="rdf-doctor -i RDF-FILE [Options]",
                                    formatter_class=argparse.RawDescriptionHelpFormatter)

    # Version info(-v, --version)
    parser.add_argument("-v","--version",
                        action="version",
                        version="%(prog)s " + get_version(VERSION_FILE))

    # show progress while processing (-e、--verbose)
    parser.add_argument("-e","--verbose",
                        action="store_true",
                        help="show progress while processing")

    # Input RDF file (-i、--input [RDF-FILE]、required)
    parser.add_argument("-i","--input", type=str,
                        required=True,
                        nargs="+",
                        help="input RDF file(s)(.ttl or .nt or gzip-compressed versions of them). Use the same extension when specifying multiple.",
                        metavar="RDF-FILE")

    # Report format (-r、--report [FORMAT]、default: shex)
    parser.add_argument("-r","--report", type=str,
                        default=REPORT_FORMAT_SHEX,
                        help="set the output format/serializer of report to one of: shex (defalut) or md or markdown(same as md)",
                        metavar="REPORT-FORMAT")

    # Output report file (-o、--output [FILE]、default: Standard output)
    parser.add_argument("-o","--output", type=str,
                        help="write to file instead of stdout",
                        metavar="FILE")

    # Target class(-c、--classes [URL1, URL2,...]、default: all、Multiple can be specified.)
    parser.add_argument("-c","--classes", type=str,
                        default=[TARGET_CLASS_ALL],
                        nargs="+",
                        help="set the target classes to be inspected to one of: all (defalut) or URL1 URL2...",
                        metavar="URL")

    # Prefix URI dictionary file path(-p, --prefix-uri-dict [FILE]、default: reference/refine-prefix-uris.tsv)
    parser.add_argument("-p","--prefix-uri-dict", type=str,
                        default=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)),
                        help='(only when "-r md"(same as "-r markdown") is specified) path to a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination for the prefix (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/refine-prefix-uris.tsv)',
                        metavar="FILE")

    # Class URI dictionary file path(-l, --class-uri-dict [FILE]、default: reference/refine-class-uris.tsv)
    parser.add_argument("-l","--class-uri-dict", type=str,
                        default=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)),
                        help='(only when "-r md"(same as "-r markdown") is specified) path to a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination for the class (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/refine-class-uris.tsv)',
                        metavar="FILE")

    # Prefix list file path(-x, --prefix-list [FILE]、default: reference/prefixes.tsv)
    parser.add_argument("-x","--prefix-list", type=str,
                        default=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)),
                        help="list of prefixes (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/prefixes.tsv)",
                        metavar="FILE")

    # input format (-f、--format [INPUT_FORMAT]、default: Standard output)
    parser.add_argument("-f","--force-format", type=str,
                        help='This option should not normally be used. Because the input format is automatically determined by the file extension. Use it only when you want to force specification. If used, "turtle" or "nt" can be specified.',
                        metavar="INPUT-FORMAT")

    return parser.parse_args(args)


# Determine if the input file is compressed and get the compression mode ("gz" or None)
def get_compression_mode(input_file):
    extension = os.path.splitext(input_file)[1]
    if extension == EXTENSION_GZ:
        return GZ
    else:
        return None


# Return input file format ("nt" or "turtle")
def get_input_format(input_file, compression_mode):
    if compression_mode != None:
        org_extension = os.path.splitext(os.path.splitext(input_file)[0])[1]
        if org_extension == EXTENSION_NT:
            # N-Triples
            return NT
        elif org_extension == EXTENSION_TTL:
            # Turtle
            return TURTLE
        else:
            # Else case does not occur.
            # Prevented by validate_command_line_args function.
            raise ValueError('"' + org_extension + '.gz" is an unsupported extension. ".ttl", ".ttl.gz", ".nt" and ".nt.gz" are supported.')
    else:
        extension = os.path.splitext(input_file)[1]
        if extension == EXTENSION_NT:
            # N-Triples
            return NT
        elif extension == EXTENSION_TTL:
            # Turtle
            return TURTLE
        else:
            # Else case does not occur.
            # Prevented by validate_command_line_args function.
            raise ValueError('"' + extension + '" is an unsupported extension. ".ttl", ".ttl.gz", ".nt" and ".nt.gz" are supported.')


# Validate args(input, output, report, classes)
def validate_command_line_args(args):
    compression_mode = ""
    input_format = ""
    for input_file in args.input:
        if input_file is None:
            # This case does not occur because -i / --input is required as an option when parsing command line arguments.
            error_msg = "Input file error: No input file specified. (-i [RDF_FILE], --input [RDF_FILE])"
            return False, error_msg

        if os.path.isfile(input_file) == False:
            error_msg = "Input file error: " + input_file + " does not exist."
            return False, error_msg

        # Check if the file has read permission
        if os.access(input_file, os.R_OK) == False:
            error_msg = "Input file error: you don't have permission to read the input file."
            return False, error_msg

        # Allow only ".nt" or ".ttl" (and .gz) extensions
        extension = os.path.splitext(input_file)[1]
        if extension == EXTENSION_GZ:
            org_extension = os.path.splitext(os.path.splitext(input_file)[0])[1]
            # gz
            if org_extension != EXTENSION_NT and org_extension != EXTENSION_TTL:
                error_msg = 'Input file error: "' + extension + '" is an unsupported extension. ".ttl", ".ttl.gz", ".nt" and ".nt.gz" are supported.'
                return False, error_msg
        elif extension != EXTENSION_NT and extension != EXTENSION_TTL:
            error_msg = 'Input file error: "' + extension + '" is an unsupported extension. ".ttl", ".ttl.gz", ".nt" and ".nt.gz" are supported.'
            return False, error_msg

        if compression_mode == "":
            compression_mode = get_compression_mode(input_file)
        else:
            if compression_mode != get_compression_mode(input_file):
                error_msg = "Input file error: If you enter multiple files, please use the same extension."
                return False, error_msg

        if input_format == "":
            input_format = get_input_format(input_file, compression_mode)
        else:
            if input_format != get_input_format(input_file, compression_mode):
                error_msg = "Input file error: If you enter multiple files, please use the same extension."
                return False, error_msg

    if args.output is not None:
        # Existence check of file output destination directory
        output_dir = os.path.dirname(args.output)
        if output_dir:
            if os.path.exists(output_dir) == False:
                error_msg = "Output file error: Output directory does not exist."
                return False, error_msg

            # Check if the file output destination has write permission
            if os.access(output_dir, os.W_OK) == False:
                error_msg = "Output file error: You don't have write permission on the output directory."
                return False, error_msg

    # Report Format only allows "shex" or "md/markdown"
    if args.report != REPORT_FORMAT_SHEX and \
        args.report != REPORT_FORMAT_MARKDOWN and \
        args.report != REPORT_FORMAT_MD:
        error_msg = 'Report format error: "' + args.report + '" is an unsupported report format. "' + REPORT_FORMAT_SHEX + '" and "' + REPORT_FORMAT_MD + '"(same as "' + REPORT_FORMAT_MARKDOWN + '") are supported.'
        return False, error_msg

    # Make an error if another class name is specified with "all"
    if TARGET_CLASS_ALL in args.classes:
        if len(args.classes) != 1:
            error_msg = 'Target class error: If "all" is specified, other classes cannot be specified.'
            return False, error_msg

    # Input Format only allows "turtle" or "nt"
    if args.force_format is not None:
        if args.force_format != TURTLE and \
            args.force_format != NT:
            error_msg = 'Input format error: "' + args.force_format + '" is an unsupported input format. "' + TURTLE + '" and "' + NT + '" are supported.'
            return False, error_msg

    # Prefix URIs dictionary file can be specified only in md/markdown mode
    if args.prefix_uri_dict != str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)) and args.report == REPORT_FORMAT_SHEX:
        error_msg = 'Prefix URIs dictionary file error: Prefix URIs dictionary file can only be specified if "md"(same as "markdown") is specified in the -r, --report option.'
        return False, error_msg

    if os.path.isfile(args.prefix_uri_dict) == False:
        error_msg = "Prefix URIs dictionary file error: Prefix dictionary does not exist or you don't have read permission."
        return False, error_msg

    # Check if the file has read permission
    if os.access(args.prefix_uri_dict, os.R_OK) == False:
        error_msg = "Prefix URIs dictionary file error: you don't have permission to read the input file."
        return False, error_msg

    # Class URIs dictionary file can be specified only in md/markdown mode
    if args.class_uri_dict != str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)) and args.report == REPORT_FORMAT_SHEX:
        error_msg = 'Class URIs dictionary file error: Class URIs dictionary file can only be specified if "md"(same as "markdown") is specified in the -r, --report option.'
        return False, error_msg

    if os.path.isfile(args.class_uri_dict) == False:
        error_msg = "Class URIs dictionary file error: Class dictionary does not exist or you don't have read permission."
        return False, error_msg

    # Check if the file has read permission
    if os.access(args.class_uri_dict, os.R_OK) == False:
        error_msg = "Class URIs dictionary file error: you don't have permission to read the input file."
        return False, error_msg

    if os.path.isfile(args.prefix_list) == False:
        error_msg = "Prefix list file error: Prefix list does not exist or you don't have read permission."
        return False, error_msg

    # Check if the file has read permission
    if os.access(args.prefix_list, os.R_OK) == False:
        error_msg = "Prefix list file error: you don't have permission to read the input file."
        return False, error_msg

    return True, None


# Processing when the report format is "shex"
def get_shex_result(args, input_format, compression_mode, result_queue):

    try:
        # Get Prefix when input file is turtle format
        if input_format == TURTLE:
            if args.verbose:
                print_overwrite(get_dt_now() + " -- Getting prefixes from input file...")

            input_prefixes, duplicated_prefixes = get_input_prefixes(args.input, compression_mode)
        else:
            input_prefixes = []
            duplicated_prefixes = []

        shaper_result = get_shaper_result(args, input_format, compression_mode, input_prefixes)

        # Prefixes with the same QName but different URIs at the same time
        if args.verbose:
            print_overwrite(get_dt_now() + " -- Checking for duplicate prefixes...")

        result_duplicated_prefixes = []
        if len(duplicated_prefixes) != 0:
            result_duplicated_prefixes.append("# Duplicate prefixes found.\n")
            result_duplicated_prefixes.append("\n")
            result_duplicated_prefixes.append("# Input-QName\tInput-prefix-URI\n")
            result_duplicated_prefixes.extend(["# " + s for s in duplicated_prefixes])
            result_duplicated_prefixes.append("\n\n")

        # Suggest QName based on URI of validation expression output by sheXer and prefixes.tsv
        if args.verbose:
            print_overwrite(get_dt_now() + " -- Creating suggestions for QName...")

        result_widely_used_qname = []
        widely_used_prefixes = get_widely_used_prefixes(args.prefix_list)
        widely_used_qname = get_widely_used_qname(shaper_result, input_prefixes, widely_used_prefixes)
        if len(widely_used_qname) != 0:
            result_widely_used_qname.append("# There is a more widely used QName.\n\n")
            result_widely_used_qname.append("# Input-QName\tWidely-used-QName\tURI\n")
            result_widely_used_qname.extend(["# " + s for s in widely_used_qname])
            result_widely_used_qname.append("\n")

        # List for storing the final result
        shex_final_result = []
        shex_final_result.extend(shaper_result)
        if len(result_duplicated_prefixes) != 0:
            shex_final_result.extend(result_duplicated_prefixes)

        if len(result_widely_used_qname) != 0:
            shex_final_result.extend(result_widely_used_qname)

        result_queue.put(shex_final_result)

    except IndexError:
        result_queue.put(IndexError('An index error has occurred. If you are using the "-x", "-p" or "-l" option, there may be a problem with the number of columns in the specified tsv file. 2 columns is normal.'))

    except Exception:
        result_queue.put(Exception('An exception error has occurred. There may be a problem with the input data. Check the contents of the file specified by the "-i" option. If there is no problem with the data and you are using the "-x", "-p", or "-l" options, there may be a problem with the contents of the file specified by these options. Please check.'))


# Processing when the report format is "md/markdown"
def get_markdown_result(args, input_format, compression_mode, result_queue):

    try:
        # Processing related to prefixes ------------------
        # Get Prefix when input file is turtle format
        if input_format == TURTLE:
            if args.verbose:
                print_overwrite(get_dt_now() + " -- Getting prefixes from input file...")

            input_prefixes, duplicated_prefixes = get_input_prefixes(args.input, compression_mode)
        else:
            input_prefixes = []
            duplicated_prefixes = []

        # Get list for result output about prefix reuse percentage
        if args.verbose:
            print_overwrite(get_dt_now() + " -- Calculating prefix reuse percentage...")

        result_prefix_reuse_percentage = []
        result_prefix_reuse_percentage.append("## Prefix reuse percentage ([?](" + HELP_LINK_URL + "))\n")
        result_prefix_reuse_percentage.append("Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor.\n")
        prefix_reuse_percentage = get_prefix_reuse_percentage(input_prefixes, args.prefix_list)
        if prefix_reuse_percentage == None:
            result_prefix_reuse_percentage.append("```\n")
            result_prefix_reuse_percentage.append("Not calculated because there is no prefix defined.\n")
            result_prefix_reuse_percentage.append("```\n\n")
        else:
            result_prefix_reuse_percentage.append("```\n")
            result_prefix_reuse_percentage.append(str(prefix_reuse_percentage) + "%\n")
            result_prefix_reuse_percentage.append("```\n\n")

        # Refer to the dictionary of prefix URIs and obtain a list that combines candidate pairs of URI rewrite source and rewrite destination
        if args.verbose:
            print_overwrite(get_dt_now() + " -- Comparing with prefix URIs dictionary...")

        result_refine_prefix_uris = []
        prefix_comparison_result = get_prefix_comparison_result(input_prefixes, args.prefix_uri_dict)
        # When there is data to output
        if len(prefix_comparison_result) != 0:
            result_refine_prefix_uris.append("Found a more widely used one for the prefix URI inputed.\n")
            result_refine_prefix_uris.append("```\n")
            result_refine_prefix_uris.append("Input-QName\tInput-prefix-URI\tSuggested-prefix-URI\n")
            result_refine_prefix_uris.extend(prefix_comparison_result)
            result_refine_prefix_uris.append("```\n\n")

        result_duplicated_prefixes = []
        if len(duplicated_prefixes) != 0:
            result_duplicated_prefixes.append("Duplicate prefixes found.\n")
            result_duplicated_prefixes.append("```\n")
            result_duplicated_prefixes.append("Input-QName\tInput-prefix-URI\n")
            result_duplicated_prefixes.extend([s for s in duplicated_prefixes])
            result_duplicated_prefixes.append("```\n\n")
        # -------------------------------------------------

        if args.verbose:
            print_overwrite(get_dt_now() + " -- Getting classes from input file...")

        # Processing related to classes -------------------
        input_classes = get_input_classes(args.input, input_format, compression_mode, args.classes)

        # Refers to the class URIs dictionary, acquires the list for result output that candidate pairs of URI rewrite source and rewrite destinations,
        # and generate the class corresponding to each key in fingerprint format stored in dictionary format.
        if args.verbose:
            print_overwrite(get_dt_now() + " -- Comparing with class URIs dictionary...")

        result_refine_class_uris = []
        class_comparison_result, fingerprint_class_dict = get_class_comparison_result(input_classes, args.class_uri_dict)
        # When there is data to output
        if len(class_comparison_result) != 0:
            result_refine_class_uris.append("Found a more widely used one for the class URI inputed.\n")
            result_refine_class_uris.append("```\n")
            result_refine_class_uris.append("Input-class-URI\tSuggested-class-URI\n")
            result_refine_class_uris.extend(class_comparison_result)
            result_refine_class_uris.append("```\n\n")

        # Get a result output list to notify about different class strings with the same key as a result of fingerprinting
        if args.verbose:
            print_overwrite(get_dt_now() + " -- Comparing with fingerprint method results...")

        result_class_fingerprint = []
        fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
        # When there is data to output
        if len(fingerprint_comparison_result) != 0:
            result_class_fingerprint.append("Found multiple strings that appear to represent the same class.\n")
            result_class_fingerprint.append("```")
            result_class_fingerprint.extend(fingerprint_comparison_result)
            result_class_fingerprint.append("\n```\n\n")
        # -------------------------------------------------

        # List for storing the final result
        md_final_result = []

        md_final_result.append("# Report on\n")
        md_final_result.append("```\n")
        for input_file in args.input:
            md_final_result.append(os.path.basename(input_file) + "\n")

        md_final_result.append("```\n\n")

        # Merge result
        md_final_result.extend(result_prefix_reuse_percentage)

        prefix_result_exists = len(result_refine_prefix_uris) != 0
        if prefix_result_exists:
            md_final_result.append("## Refine prefix URIs ([?](" + HELP_LINK_URL + "))\n")
            md_final_result.extend(result_refine_prefix_uris)
            md_final_result.extend(result_duplicated_prefixes)

        class_result_exists = len(result_refine_class_uris) != 0 or len(result_class_fingerprint) != 0
        if class_result_exists:
            md_final_result.append("## Refine class URIs ([?](" + HELP_LINK_URL + "))\n")
            md_final_result.extend(result_refine_class_uris)
            md_final_result.extend(result_class_fingerprint)

        result_queue.put(md_final_result)

    except IndexError:
        result_queue.put(IndexError('An index error has occurred. If you are using the "-x", "-p" or "-l" option, there may be a problem with the number of columns in the specified tsv file. 2 columns is normal.'))

    except Exception:
        result_queue.put(Exception('An exception error has occurred. There may be a problem with the input data. Check the contents of the file specified by the "-i" option. If there is no problem with the data and you are using the "-x", "-p", or "-l" options, there may be a problem with the contents of the file specified by these options. Please check.'))


# Call the shex_graph method of shexer's shaper class and output the result
def get_shaper_result(args, input_format, compression_mode, input_prefixes):
    # Set parameters when calling the shaper class depending on whether the class is specified as an argument
    if TARGET_CLASS_ALL in args.classes:
        target_classes = None
        all_classes_mode = True
    else:
        target_classes = args.classes
        all_classes_mode = False

    if input_format == NT:
        namespaces_dict = default_namespaces()
    else:
        namespaces_dict = {}
        for input_prefix in input_prefixes:
            namespaces_dict[input_prefix[1]] = input_prefix[0].replace(":","")

    # Get instance of shexer's shaper class
    shaper = Shaper(graph_list_of_files_input=args.input,
                    target_classes=target_classes,
                    all_classes_mode=all_classes_mode,
                    input_format=input_format,
                    namespaces_dict=namespaces_dict,
                    compression_mode=compression_mode,
                    instances_report_mode=MIXED_INSTANCES,
                    detect_minimal_iri=True)

    return shaper.shex_graph(string_output=True,
                            verbose=args.verbose,
                            acceptance_threshold=0.05)


# Calculates the percentage of prefixes in the input file that exist in the prefix list file prepared in advance,
# and returns it after rounding to the second decimal place.
# If the prefix is not detected, do not calculate and return None.
def get_prefix_reuse_percentage(input_prefixes, prefix_list_file):
    widely_used_prefixes = get_widely_used_prefixes(prefix_list_file)

    input_prefixes_count = len(input_prefixes)
    if input_prefixes_count == 0:
        return None
    else:
        reuse_count = 0
        for prefix in input_prefixes:
            for widely_used_prefix in widely_used_prefixes:
                if prefix[1] == widely_used_prefix[1]:
                    reuse_count+=1
                    break

        prefix_reuse_percentage = round(reuse_count / input_prefixes_count * 100, 2)
        return prefix_reuse_percentage


# Get the classes contained within the input file(s)
def get_input_classes(input_files, input_format, compression_mode, target_classes):

    input_classes = []
    for input_file in input_files:
        g = rdflib.Graph()

        if compression_mode != None:
            with gzip.open(input_file, "rb") as f:
                data = f.read()
            g.parse(data=data, format=input_format)
        else:
            g.parse(input_file, format=input_format)

        # Filter by classes(command line arguments)
        class_filter = "<" + ">, <".join(target_classes) + ">"

        query = """
            SELECT DISTINCT ?class_name
            WHERE {
                [] a ?class_name .
                FILTER(! isBlank(?class_name))
        """
        if TARGET_CLASS_ALL not in target_classes:
            query += " FILTER (?class_name IN (" + class_filter + "))"

        query += """
            }
        """

        qres = g.query(query)
        for row in qres:
            if f"{row.class_name}" not in input_classes:
                input_classes.append(f"{row.class_name}")

    return input_classes


# Return contents of class URIs dictionary in a two-dimensional array
def get_refine_class_uris(refine_class_uris_file):
    with open(refine_class_uris_file, mode="r", newline="\n", encoding="utf-8") as f:
        tsv_reader = csv.reader(f, delimiter="\t")
        refine_class_uris = [row for row in tsv_reader]

    return refine_class_uris


# Return contents of prefix URIs dictionary file in a two-dimensional array
def get_refine_prefix_uris(refine_prefix_uris_file):
    with open(refine_prefix_uris_file, mode="r", newline="\n", encoding="utf-8") as f:
        tsv_reader = csv.reader(f, delimiter="\t")
        refine_prefix_uris = [row for row in tsv_reader]

    return refine_prefix_uris


# Get a list of candidate pairs of URI rewrite source and rewrite destination by referencing the class URLs dictionary.
# Create a dictionary with a class corresponding to each key in the stored fingerprint format.
# Return the two.
def get_class_comparison_result(input_classes, refine_class_uris_file):
    refine_class_uris = get_refine_class_uris(refine_class_uris_file)
    class_comparison_result = []
    fingerprint_class_dict = defaultdict(list)
    # Perform clustering by fingerprint for the acquired class name
    for input_class in input_classes:
        fingerprint_class_dict[fingerprint(input_class)].append(input_class)
        for refine_class_uri in refine_class_uris:
            if input_class == refine_class_uri[0]:
                class_comparison_result.append(input_class+"\t"+refine_class_uri[1]+"\n")
                break

    return class_comparison_result, fingerprint_class_dict


# Refer to the dictionary of prefix URIs and obtain a list that combines candidate pairs of URI rewrite source and rewrite destination
def get_prefix_comparison_result(input_prefixes, refine_prefix_uris_file):
    refine_prefix_uris = get_refine_prefix_uris(refine_prefix_uris_file)
    prefix_comparison_result = []

    # Perform clustering by fingerprint for the acquired class name
    for input_prefix in input_prefixes:
        for refine_prefix_uri in refine_prefix_uris:
            if input_prefix[1] == refine_prefix_uri[0] and refine_prefix_uri[1] != "":
                prefix_comparison_result.append(str(input_prefix[0]+"\t"+input_prefix[1]+"\t"+refine_prefix_uri[1]+"\n"))
                break

    return prefix_comparison_result


# Get the output result when there are multiple different strings with the same key for the class
def get_fingerprint_comparison_result(fingerprint_class_dict):
    fingerprint_comparison_result = []
    # Extract if there are multiple different strings with the same key
    for value in fingerprint_class_dict.values():
        if len(value) >= 2:
            if len(fingerprint_comparison_result) != 0:
                fingerprint_comparison_result.append("\n")
            for v in value:
                fingerprint_comparison_result.append("\n"+v)

    return fingerprint_comparison_result


# Get the prefixes contained within the input file(s)
# And get prefixes with the same QName but different URIs at the same time.
def get_input_prefixes(input_files, compression_mode):
    input_prefixes = []
    duplicated_qnames = []
    duplicated_prefixes_dict = defaultdict(list)
    for input_file in input_files:
        if compression_mode != None:
            with gzip.open(input_file, mode="rt", encoding="utf-8") as f:
                data = f.read().splitlines()
        else:
            with open(input_file, mode="r", newline="\n", encoding="utf-8") as f:
                data = f.read().splitlines()

        for line in data:
            if ("@prefix" in line or "@PREFIX" in line):
                line_mod = line.replace("@prefix", "").replace("@PREFIX", "").replace(" ", "").replace("\t","")
                qname = line_mod[:line_mod.find(":")+1]
                uri = line_mod[line_mod.find("<")+1:line_mod.find(">")]
                if [qname, uri] not in input_prefixes:
                    input_prefixes.append([qname, uri])
                    for input_prefix in input_prefixes:
                        if input_prefix[0] == qname and input_prefix[1] != uri and qname not in duplicated_qnames:
                            duplicated_qnames.append(qname)

    for input_prefix in input_prefixes:
        if input_prefix[0] in duplicated_qnames:
            duplicated_prefixes_dict[fingerprint(input_prefix[0])].append(input_prefix[1])

    duplicated_prefixes_list = []
    for key, values in duplicated_prefixes_dict.items():
        for value in values:
            duplicated_prefixes_list.append(key + ":\t" + value + "\n")

    return input_prefixes, duplicated_prefixes_list


# Get the widely used prefix from a prepared prefix list
def get_widely_used_prefixes(prefix_list_file):
    with open(prefix_list_file, mode="r", newline="\n", encoding="utf-8") as f:
        tsv_reader = csv.reader(f, delimiter="\t")
        widely_used_prefixes = [row for row in tsv_reader]

    return widely_used_prefixes


# Compare the URI of the validation expression in the shexer output with the URI of the prepared prefix list
# and get the matching QName from the prefix list
def get_widely_used_qname(shaper_result, input_prefixes, widely_used_prefixes):
    widely_used_qname = []

    # Comparison of prefix list and minimal URI detected by shaXer
    for line in shaper_result.splitlines():
        if ("[<http" in line and ">~]" in line):
            exists_in_input_prefix = False
            shaper_result_uri = line[line.find("[<http")+2:line.find(">~]")]

            # Determine if the same URI is included in the prefix defined in the input file,
            # and if it is included, get the QName
            input_qname = "Undefined"
            for input_prefix in input_prefixes:
                if shaper_result_uri == input_prefix[1]:
                    exists_in_input_prefix = True
                    input_qname = input_prefix[0]
                    break

            tmp_widely_used_qname = []
            is_included_list = False
            for widely_used_prefix in widely_used_prefixes:
                append_str = input_qname + "\t" + widely_used_prefix[0]+"\t"+shaper_result_uri+"\n"
                if shaper_result_uri == widely_used_prefix[1] and append_str not in widely_used_qname:
                    if exists_in_input_prefix:
                        # If the prefixes defined in the input file include those with the same URI,
                        # add them to the list only if the QName is different
                        if widely_used_prefix[0] != input_qname:
                            tmp_widely_used_qname.append(append_str)
                        else:
                            # If the QName defined in the input file is also included in the prefix list,
                            # do not suggest another QName with the same URI in the prefix list
                            is_included_list = True
                            break
                    else:
                        widely_used_qname.append(append_str)

            if is_included_list == False:
                widely_used_qname.extend(tmp_widely_used_qname)

    # Comparing of prefix list and prefixes in input file
    for input_prefix in input_prefixes:
        tmp_widely_used_qname = []
        is_included_list = False
        for widely_used_prefix in widely_used_prefixes:
            append_str = input_prefix[0] + "\t" + widely_used_prefix[0]+"\t"+input_prefix[1]+"\n"
            if input_prefix[1] == widely_used_prefix[1] and append_str not in widely_used_qname:
                # If the prefixes defined in the input file include those with the same URI,
                # add them to the list only if the QName is different
                if input_prefix[0] != widely_used_prefix[0]:
                    tmp_widely_used_qname.append(append_str)
                else:
                    # If the QName defined in the input file is also included in the prefix list,
                    # do not suggest another QName with the same URI in the prefix list
                    is_included_list = True
                    break

        if is_included_list == False:
            widely_used_qname.extend(tmp_widely_used_qname)

    return widely_used_qname


# Generates a key from the received string, excluding case differences, symbols, control characters, etc.
# Values that contain only the most valuable or meaningful part of the string will have the same key
# returned by this method, useful for clustering.
# Detailed explanation：https://openrefine.org/docs/technical-reference/clustering-in-depth#fingerprint
def fingerprint(string):
    string = string.lower()
    string = re.sub("[^A-Za-z0-9 ]+", "", string)
    string = unidecode(string)
    words = string.split()
    words = sorted(list(set(words)))
    return " ".join(words)

# A dictionary of namespaces to pass to sheXer
# This function is used only when the input file is N-Triples.
def default_namespaces():
    return {
            "http://www.w3.org/2002/07/owl#": "owl",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
            "http://www.w3.org/2000/01/rdf-schema#": "rdfs",
            "http://www.w3.org/2001/XMLSchema#": "xsd",
            "http://www.w3.org/XML/1998/namespace": "xml",
            "http://www.w3.org/2004/02/skos/core#": "skos",
            "http://purl.obolibrary.org/obo/": "obo",
            }

# Get current date and time
# dd/MM/yyyy HH:mm:ss
# This function will only be called if verbose parameter is True.
def get_dt_now():
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# Overwrites the current line of the console with the string passed as argument
def print_overwrite(string):
    print("\r" + string)
