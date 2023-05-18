import os
import sys
import argparse
import gzip
import rdflib
import re
import csv
from doctor.consts import VERSION, REPORT_FORMAT_SHEX, REPORT_FORMAT_MD, REPORT_FORMAT_MARKDOWN, \
                            TARGET_CLASS_ALL, EXTENSION_NT, EXTENSION_TTL, EXTENSION_GZ, CORRECT_PREFIXES_FILE_PATH, \
                            CLASS_ERRATA_FILE_PATH, PREFIX_ERRATA_FILE_PATH, HELP_LINK_URL
from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE, GZ, MIXED_INSTANCES
from unidecode import unidecode
from collections import defaultdict
from pathlib import Path

# Main processing of rdf-doctor
def doctor():
    args = get_command_line_args(sys.argv[1:])

    result, error_msg = validate_command_line_args(args)
    if result == False:
        print(error_msg)
        return

    compression_mode = get_compression_mode(args.input)
    input_format = get_input_format(args.input, compression_mode)

    try:
        # Processing branch by report format
        if args.report == REPORT_FORMAT_SHEX:
            # shex
            generate_report_shex(args, input_format, compression_mode)
        elif args.report == REPORT_FORMAT_MARKDOWN or args.report == REPORT_FORMAT_MD:
            # markdown/md
            generate_report_markdown(args, input_format, compression_mode)
        else:
            # Else case does not occur.
            # Prevented by validate_command_line_args function.
            raise ValueError(args.report + '" is an unsupported report format. "' + REPORT_FORMAT_SHEX + '" and "' + REPORT_FORMAT_MD+ '"(same as "' + REPORT_FORMAT_MARKDOWN + '") are supported.')

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
                        action="version",
                        version="%(prog)s " + VERSION)

    # Input RDF file (-i、--input [RDF-FILE]、required)
    parser.add_argument("-i","--input", type=str,
                        required=True,
                        help="input RDF file(.ttl or .nt or gzipped versions of them)",
                        metavar="RDF-FILE")

    # Report format (-r、--report、default: shex)
    parser.add_argument("-r","--report", type=str,
                        default=REPORT_FORMAT_SHEX,
                        help="set the output format/serializer of report to one of: shex (defalut) or md or markdown(same as md)",
                        metavar="FORMAT")

    # Output report file (-o、--output [FILE]、default: Standard output)
    parser.add_argument("-o","--output", type=str,
                        help="write to file instead of stdout",
                        metavar="FILE")

    # Target class(-c、--classes、default: all、Multiple can be specified.)
    parser.add_argument("-c","--classes", type=str,
                        default=[TARGET_CLASS_ALL],
                        nargs="+",
                        help="set the target classes to be inspected to one of: all (defalut) or URL1, URL2,...",
                        metavar="URL")

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
            raise ValueError(extension + '" is an unsupported extension. ".ttl", ".ttl.gz", ".nt" and ".nt.gz" are supported.')


