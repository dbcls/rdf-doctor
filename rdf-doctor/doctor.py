import os
import sys
import argparse
import consts
import gzip
import rdflib
import re
import csv
from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE, GZ, MIXED_INSTANCES
from unidecode import unidecode
from collections import defaultdict
from pathlib import Path

# Main processing of rdf-doctor
def doctor():
    args = get_command_line_args(sys.argv[1:])

    if args.version:
        print(consts.VERSION)
        return

    result, error_msg = validate_command_line_args(args)
    if result == False:
        print(error_msg)
        return

    compression_mode = get_compression_mode(args.input)
    input_format = get_input_format(args.input, compression_mode)

    try:
        # Processing branch by report format
        if args.report == consts.REPORT_FORMAT_SHEX:
            # shex
            generate_report_shex(args, input_format, compression_mode)
        elif args.report == consts.REPORT_FORMAT_MARKDOWN or args.report == consts.REPORT_FORMAT_MD:
            # markdown/md
            generate_report_markdown(args, input_format, compression_mode)
        elif args.report == consts.REPORT_FORMAT_SHEX_PLUS:
            # shex+
            generate_report_shex_plus(args, input_format, compression_mode)
        else:
            # Else case does not occur.
            # Prevented by validate_command_line_args function.
            raise ValueError(args.report + '" is an unsupported report format. "' + consts.REPORT_FORMAT_SHEX + '", "' + consts.REPORT_FORMAT_MARKDOWN + '", "' + consts.REPORT_FORMAT_MD + '" and "' + consts.REPORT_FORMAT_SHEX_PLUS + '" are supported.')

    except ValueError as e:
        print(e)

    except:
        print("An exception error occurred. Input data format may not be correct. Please review the data.")

    return


# Parse command line arguments and get them as ArgumentParser
def get_command_line_args(args):
    parser = argparse.ArgumentParser(description="Home page: https://github.com/dbcls/rdf-doctor",
                                    usage="rdf-doctor -i RDF-FILE [Options]",
                                    formatter_class=argparse.RawDescriptionHelpFormatter)

    # Version info(-v, --version)
    parser.add_argument("-v","--version",
                        action="store_true",
                        help="Show version number")

    # Input RDF file (-i、--input [RDF-FILE]、required)
    parser.add_argument("-i","--input",
                        type=str,
                        help="Input RDF file",
                        metavar="")

    # Report format (-r、--report、default: shex)
    parser.add_argument("-r","--report", type=str,
                        default=consts.REPORT_FORMAT_SHEX,
                        help="Set the output format/serializer of report to one of: shex (defalut) or shex+ or md|markdown",
                        metavar="")

    # Output report file (-o、--output [FILE]、default: Standard output)
    parser.add_argument("-o","--output", type=str,
                        help="Write to file instead of stdout")

    # Target class(-c、--classes、default: all、Multiple can be specified.)
    parser.add_argument("-c","--classes", type=str,
                        default=[consts.TARGET_CLASS_ALL],
                        nargs='+',
                        help="Set the shexer target_classes to be inspected to one of: all (defalut) or URL1, URL2,...",
                        metavar="")

    return parser.parse_args(args)


# Determine if the input file is compressed and get the compression mode ("gz" or None)
def get_compression_mode(input_file):
    extension = os.path.splitext(input_file)[1]
    if extension == consts.EXTENSION_GZ:
        return GZ
    else:
        return None


# Return input file format ("nt" or "turtle")
def get_input_format(input_file, compression_mode):
    if compression_mode != None:
        org_extension = os.path.splitext(os.path.splitext(input_file)[0])[1]
        if org_extension == consts.EXTENSION_NT:
            # N-Triples
            return NT
        elif org_extension == consts.EXTENSION_TTL:
            # Turtle
            return TURTLE
    else:
        extension = os.path.splitext(input_file)[1]
        if extension == consts.EXTENSION_NT:
            # N-Triples
            return NT
        elif extension == consts.EXTENSION_TTL:
            # Turtle
            return TURTLE
        else:
            # Else case does not occur.
            # Prevented by validate_command_line_args function.
            raise ValueError(extension + '" is an unsupported extension. ".ttl", ".nt" and ".gz" are supported.')


