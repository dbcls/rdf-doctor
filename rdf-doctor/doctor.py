import os
import sys
import argparse
import consts
import gzip
import rdflib
import re
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
# # todo: Include rewriting candidates for prefixes and class names determined by referring to the dictionary in the report
def generate_report_markdown(args, input_format, compression_mode):
    class_list = get_classes_list(args.input, input_format, compression_mode)
    fingerprint_class_dict = defaultdict(list)

    # Perform clustering by fingerprint for the acquired class name
    for cls in class_list:
        fingerprint_class_dict[fingerprint(cls)].append(cls)

    # A list to store the result string
    result_list = []

    # Extract if there are multiple different strings with the same key
    for value in fingerprint_class_dict.values():
        if len(value) >= 2:
            result_list.append("\n")
            for v in value:
                result_list.append(v+"\n")

    # Change the output message depending on whether there are multiple different strings with the same key
    if len(result_list) != 0:
        # Insert at the beginning
        result_list.insert(0, "[INFO] Multiple strings were found that appear to represent the same class name. They are listed below.\n")
    else:
        result_list.append("[OK] A potentially incorrect class name was not detected.\n")

    prefix_reuse_percentage, error_msg = get_prefix_reuse_percentage(args.input, input_format, compression_mode)

    if error_msg != None:
        # Insert at the beginning
        result_list.insert(0, "Prefix reuse percentage: " + error_msg + "\n\n")
    else:
        # Insert at the beginning
        result_list.insert(0, "Prefix reuse percentage: " + str(prefix_reuse_percentage) + " %\n\n")

    # Output results to specified destination (standard output or file)
    if args.output is None:
        print("".join(result_list))
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("".join(result_list))


# Processing when the report format is "shex+"
# todo: Develop processing for shex+
# todo: Include validating specification
def generate_report_shex_plus(args, input_format, compression_mode):
    call_shexer_shaper(args, input_format, compression_mode)


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
def get_prefix_reuse_percentage(input_file, input_format, compression_mode):
    target_namespaces = get_namespaces_list(input_file, input_format, compression_mode)
    with open(Path(__file__).resolve().parent.joinpath(consts.PREFIX_LIST_FILE_PATH), 'r') as f:
        correct_namespaces_list = f.read().splitlines()

    target_namespace_count = len(target_namespaces)
    if target_namespace_count == 0:
        error_msg = "Not calculated because there is no prefix defined."
        return None, error_msg

    correct_count = 0
    for namespace in target_namespaces:
        if str(namespace[1]) in correct_namespaces_list:
            correct_count+=1

    return round(correct_count / target_namespace_count * 100, 2), None


def get_classes_list(input_file, input_format, compression_mode):
    g = rdflib.Graph()

    if compression_mode != None:
        with gzip.open(input_file, "rb") as f:
            data = f.read()
        g.parse(data=data, format=input_format)
    else:
        g.parse(input_file, format=input_format)

    query = """
        select distinct ?class_name
        where {
            [] a ?class_name .
            filter(! isBlank(?class_name))
        }
    """

    class_list = []
    qres = g.query(query)
    for row in qres:
        class_list.append(f"{row.class_name}")

    return class_list


def get_namespaces_list(input_file, input_format, compression_mode):
    g = rdflib.Graph()
    if compression_mode != None:
        with gzip.open(input_file, "rb") as f:
            data = f.read()
        g.parse(data=data, format=input_format)
    else:
        g.parse(input_file, format=input_format)

    namespace_list = []
    exclude_list = ["owl", "rdf", "rdfs", "xsd", "xml"]
    for namespace in g.namespaces():
        if str(namespace[0]) not in exclude_list:
            namespace_list.append(namespace)

    return namespace_list


def fingerprint(string):
    string = string.lower()
    string = re.sub("[^A-Za-z0-9 ]+", "", string)
    string = unidecode(string)
    words = string.split()
    words = sorted(list(set(words)))
    return " ".join(words)