# Validate args(input, output, report, classes)
def validate_command_line_args(args):
    if args.input is None:
        # This case does not occur because -i / --input is required as an option when parsing command line arguments.
        error_msg = "Input file error: No input file specified. (-i [RDF_FILE], --input [RDF_FILE])"
        return False, error_msg

    if os.path.isfile(args.input) == False:
        error_msg = "Input file error: Input file does not exist."
        return False, error_msg

    if args.output is not None:
        # Existence check of file output destination directory
        if os.path.dirname(args.output):
            if os.path.exists(os.path.dirname(args.output)) == False:
                error_msg = "Output file error: Output directory does not exist."
                return False, error_msg

            # Check if the file output destination has write permission
            if os.access(os.path.dirname(args.output), os.W_OK) == False:
                error_msg = "Output file error: You don't have write permission on the output directory."
                return False, error_msg

    # Report Format only allows "shex" or "md/markdown" or "shex+"
    if args.report != REPORT_FORMAT_SHEX and \
        args.report != REPORT_FORMAT_MARKDOWN and \
        args.report != REPORT_FORMAT_MD:
        error_msg = 'Report format error: "' + args.report + '" is an unsupported report format. "' + REPORT_FORMAT_SHEX + '" and "' + REPORT_FORMAT_MD + '"(same as "' + REPORT_FORMAT_MARKDOWN + '") are supported.'
        return False, error_msg

    # Allow only ".nt" or ".ttl" (and .gz) extensions
    extension = os.path.splitext(args.input)[1]
    if extension == EXTENSION_GZ:
        org_extension = os.path.splitext(os.path.splitext(args.input)[0])[1]
        # gz
        if org_extension != EXTENSION_NT and org_extension != EXTENSION_TTL:
            error_msg = 'Input file error: "' + extension + '" is an unsupported extension. ".ttl", ".ttl.gz", ".nt" and ".nt.gz" are supported.'
            return False, error_msg
    elif extension != EXTENSION_NT and extension != EXTENSION_TTL:
        error_msg = 'Input file error: "' + extension + '" is an unsupported extension. ".ttl", ".ttl.gz", ".nt" and ".nt.gz" are supported.'
        return False, error_msg

    # Make an error if another class name is specified with "all"
    if TARGET_CLASS_ALL in args.classes:
        if len(args.classes) != 1:
            error_msg = 'Target class error: If "all" is specified, other classes cannot be specified.'
            return False, error_msg

    return True, None


# Processing when the report format is "shex"
def generate_report_shex(args, input_format, compression_mode):
    shaper_result = get_shaper_result(args, input_format, compression_mode)

    # Suggest QName based on URI of validation expression output by sheXer and correct-prefixes.tsv
    result_suggested_qname = []
    input_prefixes = get_input_prefixes(args.input, compression_mode)
    correct_prefixes = get_correct_prefixes()
    suggested_qname = get_suggested_qname(shaper_result, input_prefixes, correct_prefixes)
    if len(suggested_qname) != 0:
        result_suggested_qname.append("# There may be a better QName.\n\n")
        result_suggested_qname.append("# Input QName\tSuggested QName\tURI\n")
        result_suggested_qname.extend(["# " + s for s in suggested_qname])
        result_suggested_qname.append("\n")

    # List for storing the final result
    shex_final_result = []
    shex_final_result.extend(shaper_result)
    if len(result_suggested_qname) != 0:
        shex_final_result.extend(result_suggested_qname)

    # Output results to specified destination (standard output or file)
    if args.output is None:
        print("".join(shex_final_result))
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("".join(shex_final_result))