# Validate args(input, output, report, classes)
def validate_command_line_args(args):
    if args.input is None:
        error_msg = 'Input file error: No input file specified. (-i [RDF_FILE], --input [RDF_FILE])'
        return False, error_msg

    if os.path.isfile(args.input) == False:
        error_msg = 'Input file error: Input file does not exist.'
        return False, error_msg

    if args.output is not None:
        # Existence check of file output destination directory
        if os.path.dirname(args.output):
            if os.path.exists(os.path.dirname(args.output)) == False:
                error_msg = 'Output file error: Output directory does not exist.'
                return False, error_msg

            # Check if the file output destination has write permission
            if os.access(os.path.dirname(args.output), os.W_OK) == False:
                error_msg = "Output file error: You don't have write permission on the output directory."
                return False, error_msg

    # Report Format only allows "shex" or "md/markdown" or "shex+"
    if args.report != consts.REPORT_FORMAT_SHEX and \
        args.report != consts.REPORT_FORMAT_MARKDOWN and \
        args.report != consts.REPORT_FORMAT_MD and \
        args.report != consts.REPORT_FORMAT_SHEX_PLUS:
        error_msg = 'Report format error: "' + args.report + '" is an unsupported report format. "' + consts.REPORT_FORMAT_SHEX + '", "' + consts.REPORT_FORMAT_MARKDOWN + '", "' + consts.REPORT_FORMAT_MD + '" and "' + consts.REPORT_FORMAT_SHEX_PLUS + '" are supported.'
        return False, error_msg

    # Allow only ".nt" or ".ttl" (and .gz) extensions
    extension = os.path.splitext(args.input)[1]
    if extension == consts.EXTENSION_GZ:
        org_extension = os.path.splitext(os.path.splitext(args.input)[0])[1]
        # gz
        if org_extension != consts.EXTENSION_NT and org_extension != consts.EXTENSION_TTL:
            error_msg = 'Input file error: "' + extension + '" is an unsupported extension. ".ttl", ".nt" and ".gz" are supported.'
            return False, error_msg
    elif extension != consts.EXTENSION_NT and extension != consts.EXTENSION_TTL:
        error_msg = 'Input file error: "' + extension + '" is an unsupported extension. ".ttl", ".nt" and ".gz" are supported.'
        return False, error_msg

    # Make an error if another class name is specified with "all"
    if consts.TARGET_CLASS_ALL in args.classes:
        if len(args.classes) != 1:
            error_msg = 'Target class error: If "all" is specified, other classes cannot be specified.'
            return False, error_msg

    return True, None


# Processing when the report format is "shex"
def generate_report_shex(args, input_format, compression_mode):
    call_shexer_shaper(args, input_format, compression_mode)


# Processing when the report format is "md/markdown"
def generate_report_markdown(args, input_format, compression_mode):

    # Processing related to prefixes ------------------
    # Get list for result output about prefix reuse rate
    md_result_prefix_reuse_percentage = get_md_result_prefix_reuse_percentage(args.input, input_format, compression_mode)

    input_prefixes = get_input_prefixes(args.input, input_format, compression_mode)
    # Refer to the errata of prefixes and obtain a list for result output that combines incorrect prefixes and correct prefixes
    md_result_prefix_errata = get_md_result_prefix_errata(input_prefixes)
    # -------------------------------------------------

    # Processing related to classes -------------------
    input_classes = get_input_classes(args.input, input_format, compression_mode, args.classes)

    # Refers to the errata list of the class, acquires the list for result output that combines the incorrect class and the correct class,
    # and returns the class corresponding to each key in fingerprint format stored in dictionary format.
    md_result_class_errata, fingerprint_class_dict = get_md_result_class_errata(input_classes, defaultdict(list))

    # Get a result output list to notify about different class strings with the same key as a result of fingerprinting
    md_result_class_fingerprint = get_md_result_class_fingerprint(fingerprint_class_dict)
    # -------------------------------------------------

    # List for storing the final result
    md_final_result = []

    # Merge result
    if len(md_result_prefix_reuse_percentage) != 0 or len(md_result_prefix_errata) != 0  :
        md_final_result.append("# Prefix\n\n")

    md_final_result.extend(md_result_prefix_reuse_percentage)
    md_final_result.extend(md_result_prefix_errata)

    if len(md_result_class_errata) != 0 or len(md_result_class_fingerprint) != 0  :
        md_final_result.append("# Class\n\n")

    md_final_result.extend(md_result_class_errata)
    md_final_result.extend(md_result_class_fingerprint)

    # Output results to specified destination (standard output or file)
    if args.output is None:
        print("".join(md_final_result))
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("".join(md_final_result))


# Processing when the report format is "shex+"
# todo: Develop processing for shex+
# todo: Include validating specification
def generate_report_shex_plus(args, input_format, compression_mode):
    call_shexer_shaper(args, input_format, compression_mode)


# Call the shex_graph method of shexer's shaper class and output the result
def call_shexer_shaper(args, input_format, compression_mode):
    # Set parameters when calling the shaper class depending on whether the class is specified as an argument
    if consts.TARGET_CLASS_ALL in args.classes:
        target_classes = None
        all_classes_mode = True
    else:
        target_classes = args.classes
        all_classes_mode = False

    # Init shexer's shaper class
    shaper = Shaper(graph_file_input=args.input,
                    target_classes=target_classes,
                    all_classes_mode=all_classes_mode,
                    input_format=input_format,
                    compression_mode=compression_mode,
                    instances_report_mode=MIXED_INSTANCES)

    # Output results to specified destination (standard output or file)
    if args.output is None:
        print(shaper.shex_graph(string_output=True))
    else:
        shaper.shex_graph(output_file=args.output)


# Calculates the percentage of prefixes in the input file that exist in the prefix list file prepared in advance,
# and returns it after rounding to the second decimal place.
# If the prefix is not detected, do not calculate and return an error message in the second return value.
def get_md_result_prefix_reuse_percentage(input_file, input_format, compression_mode):
    result_prefix_reuse_percentage = []
    input_prefixes = get_input_prefixes(input_file, input_format, compression_mode)
    correct_prefixes = get_correct_prefixes()

    result_prefix_reuse_percentage.append("## Reuse percentage\n")

    input_prefixes_count = len(input_prefixes)
    if input_prefixes_count == 0:
        result_prefix_reuse_percentage.append("```\n")
        result_prefix_reuse_percentage.append("Not calculated because there is no prefix defined.\n")
        result_prefix_reuse_percentage.append("```\n\n")
    else:
        correct_count = 0
        for prefix in input_prefixes:
            if str(prefix[1]) in correct_prefixes:
                correct_count+=1

        prefix_reuse_percentage = round(correct_count / input_prefixes_count * 100, 2)
        result_prefix_reuse_percentage.append("```\n")
        result_prefix_reuse_percentage.append(str(prefix_reuse_percentage) + "%\n")
        result_prefix_reuse_percentage.append("```\n\n")

    return result_prefix_reuse_percentage


# Get the classes contained within the input file
def get_input_classes(input_file, input_format, compression_mode, target_classes):
    g = rdflib.Graph()

    if compression_mode != None:
        with gzip.open(input_file, "rb") as f:
            data = f.read()
        g.parse(data=data, format=input_format)
    else:
        g.parse(input_file, format=input_format)

    # Filter by classes(command line arguments)
    class_filter = ','.join(target_classes)

    query = """
        SELECT DISTINCT ?class_name
        WHERE {
            [] a ?class_name .
            FILTER(! isBlank(?class_name))
    """
    if consts.TARGET_CLASS_ALL not in target_classes:
        query += " FILTER (?class_name IN (" + class_filter + "))"

    query += """
        }
    """

    input_classes = []
    qres = g.query(query)
    for row in qres:
        input_classes.append(f"{row.class_name}")

    return input_classes


# Return class errata in a two-dimensional array
def get_class_errata():
    with open(Path(__file__).resolve().parent.joinpath(consts.CLASS_ERRATA_FILE_PATH), mode='r', newline='\n', encoding='utf-8') as f:
        tsv_reader = csv.reader(f, delimiter='\t')
        class_errata = [row for row in tsv_reader]

    return class_errata