# Processing when the report format is "md/markdown"
def generate_report_markdown(args, input_format, compression_mode):

    # Processing related to prefixes ------------------
    # Get list for result output about prefix reuse rate
    result_prefix_reuse_percentage = []
    input_prefixes = get_input_prefixes(args.input, compression_mode)
    result_prefix_reuse_percentage.append("## Prefix reuse percentage ([?](" + HELP_LINK_URL + "))\n")
    result_prefix_reuse_percentage.append("Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor.\n")
    prefix_reuse_percentage = get_prefix_reuse_percentage(input_prefixes)
    if prefix_reuse_percentage == None:
        result_prefix_reuse_percentage.append("```\n")
        result_prefix_reuse_percentage.append("Not calculated because there is no prefix defined.\n")
        result_prefix_reuse_percentage.append("```\n\n")
    else:
        result_prefix_reuse_percentage.append("```\n")
        result_prefix_reuse_percentage.append(str(prefix_reuse_percentage) + "%\n")
        result_prefix_reuse_percentage.append("```\n\n")

    # Refer to the errata of prefixes and obtain a list for result output that combines incorrect prefixes and correct prefixes
    result_prefix_errata = []
    prefix_comparison_result = get_prefix_comparison_result(input_prefixes)
    # When there is data to output
    if len(prefix_comparison_result) != 0:
        result_prefix_errata.append("Found prefixes that looks incorrect.\n")
        result_prefix_errata.append("```\n")
        result_prefix_errata.append("Prefix\tInput URI\tSuggested URI\n")
        result_prefix_errata.extend(prefix_comparison_result)
        result_prefix_errata.append("```\n\n")
    # -------------------------------------------------

    # Processing related to classes -------------------
    input_classes = get_input_classes(args.input, input_format, compression_mode, args.classes)

    # Refers to the errata list of the class, acquires the list for result output that combines the incorrect class and the correct class,
    # and returns the class corresponding to each key in fingerprint format stored in dictionary format.
    result_class_errata = []
    class_comparison_result, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list))
    # When there is data to output
    if len(class_comparison_result) != 0:
        result_class_errata.append("Found class names that looks incorrect.\n")
        result_class_errata.append("```\n")
        result_class_errata.append("Input class name\tSuggested class name\n")
        result_class_errata.extend(class_comparison_result)
        result_class_errata.append("```\n\n")

    # Get a result output list to notify about different class strings with the same key as a result of fingerprinting
    result_class_fingerprint = []
    fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
    # When there is data to output
    if len(fingerprint_comparison_result) != 0:
        result_class_fingerprint.append("Found multiple strings that appear to represent the same class name.\n")
        result_class_fingerprint.append("```")
        result_class_fingerprint.extend(fingerprint_comparison_result)
        result_class_fingerprint.append("\n```\n\n")
    # -------------------------------------------------

    # List for storing the final result
    md_final_result = []

    md_final_result.append("# Report on " + os.path.basename(args.input) + "\n\n")

    # Merge result
    md_final_result.extend(result_prefix_reuse_percentage)

    prefix_result_exists = len(result_prefix_errata) != 0
    if prefix_result_exists:
        md_final_result.append("## Refine prefixes ([?](" + HELP_LINK_URL + "))\n")
        md_final_result.extend(result_prefix_errata)

    class_result_exists = len(result_class_errata) != 0 or len(result_class_fingerprint) != 0
    if class_result_exists:
        md_final_result.append("## Refine classes ([?](" + HELP_LINK_URL + "))\n")
        md_final_result.extend(result_class_errata)
        md_final_result.extend(result_class_fingerprint)

    # Output results to specified destination (standard output or file)
    if args.output is None:
        print("".join(md_final_result))
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("".join(md_final_result))

# Call the shex_graph method of shexer's shaper class and output the result
def get_shaper_result(args, input_format, compression_mode):
    # Set parameters when calling the shaper class depending on whether the class is specified as an argument
    if TARGET_CLASS_ALL in args.classes:
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
                    instances_report_mode=MIXED_INSTANCES,
                    detect_minimal_iri=True)

    return shaper.shex_graph(string_output=True)


# Calculates the percentage of prefixes in the input file that exist in the prefix list file prepared in advance,
# and returns it after rounding to the second decimal place.
# If the prefix is not detected, do not calculate and return None.
def get_prefix_reuse_percentage(input_prefixes):
    correct_prefixes = get_correct_prefixes()

    input_prefixes_count = len(input_prefixes)
    if input_prefixes_count == 0:
        return None
    else:
        correct_count = 0
        for prefix in input_prefixes:
            for correct_prefix in correct_prefixes:
                if prefix[1] == correct_prefix[1]:
                    correct_count+=1
                    break

        prefix_reuse_percentage = round(correct_count / input_prefixes_count * 100, 2)
        return prefix_reuse_percentage


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
    class_filter = ",".join(target_classes)

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

    input_classes = []
    qres = g.query(query)
    for row in qres:
        input_classes.append(f"{row.class_name}")

    return input_classes


# Return class errata in a two-dimensional array
def get_class_errata():
    with open(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH), mode="r", newline="\n", encoding="utf-8") as f:
        tsv_reader = csv.reader(f, delimiter="\t")
        class_errata = [row for row in tsv_reader]

    return class_errata


# Return prefix errata in a two-dimensional array
def get_prefix_errata():
    with open(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH), mode="r", newline="\n", encoding="utf-8") as f:
        tsv_reader = csv.reader(f, delimiter="\t")
        prefix_errata = [row for row in tsv_reader]

    return prefix_errata