# Return prefix errata in a two-dimensional array
def get_prefix_errata():
    with open(Path(__file__).resolve().parent.joinpath(consts.PREFIX_ERRATA_FILE_PATH), mode='r', newline='\n', encoding='utf-8') as f:
        tsv_reader = csv.reader(f, delimiter='\t')
        prefix_errata = [row for row in tsv_reader]

    return prefix_errata


# Refers to the errata list of the class, acquires the list for result output that combines the incorrect class and the correct class,
# and returns the class corresponding to each key in fingerprint format stored in dictionary format.
def get_md_result_class_errata(input_classes, fingerprint_class_dict):
    class_errata = get_class_errata()
    result_body = []

    # Perform clustering by fingerprint for the acquired class name
    for cls in input_classes:
        fingerprint_class_dict[fingerprint(cls)].append(cls)
        for eratta in class_errata:
            if cls == eratta[0]:
                result_body.append(cls+"\t"+eratta[1]+"\n")

    md_result_class_errata = []
    # When there is data to output
    if len(result_body) != 0:
        md_result_class_errata.append("## A class name that appears to be incorrect was found.\n")
        md_result_class_errata.append("```\n")
        md_result_class_errata.append("Input\tCorrect\n")
        md_result_class_errata.extend(result_body)
        md_result_class_errata.append("```\n\n")

    return md_result_class_errata, fingerprint_class_dict


# Refer to the errata of prefixes and obtain a list for result output that combines incorrect prefixes and correct prefixes
def get_md_result_prefix_errata(input_prefixes):
    prefix_errata = get_prefix_errata()
    result_body = []

    # Perform clustering by fingerprint for the acquired class name
    for prefix in input_prefixes:
        for eratta in prefix_errata:
            if str(prefix[1]) == eratta[1] and eratta[2] != "":
                result_body.append(prefix[1]+"\t"+eratta[2]+"\n")

    md_result_prefix_errata = []
    # When there is data to output
    if len(result_body) != 0:
        md_result_prefix_errata.append("## A prefix that appears to be incorrect was found.\n")
        md_result_prefix_errata.append("```\n")
        md_result_prefix_errata.append("Input\tCorrect\n")
        md_result_prefix_errata.extend(result_body)
        md_result_prefix_errata.append("```\n\n")

    return md_result_prefix_errata


# Get the output result when there are multiple different strings with the same key for the class
def get_md_result_class_fingerprint(fingerprint_class_dict):
    result_body = []
    # Extract if there are multiple different strings with the same key
    for value in fingerprint_class_dict.values():
        if len(value) >= 2:
            if len(result_body) != 0:
                result_body.append("\n")
            for v in value:
                result_body.append("\n"+v)

    md_result_class_fingerprint = []
    # When there is data to output
    if len(result_body) != 0:
        md_result_class_fingerprint.append("## Multiple strings were found that appear to represent the same class name.\n")
        md_result_class_fingerprint.append("```")
        md_result_class_fingerprint.extend(result_body)
        md_result_class_fingerprint.append("\n```\n\n")

    return md_result_class_fingerprint


# Get the prefixes contained within the input file
def get_input_prefixes(input_file, input_format, compression_mode):
    g = rdflib.Graph()
    if compression_mode != None:
        with gzip.open(input_file, "rb") as f:
            data = f.read()
        g.parse(data=data, format=input_format)
    else:
        g.parse(input_file, format=input_format)

    input_prefixes = []
    exclude_list = ["owl", "rdf", "rdfs", "xsd", "xml"]
    for prefix in g.namespaces():
        if str(prefix[0]) not in exclude_list:
            input_prefixes.append(prefix)

    return input_prefixes


# Get the correct prefix from a prepared prefix list
def get_correct_prefixes():
    with open(Path(__file__).resolve().parent.joinpath(consts.CORRECT_PREFIXES_FILE_PATH), 'r') as f:
        correct_prefixes = f.read().splitlines()

    return correct_prefixes


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