# Refers to the errata list of the class, acquires the list for result output that combines the incorrect class and the correct class,
# and returns the class corresponding to each key in fingerprint format stored in dictionary format.
def get_class_comparison_result(input_classes, fingerprint_class_dict):
    class_errata = get_class_errata()
    class_comparison_result = []

    # Perform clustering by fingerprint for the acquired class name
    for cls in input_classes:
        fingerprint_class_dict[fingerprint(cls)].append(cls)
        for eratta in class_errata:
            if cls == eratta[0]:
                class_comparison_result.append(cls+"\t"+eratta[1]+"\n")
                break

    return class_comparison_result, fingerprint_class_dict


# Refer to the errata of prefixes and obtain a list that combines incorrect prefixes and correct prefixes
def get_prefix_comparison_result(input_prefixes):
    prefix_errata = get_prefix_errata()
    prefix_comparison_result = []

    # Perform clustering by fingerprint for the acquired class name
    for prefix in input_prefixes:
        for eratta in prefix_errata:
            if prefix[1] == eratta[0] and eratta[1] != "":
                prefix_comparison_result.append(str(prefix[0]+"\t"+prefix[1]+"\t"+eratta[1]+"\n"))
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


# Get the output result when there are multiple different strings with the same key for the class, as a commnet
def get_fingerprint_comparison_result_as_comment(fingerprint_class_dict):
    fingerprint_comparison_result = []
    # Extract if there are multiple different strings with the same key
    for value in fingerprint_class_dict.values():
        if len(value) >= 2:
            if len(fingerprint_comparison_result) != 0:
                fingerprint_comparison_result.append("\n")
            for v in value:
                fingerprint_comparison_result.append("\n"+"# "+v)

    return fingerprint_comparison_result


# Get the prefixes contained within the input file
def get_input_prefixes(input_file, compression_mode):
    if compression_mode != None:
        with gzip.open(input_file, mode="rt", encoding="utf-8") as f:
            data = f.read().splitlines()
    else:
        with open(input_file, mode="r", newline="\n", encoding="utf-8") as f:
            data = f.read().splitlines()

    input_prefixes = []
    for line in data:
        if ("@prefix" in line or "@PREFIX" in line):
            line_mod = line.replace("@prefix", "").replace("@PREFIX", "").replace(" ", "").replace("\t","")
            qname = line_mod[:line_mod.find(":")+1]
            uri = line_mod[line_mod.find("<")+1:line_mod.find(">")]
            if [qname, uri] not in input_prefixes:
                input_prefixes.append([qname, uri])

    return input_prefixes


# Get the correct prefix from a prepared prefix list
def get_correct_prefixes():
    with open(Path(__file__).resolve().parent.joinpath(CORRECT_PREFIXES_FILE_PATH), mode="r", newline="\n", encoding="utf-8") as f:
        tsv_reader = csv.reader(f, delimiter="\t")
        correct_prefixes = [row for row in tsv_reader]

    return correct_prefixes


# Compare the URI of the validation expression in the shexer output with the URI of the prepared prefix list
# and get the matching QName from the prefix list
def get_suggested_qname(shaper_result, input_prefixes, correct_prefixes):
    suggest_qname = []
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

            tmp_suggest_qname = []
            is_input_correct_qname = False
            for correct_prefix in correct_prefixes:
                append_str = input_qname + "\t" + correct_prefix[0]+"\t"+shaper_result_uri+"\n"
                if (shaper_result_uri == correct_prefix[1] and append_str not in suggest_qname):
                    if exists_in_input_prefix:
                        # If the prefixes defined in the input file include those with the same URI,
                        # add them to the list only if the QName is different
                        if correct_prefix[0] != input_qname:
                            tmp_suggest_qname.append(append_str)
                        else:
                            # If the QName defined in the input file is also included in the prefix list,
                            # do not suggest another QName with the same URI in the prefix list
                            is_input_correct_qname = True
                            break
                    else:
                        suggest_qname.append(append_str)

            if is_input_correct_qname == False:
                suggest_qname.extend(tmp_suggest_qname)

    return suggest_qname


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
