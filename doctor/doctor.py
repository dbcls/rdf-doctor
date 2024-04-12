import os
import sys
import argparse
import gzip
from zipfile import ZipFile
import tarfile
import rdflib
import re
import csv
import codecs
import time
import datetime
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import queue
import shutil
from unidecode import unidecode
from collections import defaultdict
from pathlib import Path
import tempfile
import uuid
from doctor.consts import VERSION_FILE, TARGET_CLASS_ALL, EXTENSION_NT, EXTENSION_TTL, \
                            EXTENSION_RDF, EXTENSION_XML, EXTENSION_OWL, EXTENSION_GZ, EXTENSION_ZIP, EXTENSION_TAR_GZ, \
                            PREFIXES_FILE_PATH, REFINE_CLASS_URIS_FILE_PATH, REFINE_PREFIX_URIS_FILE_PATH, HELP_LINK_URL, \
                            FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, \
                            FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP, FILE_TYPE_ALL, FILE_TYPE_DICT, TMP_DISK_USAGE_LIMIT_DEFAULT

from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE, RDF_XML, GZ, ZIP, MIXED_INSTANCES

is_displaying_spinner = False
in_progress_rdflib_query = False

# Main processing of rdf-doctor
def doctor():
    args = get_command_line_args(sys.argv[1:])

    error_msg = validate_command_line_args_other(args)
    if error_msg is not None:
        print(error_msg)
        return

    # Generate temporary directory for compressed file decompression
    with tempfile.TemporaryDirectory(dir=args.tmp_dir) as temp_dir:

        input_file_2d_list = []
        # If the option is specified to separate results for each input file
        if args.each:
            if args.output is None:
                print("The --each option should be used with the --output option.")
                return

            # Get an array containing each file to be processed
            # Acquire as a two-dimensional array for compatibility with subsequent processing
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each(args.input, temp_dir, args.tmp_dir_disk_usage_limit)
            if error_msg is not None:
                print(error_msg)
                return
        else:
            # Retrieve input files in dictionary format by type
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type(args.input, temp_dir, args.tmp_dir_disk_usage_limit)
            if error_msg is not None:
                print(error_msg)
                return

        if args.type:
            if args.type == "all":
                target_file_types = exists_file_types
            else:
                target_file_types = args.type.split(",")
        else:
            target_file_types = get_target_file_types(exists_file_types)

        for input_file_list in input_file_2d_list:
            if is_target_file(input_file_list, target_file_types):
                error_msg = validate_command_line_args_input(args, input_file_list[0])
                if error_msg is not None:
                    print(error_msg)
                    return

        result_queue = queue.Queue()
        executor_calc = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
        executor_spinner = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())

        global is_displaying_spinner
        if args.verbose:
            is_displaying_spinner = True
            executor_spinner.submit(display_spinner)

        try:
            for input_file_list in input_file_2d_list:
                if is_target_file(input_file_list, target_file_types) == False:
                    continue

                compression_mode = input_file_list[1]
                input_format = input_file_list[2]

                executor_calc.submit(get_shex_result, args, input_file_list[0], input_format, compression_mode, result_queue)

            executor_calc.shutdown()
            if args.verbose:
                is_displaying_spinner = False
                executor_spinner.shutdown()

            while not result_queue.empty():
                result_output = result_queue.get()
                if type(result_output) is list:
                    # Normal case
                    if args.output is None:
                        # Standard output
                        print_overwrite("".join(result_output[0]))
                    else:
                        # Output to file
                        if args.each:
                            #with open(args.output + "/" + os.path.basename(input_file_list[0][0]) + ".shex", "w", encoding="utf-8") as f:
                            with open(args.output + "/" + Path(result_output[1][0]).name + ".shex", "w", encoding="utf-8") as f:
                                f.write("".join(result_output[0]))
                        else:
                            # Output one result file for each type of file processed(Turtle, N-triples, and RDF/XML)
                            # turtle.shex, nt.shex, rdf.shex
                            if result_output[2] == TURTLE:
                                output_file_name = TURTLE
                            elif result_output[2] == NT:
                                output_file_name = "n-triples"
                            elif result_output[2] == RDF_XML:
                                output_file_name = "rdf_xml"

                            if result_output[3] is None:
                                compression_exetention = ""
                            else:
                                compression_exetention = "." + result_output[3]

                            with open(args.output + "/" + output_file_name + compression_exetention + ".shex", "w", encoding="utf-8") as f:
                                f.write("".join(result_output[0]))

                    if args.verbose:
                        print_overwrite(get_dt_now() + " -- Done!")

                elif type(result_output) in [ValueError, IndexError, MemoryError, Exception]:
                    # Error case
                    raise result_output

                else:
                    # Else case does not occur.
                    raise Exception("An exception error has occurred. Not the expected processing result.")

        except ValueError as e:
            print(e)

        except IndexError as e:
            print(e)

        except MemoryError as e:
            print(e)

        except KeyboardInterrupt:
            print ("Keyboard interrupt occurred.")

        except Exception as e:
            print(e)

        finally:
            is_displaying_spinner = False
            executor_calc.shutdown()
            executor_spinner.shutdown()

    return


# Function for displaying dots during processing
def display_spinner():
    i = 0
    spin_char = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    #while result_queue.empty():
    global is_displaying_spinner
    while is_displaying_spinner:
        print(spin_char[i], end="\r")
        if i == len(spin_char) - 1:
            i = 0
        else:
            i += 1
        time.sleep(0.2)


def read(rel_path):
    here = Path(Path(__file__).parent).resolve()
    with codecs.open(Path(here) / rel_path, 'r') as fp:
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

    # Version info(-V, --version)
    parser.add_argument("-V","--version",
                        action="version",
                        version="%(prog)s " + get_version(VERSION_FILE))

    # show progress while processing (-v、--verbose)
    parser.add_argument("-v","--verbose",
                        action="store_true",
                        help="show progress while processing")

    # Input RDF file (-i、--input [RDF-FILE]、required)
    parser.add_argument("-i","--input", type=str,
                        required=True,
                        nargs="+",
                        help='input RDF file or directory (Turtle(.ttl), N-Triples(.nt), RDF/XML(.rdf, .xml, .owl) and their compressed versions are supported)',
                        metavar="RDF-FILE or DIRECTORY")

    # Input file type (-t、--type)
    parser.add_argument("-t","--type",
                        help='specifies the type of the input file ("all" or individually from the following Multiple types can be specified by separating them with a comma. ttl, nt, rdf_xml, ttl_gz, nt_gz, rdf_xml_gz, ttl_zip, nt_zip, rdf_xml_zip)')

    # Add report to results (-r、--report)
    parser.add_argument("-r","--report",
                        action="store_true",
                        help="add report to results")

    # Output directory (-o、--output [DIRECTORY]、default: Standard output)
    parser.add_argument("-o","--output", type=str,
                        help="directory to output results (standard output if not specified)",
                        metavar="DIRECTORY")

    # Target class(-c、--classes [URL1, URL2,...]、default: all、Multiple can be specified.)
    parser.add_argument("-c","--classes", type=str,
                        default=[TARGET_CLASS_ALL],
                        nargs="+",
                        help="set the target classes to be inspected to one of: all (defalut) or URL1 URL2...",
                        metavar="URL")

    # Separate results by file when multiple files are specified (-e、--each)
    parser.add_argument("-e","--each",
                        action="store_true",
                        help="separate results by file when multiple files are specified")

    # Temporary directory (--tmp-dir [DIRECTORY]、default: Platform-dependent default temporary directory)
    parser.add_argument("--tmp-dir", type=str,
                        default=None,
                        help='Temporary directory where the unzipped contents are placed when processing tar.gz or zip (default: Platform-dependent default temporary directory)',
                        metavar="DIRECTORY")

    # Temporary directory usage upper limit(--tmp-dir-disk-usage-limit [percentage]、default: 95)
    parser.add_argument("--tmp-dir-disk-usage-limit", type=int,
                        default=TMP_DISK_USAGE_LIMIT_DEFAULT,
                        help='Percentage of disk usage that contains the temporary directory where unzipped contents are placed when processing tar.gz or zip. Interrupt processing when the specified usage percentage is exceeded (1-100 default: 95)',
                        metavar="PERCENTAGE")

    # Prefix URI dictionary file path(--prefix-uri-dict [FILE]、default: reference/refine-prefix-uris.tsv)
    parser.add_argument("--prefix-uri-dict", type=str,
                        default=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)),
                        help='path to a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination for the prefix (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/refine-prefix-uris.tsv)',
                        metavar="FILE")

    # Class URI dictionary file path(--class-uri-dict [FILE]、default: reference/refine-class-uris.tsv)
    parser.add_argument("--class-uri-dict", type=str,
                        default=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)),
                        help='path to a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination for the class (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/refine-class-uris.tsv)',
                        metavar="FILE")

    # Prefix list file path(--prefix-list [FILE]、default: reference/prefixes.tsv)
    parser.add_argument("--prefix-list", type=str,
                        default=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)),
                        help="list of prefixes (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/prefixes.tsv)",
                        metavar="FILE")

    # input format (--force-format [INPUT_FORMAT]、default: Standard output)
    parser.add_argument("--force-format", type=str,
                        help='This option should not normally be used. Because the input format is automatically determined by the file extension. Use it only when you want to force specification. If used, "turtle", "nt" and "xml"(=RDF/XML) can be specified.',
                        metavar="INPUT-FORMAT")

    return parser.parse_args(args)


# Returns a two-dimensional array of input file array, compression mode, and input format
# One element of the two-dimensional array is configured for each compression mode and input format.
# example
# {
#     ttl: [["test1.ttl", "test2.ttl", "test3.ttl"], None, "turtle"]
#     nt: [["test4.nt", "test5.nt", "test6.nt"], None, "nt"],
#     rdf_xml: [["test7.rdf", "test8.xml", "test9.owl"], None, "xml"],
#     ttl_gz: [["test10.ttl.gz", "test11.ttl.gz", "test12.ttl.gz"], "gz", "turtle"]
#     nt_gz: [["test13.nt.gz", "test14.nt.gz", "test15.nt.gz"], gz, "nt"],
#     rdf_xml_gz: [["test16.rdf.gz", "test17.xml.gz", "test18.owl.gz"], gz, "xml"],
#     ttl_zip: [["test19.ttl.zip", "test20.ttl.zip", "test21.ttl.zip"], zip, "turtle"]
#     nt_zip: [["test22.nt.zip", "test23.nt.zip", "test24.nt.zip"], zip, "nt"],
#     rdf_xml_zip: [["test25.rdf.zip", "test26.xml.zip", "test27.owl.zip"], zip, "xml"]
# }
def get_input_files_by_type(input_files, temp_dir, tmp_dir_disk_usage_limit):

    input_file_list_ttl = []            # Turtle(.ttl)
    input_file_list_nt = []             # N-Triples(.nt)
    input_file_list_rdf_xml = []        # RDF/XML(.rdf, .xml, .owl)
    input_file_list_ttl_gz = []         # GZ compressed Turtle(.ttl.gz)
    input_file_list_nt_gz = []          # GZ compressed N-Triples(.nt.gz)
    input_file_list_rdf_xml_gz = []     # GZ compressed RDF/XML(.rdf.gz, .xml.gz, .owl.gz)
    input_file_list_ttl_zip = []        # ZIP compressed Turtle(.ttl.zip)
    input_file_list_nt_zip = []         # ZIP compressed N-Triples(.nt.zip)
    input_file_list_rdf_xml_zip = []    # ZIP compressed RDF/XML(.rdf.zip, .xml.zip, .owl.zip)
    input_file_2d_list = []             # For storing final results
    exists_file_types = []

    # input_file_list_other = []        # Other than those above
    for input_file in input_files:
        if Path(input_file).exists() == False:
            error_msg = '"' + input_file + '" does not exist.'
            return None, None, error_msg

        # When input_file is a directory
        if Path(input_file).is_dir():
            # Loop by recursively retrieving files in a directory
            for root, _, files in os.walk(top=input_file):
                for file in files:
                    file_path = Path(root) / file
                    compression_mode = get_compression_mode(file_path)
                    input_format = get_input_format(file_path, compression_mode)

                    # Determine file type and add to array
                    if compression_mode == GZ:
                        if input_format == TURTLE:
                            input_file_list_ttl_gz.append(file_path)
                        elif input_format == NT:
                            input_file_list_nt_gz.append(file_path)
                        elif input_format == RDF_XML:
                            input_file_list_rdf_xml_gz.append(file_path)
                        else:
                            # No processing except for .ttl, .nt, .rdf, .xml, .owl compressed
                            pass

                    elif compression_mode == ZIP:
                        if input_format == TURTLE:
                            input_file_list_ttl_zip.append(file_path)
                        elif input_format == NT:
                            input_file_list_nt_zip.append(file_path)
                        elif input_format == RDF_XML:
                            input_file_list_rdf_xml_zip.append(file_path)
                        else:
                            # No processing except for .ttl, .nt, .rdf, .xml, .owl compressed
                            pass

                    elif compression_mode is None:
                        if input_format == TURTLE:
                            input_file_list_ttl.append(file_path)
                        elif input_format == NT:
                            input_file_list_nt.append(file_path)
                        elif input_format == RDF_XML:
                            input_file_list_rdf_xml.append(file_path)
                        else:
                            # No processing except for .ttl, .nt, .rdf, .xml, .owl
                            pass

        else:
            compression_mode = get_compression_mode(input_file)
            input_format = get_input_format(input_file, compression_mode)

            if compression_mode == GZ:
                if input_format == TURTLE:
                    input_file_list_ttl_gz.append(input_file)
                elif input_format == NT:
                    input_file_list_nt_gz.append(input_file)
                elif input_format == RDF_XML:
                    input_file_list_rdf_xml_gz.append(input_file)
                else:
                    extension = get_extension_before_compression(input_file) + "." + compression_mode

                    if extension == EXTENSION_TAR_GZ:
                        # Check disk usage percentage
                        if get_disk_usage_percentage(temp_dir) >= tmp_dir_disk_usage_limit:
                            error_msg = 'The process was canceled because the disk usage exceeded ' + str(tmp_dir_disk_usage_limit) + '%.'
                            return None, None, error_msg

                        extract_path = Path(temp_dir) / Path(input_file + "_" + str(uuid.uuid4())).name
                        # For .tar.gz, expand and process the contents
                        with tarfile.open(input_file, 'r:gz') as tar:
                            tar.extractall(extract_path)

                        # Loop by recursively retrieving files in a directory
                        for root, _, files in os.walk(top=extract_path):
                            for file in files:
                                file_path = Path(root) / file

                                compression_mode = get_compression_mode(file_path)
                                input_format = get_input_format(file_path, compression_mode)
                                if compression_mode == GZ:
                                    if input_format == TURTLE:
                                        input_file_list_ttl_gz.append(file_path)
                                    elif input_format == NT:
                                        input_file_list_nt_gz.append(file_path)
                                    elif input_format == RDF_XML:
                                        input_file_list_rdf_xml_gz.append(file_path)
                                    else:
                                        # No processing except for .ttl, .nt, .rdf, .xml, .owl compressed
                                        pass
                                elif compression_mode == ZIP:
                                    if input_format == TURTLE:
                                        input_file_list_ttl_zip.append(file_path)
                                    elif input_format == NT:
                                        input_file_list_nt_zip.append(file_path)
                                    elif input_format == RDF_XML:
                                        input_file_list_rdf_xml_zip.append(file_path)
                                    else:
                                        # No processing except for .ttl, .nt, .rdf, .xml, .owl compressed
                                        pass

                                elif compression_mode is None:
                                    if input_format == TURTLE:
                                        input_file_list_ttl.append(file_path)
                                    elif input_format == NT:
                                        input_file_list_nt.append(file_path)
                                    elif input_format == RDF_XML:
                                        input_file_list_rdf_xml.append(file_path)
                                    else:
                                        # No processing except for .ttl, .nt, .rdf, .xml, .owl
                                        pass
                    else:
                        error_msg = '"' + extension + '" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.'
                        return None, None, error_msg

            elif compression_mode == ZIP:
                if input_format == TURTLE:
                    input_file_list_ttl_zip.append(input_file)
                elif input_format == NT:
                    input_file_list_nt_zip.append(input_file)
                elif input_format == RDF_XML:
                    input_file_list_rdf_xml_zip.append(input_file)
                else:
                    extension = get_extension_before_compression(input_file) + "." + compression_mode
                    if extension == EXTENSION_ZIP:
                        # Check disk usage percentage
                        if get_disk_usage_percentage(temp_dir) >= tmp_dir_disk_usage_limit:
                            error_msg = 'The process was canceled because the disk usage exceeded ' + str(tmp_dir_disk_usage_limit) + '%.'
                            return None, None, error_msg

                        extract_path = Path(temp_dir) / Path(input_file + "_" + str(uuid.uuid4())).name
                        # For .zip, expand and process the contents
                        with ZipFile(input_file,'r') as zip:
                            zip.extractall(extract_path)

                        # Loop by recursively retrieving files in a directory
                        for root, _, files in os.walk(top=extract_path):
                            for file in files:
                                file_path = Path(root) / file

                                compression_mode = get_compression_mode(file_path)
                                input_format = get_input_format(file_path, compression_mode)
                                if compression_mode == GZ:
                                    if input_format == TURTLE:
                                        input_file_list_ttl_gz.append(file_path)
                                    elif input_format == NT:
                                        input_file_list_nt_gz.append(file_path)
                                    elif input_format == RDF_XML:
                                        input_file_list_rdf_xml_gz.append(file_path)
                                    else:
                                        # No processing except for .ttl, .nt, .rdf, .xml, .owl compressed
                                        pass

                                elif compression_mode == ZIP:
                                    if input_format == TURTLE:
                                        input_file_list_ttl_zip.append(file_path)
                                    elif input_format == NT:
                                        input_file_list_nt_zip.append(file_path)
                                    elif input_format == RDF_XML:
                                        input_file_list_rdf_xml_zip.append(file_path)
                                    else:
                                        # No processing except for .ttl, .nt, .rdf, .xml, .owl compressed
                                        pass

                                elif compression_mode is None:
                                    if input_format == TURTLE:
                                        input_file_list_ttl.append(file_path)
                                    elif input_format == NT:
                                        input_file_list_nt.append(file_path)
                                    elif input_format == RDF_XML:
                                        input_file_list_rdf_xml.append(file_path)
                                    else:
                                        # No processing except for .ttl, .nt, .rdf, .xml, .owl
                                        pass
                    else:
                        error_msg = '"' + extension + '" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.'
                        return None, None, error_msg

            elif compression_mode is None:
                if input_format == TURTLE:
                    input_file_list_ttl.append(input_file)
                elif input_format == NT:
                    input_file_list_nt.append(input_file)
                elif input_format == RDF_XML:
                    input_file_list_rdf_xml.append(input_file)
                else:
                    error_msg = '"' + get_extension(input_file) + '" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.'
                    return None, None, error_msg

    if len(input_file_list_ttl) != 0:
        # input_file_dict[FILE_TYPE_TTL] = [input_file_list_ttl, None, TURTLE]
        input_file_2d_list.append([input_file_list_ttl, None, TURTLE])
        exists_file_types.append(FILE_TYPE_TTL)
    if len(input_file_list_nt) != 0:
        # input_file_dict[FILE_TYPE_NT] = [input_file_list_nt, None, NT]
        input_file_2d_list.append([input_file_list_nt, None, NT])
        exists_file_types.append(FILE_TYPE_NT)
    if len(input_file_list_rdf_xml) != 0:
        # input_file_dict[FILE_TYPE_RDF_XML] = [input_file_list_rdf_xml, None, RDF_XML]
        input_file_2d_list.append([input_file_list_rdf_xml, None, RDF_XML])
        exists_file_types.append(FILE_TYPE_RDF_XML)
    if len(input_file_list_ttl_gz) != 0:
        # input_file_dict[FILE_TYPE_TTL_GZ] = [input_file_list_ttl_gz, GZ, TURTLE]
        input_file_2d_list.append([input_file_list_ttl_gz, GZ, TURTLE])
        exists_file_types.append(FILE_TYPE_TTL_GZ)
    if len(input_file_list_nt_gz) != 0:
        # input_file_dict[FILE_TYPE_NT_GZ] = [input_file_list_nt_gz, GZ, NT]
        input_file_2d_list.append([input_file_list_nt_gz, GZ, NT])
        exists_file_types.append(FILE_TYPE_NT_GZ)
    if len(input_file_list_rdf_xml_gz) != 0:
        # input_file_dict[FILE_TYPE_RDF_XML_GZ] = [input_file_list_rdf_xml_gz, GZ, RDF_XML]
        input_file_2d_list.append([input_file_list_rdf_xml_gz, GZ, RDF_XML])
        exists_file_types.append(FILE_TYPE_RDF_XML_GZ)
    if len(input_file_list_ttl_zip) != 0:
        # input_file_dict[FILE_TYPE_TTL_ZIP] = [input_file_list_ttl_zip, ZIP, TURTLE]
        input_file_2d_list.append([input_file_list_ttl_zip, ZIP, TURTLE])
        exists_file_types.append(FILE_TYPE_TTL_ZIP)
    if len(input_file_list_nt_zip) != 0:
        # input_file_dict[FILE_TYPE_NT_ZIP] = [input_file_list_nt_zip, ZIP, NT]
        input_file_2d_list.append([input_file_list_nt_zip, ZIP, NT])
        exists_file_types.append(FILE_TYPE_NT_ZIP)
    if len(input_file_list_rdf_xml_zip) != 0:
        # input_file_dict[FILE_TYPE_RDF_XML_ZIP] = [input_file_list_rdf_xml_zip, ZIP, RDF_XML]
        input_file_2d_list.append([input_file_list_rdf_xml_zip, ZIP, RDF_XML])
        exists_file_types.append(FILE_TYPE_RDF_XML_ZIP)

    return input_file_2d_list, exists_file_types, None


# Get an array containing each file to be processed
# Acquire as a two-dimensional array for compatibility with subsequent processing.
# example
# [
#     ["test1.ttl", None, "turtle"],
#     ["test2.ttl", None, "turtle"],
#     ["test3.ttl", None, "turtle"],
#     ["test4.ttl.gz", "gz", "turtle"],
#     ["test5.nt", None, "nt"],
#     ["test6.nt", None, "nt"],
#     ["test7.nt", None, "nt"],
#     ["test8.nt.gz", "gz", "nt"],
#     ["test9.rdf", None, "xml"],
#     ["test10.xml", None, "xml"],
#     ["test11.owl", None, "xml"],
#     ["test12.rdf.zip", "zip", "xml"]
# ]
def get_input_files_each(input_files, temp_dir, tmp_dir_disk_usage_limit):

    input_file_2d_list = []
    exists_file_types = []

    for input_file in input_files:
        if Path(input_file).exists() == False:
            error_msg = '"' + input_file + '" does not exist.'
            return None, None, error_msg

        # When input_file is a directory
        if Path(input_file).is_dir():
            # Loop by recursively retrieving files in a directory
            for root, _, files in os.walk(top=input_file):
                for file in files:
                    file_path = Path(root) / file
                    compression_mode = get_compression_mode(file_path)
                    input_format = get_input_format(file_path, compression_mode)

                    # Determine file type and add to array
                    if input_format == TURTLE:
                        input_file_2d_list.append([[file_path], compression_mode, TURTLE])
                    elif input_format == NT:
                        input_file_2d_list.append([[file_path], compression_mode, NT])
                    elif input_format == RDF_XML:
                        input_file_2d_list.append([[file_path], compression_mode, RDF_XML])
                    else:
                        # No processing except for .ttl, .nt, .rdf, .xml, .owl compressed
                        pass

        else:
            # Files with the following extensions are supported: .ttl, .nt, .rdf, .xml, and .owl.
            # However, other files are also added to the list for input checking.
            compression_mode = get_compression_mode(input_file)
            input_format = get_input_format(input_file, compression_mode)

            if input_format == TURTLE:
                input_file_2d_list.append([[input_file], compression_mode, TURTLE])
            elif input_format == NT:
                input_file_2d_list.append([[input_file], compression_mode, NT])
            elif input_format == RDF_XML:
                input_file_2d_list.append([[input_file], compression_mode, RDF_XML])
            else:
                # Case None
                if compression_mode is None:
                    extension = get_extension(input_file)
                else:
                    extension = get_extension_before_compression(input_file) + "." + compression_mode

                if extension == EXTENSION_TAR_GZ:
                    # Check disk usage percentage
                    if get_disk_usage_percentage(temp_dir) >= tmp_dir_disk_usage_limit:
                        error_msg = 'The process was canceled because the disk usage exceeded ' + str(tmp_dir_disk_usage_limit) + '%.'
                        return None, None, error_msg

                    extract_path = Path(temp_dir) / Path(input_file + "_" + str(uuid.uuid4())).name
                    # For .tar.gz, expand and process the contents
                    with tarfile.open(input_file, 'r:gz') as tar:
                        tar.extractall(extract_path)

                    # Loop by recursively retrieving files in a directory
                    for root, _, files in os.walk(top=extract_path):
                        for file in files:
                            file_path = Path(root) / file
                            # Determine file type and add to array
                            compression_mode = get_compression_mode(file_path)
                            input_format = get_input_format(file_path, compression_mode)
                            if input_format == TURTLE:
                                input_file_2d_list.append([[file_path], compression_mode, TURTLE])
                            elif input_format == NT:
                                input_file_2d_list.append([[file_path], compression_mode, NT])
                            elif input_format == RDF_XML:
                                input_file_2d_list.append([[file_path], compression_mode, RDF_XML])
                            else:
                                # No processing except for .ttl, .nt, .rdf, .xml, .owl and their compressed
                                pass

                elif extension == EXTENSION_ZIP:
                    # Check disk usage percentage
                    if get_disk_usage_percentage(temp_dir) >= tmp_dir_disk_usage_limit:
                        error_msg = 'The process was canceled because the disk usage exceeded ' + str(tmp_dir_disk_usage_limit) + '%.'
                        return None, None, error_msg

                    extract_path = Path(temp_dir) / Path(input_file + "_" + str(uuid.uuid4())).name
                    # For .zip, expand and process the contents
                    with ZipFile(input_file,'r') as zip:
                        zip.extractall(extract_path)

                    # Loop by recursively retrieving files in a directory
                    for root, _, files in os.walk(top=extract_path):
                        for file in files:
                            file_path = Path(root) / file
                            compression_mode = get_compression_mode(file_path)
                            input_format = get_input_format(file_path, compression_mode)
                            if input_format == TURTLE:
                                input_file_2d_list.append([[file_path], compression_mode, TURTLE])
                            elif input_format == NT:
                                input_file_2d_list.append([[file_path], compression_mode, NT])
                            elif input_format == RDF_XML:
                                input_file_2d_list.append([[file_path], compression_mode, RDF_XML])
                            else:
                                # No processing except for .ttl, .nt, .rdf, .xml, .owl and their compressed
                                pass
                else:
                    error_msg = '"' + extension + '" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.'
                    return None, None, error_msg

    for input_file_list in input_file_2d_list:
        if input_file_list[1] is None:
            if input_file_list[2] == TURTLE and FILE_TYPE_TTL not in exists_file_types:
                exists_file_types.append(FILE_TYPE_TTL)
            elif input_file_list[2] == NT and FILE_TYPE_NT not in exists_file_types:
                exists_file_types.append(FILE_TYPE_NT)
            elif input_file_list[2] == RDF_XML and FILE_TYPE_RDF_XML not in exists_file_types:
                exists_file_types.append(FILE_TYPE_RDF_XML)
        elif input_file_list[1] == GZ:
            if input_file_list[2] == TURTLE and FILE_TYPE_TTL_GZ not in exists_file_types:
                exists_file_types.append(FILE_TYPE_TTL_GZ)
            elif input_file_list[2] == NT and FILE_TYPE_NT_GZ not in exists_file_types:
                exists_file_types.append(FILE_TYPE_NT_GZ)
            elif input_file_list[2] == RDF_XML and FILE_TYPE_RDF_XML_GZ not in exists_file_types:
                exists_file_types.append(FILE_TYPE_RDF_XML_GZ)
        elif input_file_list[1] == ZIP:
            if input_file_list[2] == TURTLE and FILE_TYPE_TTL_ZIP not in exists_file_types:
                exists_file_types.append(FILE_TYPE_TTL_ZIP)
            elif input_file_list[2] == NT and FILE_TYPE_NT_ZIP not in exists_file_types:
                exists_file_types.append(FILE_TYPE_NT_ZIP)
            elif input_file_list[2] == RDF_XML and FILE_TYPE_RDF_XML_ZIP not in exists_file_types:
                exists_file_types.append(FILE_TYPE_RDF_XML_ZIP)

    return input_file_2d_list, exists_file_types, None

# Determine if the input file is compressed and get the compression mode ("gz" or None)
def get_compression_mode(input_file):
    extension = get_extension(input_file)
    if extension == EXTENSION_GZ:
        return GZ
    elif extension == EXTENSION_ZIP:
        return ZIP
    else:
        return None


# Return input file format ("nt" or "turtle" or "xml")
def get_input_format(input_file, compression_mode):
    if compression_mode is not None:
        extension = get_extension_before_compression(input_file)
    else:
        extension = get_extension(input_file)

    if extension == EXTENSION_NT:
        # N-Triples
        return NT
    elif extension == EXTENSION_TTL:
        # Turtle
        return TURTLE
    elif extension in [EXTENSION_RDF, EXTENSION_XML, EXTENSION_OWL]:
        # RDF/XML(.owl、.rdf、.xml)
        return RDF_XML
    else:
        return None


# Validate args(input)
def validate_command_line_args_input(args, input_file_list):
    compression_mode = ""
    input_format = ""
    for input_file in input_file_list:
        if input_file is None:
            # This case does not occur because -i / --input is required as an option when parsing command line arguments.
            error_msg = "Input file error: No input file specified. (-i [RDF_FILE], --input [RDF_FILE])"
            return error_msg

        if Path(input_file).is_file() == False:
            error_msg = "Input file error: " + input_file + " does not exist."
            return error_msg

        # Check if the file has read permission
        if os.access(input_file, os.R_OK) == False:
            error_msg = "Input file error: you don't have permission to read the input file."
            return error_msg

        # Allow only ".nt", ".ttl", ".rdf", ".xml", ".owl" (and their compressed versions) extensions
        extension = get_extension(input_file)
        if extension in [EXTENSION_GZ, EXTENSION_ZIP]:
            org_extension = get_extension_before_compression(input_file)
            # gz
            # if org_extension != EXTENSION_NT and org_extension != EXTENSION_TTL and org_extension != EXTENSION_RDF and org_extension != EXTENSION_XML and org_extension != EXTENSION_OWL:
            if org_extension not in [EXTENSION_NT, EXTENSION_TTL, EXTENSION_RDF, EXTENSION_XML, EXTENSION_OWL]:
                error_msg = 'Input file error: "' + extension + '" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.'
                return error_msg
        #elif extension != EXTENSION_NT and extension != EXTENSION_TTL and extension != EXTENSION_RDF and extension != EXTENSION_XML and extension != EXTENSION_OWL:
        elif extension not in [EXTENSION_NT, EXTENSION_TTL, EXTENSION_RDF, EXTENSION_XML, EXTENSION_OWL]:
            error_msg = 'Input file error: "' + extension + '" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.'
            return error_msg

        if compression_mode == "":
            compression_mode = get_compression_mode(input_file)
        else:
            # This case usually does not occur because input files are classified by compression mode and input format at the start of processing.
            if compression_mode != get_compression_mode(input_file):
                error_msg = "Input file error: Input file extension could not be processed properly."
                return error_msg

        if input_format == "":
            input_format = get_input_format(input_file, compression_mode)
        else:
            # This case usually does not occur because input files are classified by compression mode and input format at the start of processing.
            if input_format != get_input_format(input_file, compression_mode):
                error_msg = "Input file error: Input file extension could not be processed properly."
                return error_msg

    return None


# Validate args(Excluding input)
def validate_command_line_args_other(args):
    if args.output is not None:
        # Existence check of file output destination directory
        if Path(args.output).is_file():
            error_msg = "Output directory error: A directory must be specified as the output destination. Files cannot be specified."
            return error_msg

        output_dir = Path(args.output)
        if output_dir:
            if Path(output_dir).exists() == False:
                error_msg = "Output directory error: Output directory does not exist."
                return error_msg

            # Check if the file output destination has write permission
            if os.access(output_dir, os.W_OK) == False:
                error_msg = "Output directory error: You don't have write permission on the output directory."
                return error_msg

    # Make an error if another class name is specified with "all"
    if TARGET_CLASS_ALL in args.classes:
        if len(args.classes) != 1:
            error_msg = 'Target class error: If "all" is specified, other classes cannot be specified.'
            return error_msg

    # Input Format only allows "turtle" or "nt" or "xml"
    if args.force_format is not None:
        if args.force_format not in [TURTLE, NT, RDF_XML]:
            error_msg = 'Input format error: "' + args.force_format + '" is an unsupported input format. "' + TURTLE + '", "' + NT + '" and "' + RDF_XML + '"(=RDF/XML) are supported.'
            return error_msg

    if Path(args.prefix_uri_dict).is_file() == False:
        error_msg = "Prefix URIs dictionary file error: Prefix dictionary does not exist or you don't have read permission."
        return error_msg

    # Check if the file has read permission
    if os.access(args.prefix_uri_dict, os.R_OK) == False:
        error_msg = "Prefix URIs dictionary file error: you don't have permission to read the input file."
        return error_msg

    if Path(args.class_uri_dict).is_file() == False:
        error_msg = "Class URIs dictionary file error: Class dictionary does not exist or you don't have read permission."
        return error_msg

    # Check if the file has read permission
    if os.access(args.class_uri_dict, os.R_OK) == False:
        error_msg = "Class URIs dictionary file error: you don't have permission to read the input file."
        return error_msg

    if Path(args.prefix_list).is_file() == False:
        error_msg = "Prefix list file error: Prefix list does not exist or you don't have read permission."
        return error_msg

    # Check if the file has read permission
    if os.access(args.prefix_list, os.R_OK) == False:
        error_msg = "Prefix list file error: you don't have permission to read the input file."
        return error_msg

    # Check input file types
    if args.type is not None:
        types = args.type.split(",")
        if FILE_TYPE_ALL in types:
            if len(types) != 1:
                error_msg = 'Type error: If "all" is specified, other types cannot be specified.'
                return error_msg
        else:
            for type in types:
                if type not in FILE_TYPE_DICT:
                    error_msg = 'Type error: "' + type + '" is an unsupported input file format. "' + FILE_TYPE_TTL + '", "' + FILE_TYPE_NT + '", "' + FILE_TYPE_RDF_XML + '", "' + FILE_TYPE_TTL_GZ + '", "' + FILE_TYPE_NT_GZ + '", "' + FILE_TYPE_RDF_XML_GZ + '", "' + FILE_TYPE_TTL_ZIP + '", "' + FILE_TYPE_NT_ZIP + '" and "' + FILE_TYPE_RDF_XML_ZIP + '" are supported.'
                    return error_msg

    # Check temporary directory
    if args.tmp_dir is not None:
        # Existence check of file temporary directory destination directory
        if Path(args.tmp_dir).is_file():
            error_msg = "Temporary directory error: A directory must be specified as the temporary directory destination. Files cannot be specified."
            return error_msg

        tmp_dir = Path(args.tmp_dir)
        if tmp_dir:
            if Path(tmp_dir).exists() == False:
                error_msg = "Temporary directory error: Temporary directory does not exist."
                return error_msg

            # Check if the file temporary directory destination has write permission
            if os.access(tmp_dir, os.W_OK) == False:
                error_msg = "Temporary directory error: You don't have write permission on the temporary directory."
                return error_msg

    # Check temporary directory usage limit
    if args.tmp_dir_disk_usage_limit < 1 or args.tmp_dir_disk_usage_limit > 100:
        error_msg = "Temporary directory disk usage limit error: Please specify the upper limit of Disk containing temporary directory usage percentage as a number between 1 and 100."
        return error_msg

    return None


# Processing when the report format is "shex"
def get_shex_result(args, input_file_list, input_format, compression_mode, result_queue):

    try:
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(args.prefix_list)

        # Get Prefix when input file is turtle format
        if input_format == NT:
            input_prefixes = []
            duplicated_prefixes = []
            namespaces_dict = get_default_namespaces_dict()
        else:
            if args.verbose:
                print_overwrite(get_dt_now() + " -- Getting prefixes from input file...")

            if input_format == TURTLE:
                input_prefixes, duplicated_prefixes, duplicated_prefixes_dict = get_input_prefixes_turtle(input_file_list, compression_mode)
            elif input_format == RDF_XML:
                input_prefixes, duplicated_prefixes, duplicated_prefixes_dict = get_input_prefixes_rdf_xml(input_file_list, compression_mode)
            else:
                raise ValueError('Invalid input format: ' + str(input_format))

            namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)

        shaper_result = get_shaper_result(args, input_file_list, input_format, compression_mode, namespaces_dict)

        report_result = []
        # Output only if report output option is specified
        if args.report:
            # Prefixes with the same Namespace but different URIs at the same time
            if args.verbose:
                print_overwrite(get_dt_now() + " -- Checking for duplicate prefixes...")

            result_duplicated_prefixes = []
            if len(duplicated_prefixes) != 0:
                result_duplicated_prefixes.append("# Duplicate prefixes found.\n")
                result_duplicated_prefixes.append("# ```\n")
                result_duplicated_prefixes.append("# Input-Namespace\tInput-prefix-URI\n")
                result_duplicated_prefixes.extend(["# " + s for s in duplicated_prefixes])
                result_duplicated_prefixes.append("# ```\n")
                result_duplicated_prefixes.append("# \n# \n")

            # Suggest Namespace based on URI of validation expression output by sheXer and prefixes.tsv
            if args.verbose:
                print_overwrite(get_dt_now() + " -- Creating suggestions for Namespace...")

            result_widely_used_namespace_and_uri = []
            widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, args.prefix_uri_dict)
            if len(widely_used_namespace_and_uri) != 0:
                result_widely_used_namespace_and_uri.append("# There is a more widely used Namespace and URI.\n")
                result_widely_used_namespace_and_uri.append("# (For each of Namespace and URI, output only if the input value differs from the widely used value.)\n")
                # When prefix list is explicitly specified
                if args.prefix_list != str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)):
                    result_widely_used_namespace_and_uri.append("# Using a customized prefix list. (" + args.prefix_list + ")\n")
                # When prefix URI dictionary is explicitly specified
                if args.prefix_uri_dict != str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)):
                    result_widely_used_namespace_and_uri.append("# Using a customized prefix URI dictionary. (" + args.prefix_uri_dict + ")\n")

                result_widely_used_namespace_and_uri.append("# ```\n")
                result_widely_used_namespace_and_uri.append("# Input-Namespace\tInput-URI\tWidely-used-Namespace\tWidely-used-URI\n")
                result_widely_used_namespace_and_uri.extend(["# " + s for s in widely_used_namespace_and_uri])
                result_widely_used_namespace_and_uri.append("# ```\n")
                result_widely_used_namespace_and_uri.append("# \n# \n")

            # Output results previously output in markdown mode=========================================
            # Get list for result output about prefix reuse percentage
            if args.verbose:
                print_overwrite(get_dt_now() + " -- Calculating prefix reuse percentage...")

            result_prefix_reuse_percentage = []
            result_prefix_reuse_percentage.append("# ## Prefix reuse percentage ([?](" + HELP_LINK_URL + "))\n# \n")
            result_prefix_reuse_percentage.append("# Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor.\n")
            result_prefix_reuse_percentage.append("# ```\n")
            prefix_reuse_percentage = get_prefix_reuse_percentage(input_prefixes, widely_used_prefixes_dict)
            if prefix_reuse_percentage is None:
                result_prefix_reuse_percentage.append("# Not calculated because there is no prefix defined.\n")
            else:
                result_prefix_reuse_percentage.append("# " + str(prefix_reuse_percentage) + "%\n")
            result_prefix_reuse_percentage.append("# ```\n# \n# \n")

            if args.verbose:
                print_overwrite(get_dt_now() + " -- Getting classes from input file...")

            # Processing related to classes -------------------
            input_classes = get_input_classes(input_file_list, input_format, compression_mode, args.classes)

            # Refers to the class URIs dictionary, acquires the list for result output that candidate pairs of URI rewrite source and rewrite destinations,
            # and generate the class corresponding to each key in fingerprint format stored in dictionary format.
            if args.verbose:
                print_overwrite(get_dt_now() + " -- Comparing with class URIs dictionary...")

            result_refine_class_uris = []
            class_comparison_result, fingerprint_class_dict = get_class_comparison_result(input_classes, args.class_uri_dict)
            # When there is data to output
            if len(class_comparison_result) != 0:
                result_refine_class_uris.append("# Found a more widely used one for the class URI inputed.\n")
                # When class URI dictionary is explicitly specified
                if args.class_uri_dict != str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)):
                    result_refine_class_uris.append("# Using a customized class URI dictionary. (" + args.class_uri_dict + ")\n")

                result_refine_class_uris.append("# ```\n")
                result_refine_class_uris.append("# Input-class-URI\tSuggested-class-URI\n")
                result_refine_class_uris.extend(["# " + s for s in class_comparison_result])
                result_refine_class_uris.append("# ```\n")
                result_refine_class_uris.append("# \n# \n")

            # Get a result output list to notify about different class strings with the same key as a result of fingerprinting
            if args.verbose:
                print_overwrite(get_dt_now() + " -- Comparing with fingerprint method results...")

            result_class_fingerprint = []
            fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
            # When there is data to output
            if len(fingerprint_comparison_result) != 0:
                result_class_fingerprint.append("# Found multiple strings that appear to represent the same class.\n")
                result_class_fingerprint.append("# ```\n# ")
                result_class_fingerprint.extend(fingerprint_comparison_result)
                result_class_fingerprint.append("\n# ```\n")
                result_class_fingerprint.append("# \n# \n")

            # List for storing the final result
            report_result = []

            report_result.append("# # Report on\n")
            report_result.append("# ```\n")
            for input_file in input_file_list:
                report_result.append("# " + Path(input_file).name + "\n")
            report_result.append("# ```\n")
            report_result.append("# \n")

            # Merge result
            report_result.extend(result_prefix_reuse_percentage)

            prefix_result_exists = len(result_duplicated_prefixes) != 0 or len(result_widely_used_namespace_and_uri) != 0
            if prefix_result_exists:
                report_result.append("# ## Refine namespace and URIs ([?](" + HELP_LINK_URL + "))\n# \n")

            if len(result_duplicated_prefixes) != 0:
                report_result.extend(result_duplicated_prefixes)

            if len(result_widely_used_namespace_and_uri) != 0:
                report_result.extend(result_widely_used_namespace_and_uri)

            class_result_exists = len(result_refine_class_uris) != 0 or len(result_class_fingerprint) != 0
            if class_result_exists:
                report_result.append("# ## Refine class URIs ([?](" + HELP_LINK_URL + "))\n# \n")
                report_result.extend(result_refine_class_uris)
                report_result.extend(result_class_fingerprint)

            # Output results previously output in markdown mode =========================================

        # List for storing the final result
        shex_final_result = []
        shex_final_result.extend(shaper_result)

        if len(report_result) != 0:
            shex_final_result.extend(report_result)

        result_queue.put([shex_final_result, input_file_list, input_format, compression_mode])

    except ValueError as e:
        result_queue.put(ValueError('A value error has occurred.\n\nValueError message: ' + str(e)))

    except IndexError as e:
        result_queue.put(IndexError('An index error has occurred.\n\nIndexError message: ' + str(e)))

    except MemoryError as e:
        result_queue.put(MemoryError('A memory error has occurred.\n\nMemoryError message: ' + str(e)))

    except Exception as e:
        result_queue.put(Exception('An exception error has occurred.\n\nException message: ' + str(e)))


# Call the shex_graph method of shexer's shaper class and output the result
def get_shaper_result(args, input_file_list, input_format, compression_mode, namespaces_dict):
    # Set parameters when calling the shaper class depending on whether the class is specified as an argument
    if TARGET_CLASS_ALL in args.classes:
        target_classes = None
        all_classes_mode = True
    else:
        target_classes = args.classes
        all_classes_mode = False

    # Information ========================================================================================
    # In sheXer2.2.2, specifying a zip file with the graph_list_of_files_input parameter causes an error.
    # Waiting for it to be fixed on sheXer side
    # ====================================================================================================
    # Get instance of shexer's shaper class
    #shaper = Shaper(graph_file_input=input_file_list[0],
    shaper = Shaper(graph_list_of_files_input=input_file_list,
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
def get_prefix_reuse_percentage(input_prefixes, widely_used_prefixes_dict):

    input_prefixes_count = len(input_prefixes)
    if input_prefixes_count == 0:
        return None
    else:
        reuse_count = 0
        for prefix in input_prefixes:
            for widely_used_prefix_namespace, widely_used_prefix_uri in widely_used_prefixes_dict.items():
                if prefix[0] == widely_used_prefix_namespace and prefix[1] == widely_used_prefix_uri:
                    reuse_count+=1
                    break

        prefix_reuse_percentage = round(reuse_count / input_prefixes_count * 100, 2)
        return prefix_reuse_percentage


# Get the classes contained within the input file(s)
def get_input_classes(input_files, input_format, compression_mode, target_classes):

    input_classes = []
    for input_file in input_files:
        g = rdflib.Graph()

        if compression_mode == GZ:
            with gzip.open(input_file, "rb") as f:
                data = f.read()
            g.parse(data=data, format=input_format)
        elif compression_mode == ZIP:
            with ZipFile(input_file, "r") as f:
                data = f.read(Path(input_file).name.replace(".zip", "")).decode()
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

        # Correspondence for not executing query methods in parallel, since calling them in parallel will result in an error. -----
        global in_progress_rdflib_query
        while in_progress_rdflib_query == True:
            time.sleep(0.01)
        in_progress_rdflib_query = True
        qres = g.query(query)
        in_progress_rdflib_query = False
        # -------------------------------------------------------------------------------------------------------------------------

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
    refine_prefix_uris = {}
    with open(refine_prefix_uris_file, mode="r", newline="\n", encoding="utf-8") as f:
        tsv_reader = csv.reader(f, delimiter = '\t')
        refine_prefix_uris = {rows[0]: rows[1] for rows in tsv_reader}

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


# Get the output result when there are multiple different strings with the same key for the class
def get_fingerprint_comparison_result(fingerprint_class_dict):
    fingerprint_comparison_result = []
    # Extract if there are multiple different strings with the same key
    for value in fingerprint_class_dict.values():
        if len(value) >= 2:
            if len(fingerprint_comparison_result) != 0:
                fingerprint_comparison_result.append("\n# ")
            for v in value:
                if len(fingerprint_comparison_result) == 0:
                    fingerprint_comparison_result.append(v)
                else:
                    fingerprint_comparison_result.append("\n# "+v)

    return fingerprint_comparison_result


# Get the prefixes contained within the Turtle file(s)
# And get prefixes with the same Namespace but different URIs at the same time.
def get_input_prefixes_turtle(input_files, compression_mode):
    input_prefixes = []
    duplicated_namespaces = []
    duplicated_prefixes_dict = defaultdict(list) # Used for processing Namespace collision prevention when generating namespaces_dict to be passed to sheXer. ex. {'foaf:': ['http://xmlns.com/foaf/0.1/', 'http://xmlns.com/foaf/spec/#']}
    for input_file in input_files:
        if compression_mode == GZ:
            with gzip.open(input_file, mode="rt", encoding="utf-8") as f:
                data = f.read().splitlines()
        elif compression_mode == ZIP:
            with ZipFile(input_file, "r") as f:
                data = f.read(Path(input_file).name.replace(".zip", "")).decode().splitlines()
        else:
            with open(input_file, mode="r", newline="\n", encoding="utf-8") as f:
                data = f.read().splitlines()

        for line in data:
            if ("@prefix" in line or "@PREFIX" in line):
                line_mod = line.replace("@prefix", "").replace("@PREFIX", "").replace(" ", "").replace("\t","")
                namespace = line_mod[:line_mod.find(":")+1]
                uri = line_mod[line_mod.find("<")+1:line_mod.find(">")]
                if [namespace, uri] not in input_prefixes:
                    input_prefixes.append([namespace, uri])
                    for input_prefix in input_prefixes:
                        if input_prefix[0] == namespace and input_prefix[1] != uri and namespace not in duplicated_namespaces:
                            duplicated_namespaces.append(namespace)

    for input_prefix in input_prefixes:
        if input_prefix[0] in duplicated_namespaces:
            duplicated_prefixes_dict[input_prefix[0]].append(input_prefix[1])

    duplicated_prefixes_list = []
    for key, values in duplicated_prefixes_dict.items():
        for value in values:
            duplicated_prefixes_list.append(key + "\t" + value + "\n")

    return input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict


# Get the prefixes contained within the RDF/XML file(s)
# And get prefixes with the same Namespace but different URIs at the same time.
def get_input_prefixes_rdf_xml(input_files, compression_mode):
    input_prefixes = []
    duplicated_namespaces = []
    duplicated_prefixes_dict = defaultdict(list) # Used for processing Namespace collision prevention when generating namespaces_dict to be passed to sheXer. ex. {'foaf:': ['http://xmlns.com/foaf/0.1/', 'http://xmlns.com/foaf/spec/#']}
    entity_namespaces_dict = {}
    for input_file in input_files:
        if compression_mode == GZ:
            with gzip.open(input_file, mode="rt", encoding="utf-8") as f:
                data = f.read().splitlines()
        elif compression_mode == ZIP:
            with ZipFile(input_file, "r") as f:
                data = f.read(Path(input_file).name.replace(".zip", "")).decode().splitlines()
        else:
            with open(input_file, mode="r", newline="\n", encoding="utf-8") as f:
                data = f.read().splitlines()

        for line in data:
            # Get ENTITY declaration if there is one
            if "!ENTITY" in line:
                getting_namespace = False
                getting_uri = False
                line_values = line.split(" ")
                for line_value in line_values:
                    if "!ENTITY" in line_value:
                        getting_namespace = True
                        continue
                    elif getting_namespace:
                        entity_namespace = line_value + ":"
                        getting_namespace = False
                        getting_uri = True
                        continue
                    elif getting_uri:
                        entity_uri = line_value.replace('"', '').replace(">","")
                        break

                entity_namespaces_dict[entity_namespace] = entity_uri

            elif "xmlns:" in line:
                namespaces = line.split("xmlns:")
                for namespace in namespaces:
                    if "=" in namespace:
                        line_mod = namespace.replace('"', '').replace(" ", "").replace("<","").replace(">","")
                        namespace = line_mod[:line_mod.find("=")] + ":"
                        uri = line_mod[line_mod.find("=")+1:]

                        # If the right side of the equal is described as &xsd;, etc., replace it with the content obtained from the ENTITY declaration.
                        if "&" in uri and ";" in uri:
                            if namespace in entity_namespaces_dict:
                                uri = entity_namespaces_dict[namespace]
                            else:
                                # If there is no ENTITY declaration, leave the URI empty
                                # In this case, an exception error will occur on the sheXer side.
                                uri = ""
                        else:
                            uri = line_mod[line_mod.find("=")+1:]

                        if [namespace, uri] not in input_prefixes:
                            input_prefixes.append([namespace, uri])

                        for input_prefix in input_prefixes:
                            if input_prefix[0] == namespace and input_prefix[1] != uri and namespace not in duplicated_namespaces:
                                duplicated_namespaces.append(namespace)

    # Detects Prefixes with duplicate Namespace and stores them in the dictionary
    for input_prefix in input_prefixes:
        if input_prefix[0] in duplicated_namespaces:
            duplicated_prefixes_dict[input_prefix[0]].append(input_prefix[1])

    duplicated_prefixes_list = []
    for key, values in duplicated_prefixes_dict.items():
        for value in values:
            duplicated_prefixes_list.append(key + "\t" + value + "\n")

    return input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict


# Get the widely used prefix from a prepared prefix list
def get_widely_used_prefixes_dict(prefix_list_file):
    widely_used_prefixes_dict = {}
    with open(prefix_list_file, mode="r", newline="\n", encoding="utf-8") as f:
        tsv_reader = csv.reader(f, delimiter = '\t')
        widely_used_prefixes_dict = {rows[0]: rows[1] for rows in tsv_reader}

    return widely_used_prefixes_dict


# Compare the URI of the validation expression in the shexer output with the URI of the prepared prefix list
# and get the matching Namespace from the prefix list
def get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, refine_prefix_uris_file):
    widely_used_namespace_and_uri_result = []

    # Comparison of prefix list and minimal URI detected by shaXer
    for line in shaper_result.splitlines():
        if ("[<http" in line and ">~]" in line):
            shaper_result_uri = line[line.find("[<http")+2:line.find(">~]")]

            # Determine if the same URI is included in the prefix defined in the input file,
            # and if it is included, get the Namespace
            input_namespace = "Undefined"
            for input_prefix in input_prefixes:
                if shaper_result_uri == input_prefix[1]:
                    input_namespace = input_prefix[0]
                    break

            # Obtain namespaces and URIs to suggest, formatting them for output
            suggest_string = get_suggest_string_for_widely_used_namespace_and_uri(input_namespace, shaper_result_uri, widely_used_prefixes_dict, refine_prefix_uris_file)

            # If the string for the suggestion you got exists and is not yet included in the results
            if suggest_string not in widely_used_namespace_and_uri_result and len(suggest_string) > 0:
                    widely_used_namespace_and_uri_result.append(suggest_string)

    # Comparing of prefix list and prefixes in input file
    for input_prefix in input_prefixes:
        input_namespace = input_prefix[0]
        input_uri = input_prefix[1]

        # Obtain namespaces and URIs to suggest, formatting them for output
        suggest_string = get_suggest_string_for_widely_used_namespace_and_uri(input_namespace, input_uri, widely_used_prefixes_dict, refine_prefix_uris_file)

        # If the string for the suggestion you got exists and is not yet included in the results
        if suggest_string not in widely_used_namespace_and_uri_result and len(suggest_string) > 0:
            widely_used_namespace_and_uri_result.append(suggest_string)

    return widely_used_namespace_and_uri_result


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
def get_default_namespaces_dict():
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

# Returns the extension of the given filename
def get_extension(input_file):
    return Path(input_file).suffix

# Returns the second extension from the end of the given filename
def get_extension_before_compression(input_file):
    return Path(Path(input_file).stem).suffix

# Obtain the target file format by input from the user
def get_target_file_types(exists_file_types):
    target_file_types = []

    if len(exists_file_types) > 1:
        print("The following types of files were found.")
        for key, value in FILE_TYPE_DICT.items():
            if key in exists_file_types:
                print(value)

        while True:
            user_input = input("\n1: Process all\n2: Specify file type\n(1/2):")
            if user_input == "1":
                is_process_all = True
                break
            elif user_input == "2":
                is_process_all = False
                break

    for exists_file_type in exists_file_types:
        if len(exists_file_types) == 1 or is_process_all:
            target_file_types.append(exists_file_type)
        else:
            while True:
                user_input = input("Process " + FILE_TYPE_DICT[exists_file_type] + " files?(y/n): ").lower()
                if user_input in ["y", "ye", "yes", ]:
                    target_file_types.append(exists_file_type)
                    break
                elif user_input in ["n", "no"]:
                    break

    return target_file_types

# Determines if a file is to be processed based on the file passed as an argument and the target file type.
def is_target_file(input_file_list, target_file_types):

    if input_file_list[1] is None:
        if input_file_list[2] == TURTLE:
            if FILE_TYPE_TTL in target_file_types:
                return True
        elif input_file_list[2] == NT:
            if FILE_TYPE_NT in target_file_types:
                return True
        elif input_file_list[2] == RDF_XML:
            if FILE_TYPE_RDF_XML in target_file_types:
                return True
    elif input_file_list[1] == GZ:
        if input_file_list[2] == TURTLE:
            if FILE_TYPE_TTL_GZ in target_file_types:
                return True
        elif input_file_list[2] == NT:
            if FILE_TYPE_NT_GZ in target_file_types:
                return True
        elif input_file_list[2] == RDF_XML:
            if FILE_TYPE_RDF_XML_GZ in target_file_types:
                return True
    elif input_file_list[1] == ZIP:
        if input_file_list[2] == TURTLE:
            if FILE_TYPE_TTL_ZIP in target_file_types:
                return True
        elif input_file_list[2] == NT:
            if FILE_TYPE_NT_ZIP in target_file_types:
                return True
        elif input_file_list[2] == RDF_XML:
            if FILE_TYPE_RDF_XML_ZIP in target_file_types:
                return True

    return False

# If a Turtle or RDF/XML file is entered
# Generates and returns a namespace to be passed to sheXer.
# Includes a process to assign a temporary namespace to a non-genuine URI to prevent collisions when multiple namespaces with different URIs exist.
def get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict):
    namespaces_dict = {}
    temp_namespace_index = 1
    for input_prefix in input_prefixes:
        # Check for the existence of the same namespace name with different URIs
        if input_prefix[0] in duplicated_prefixes_dict:
            # # If there is a match in prefixes.tsv for both namespace and URI, it is considered legitimate and the namespace is determined as is.
            if input_prefix[0] in widely_used_prefixes_dict and widely_used_prefixes_dict[input_prefix[0]] == input_prefix[1]:
                namespaces_dict[input_prefix[1]] = input_prefix[0].replace(":","")
            else:
                # If there is no match, assign a temporary namespace such as ns1, ns2, etc., since they are not legitimate.
                namespaces_dict[input_prefix[1]] = "ns" + str(temp_namespace_index)
                temp_namespace_index += 1
        else:
            namespaces_dict[input_prefix[1]] = input_prefix[0].replace(":","")

    return namespaces_dict

# Extracts the corresponding namespace from a dictionary of namespace/URI pairs passed as a parameter,
# and returns it as an array, conditional on the uri also passed as a parameter.
def get_widely_used_namespace_by_uri(uri, widely_used_prefixes_dict):
    result = []
    for key, value in widely_used_prefixes_dict.items():
        if value == uri and key not in result:
            result.append(key)

    return result

# Extracts the corresponding uri from a dictionary of namespace/URI pairs passed as a parameter,
# and returns it as a string, conditional on the namespace also passed as a parameter.
# The dictionary is unique with namespace as the key, so the corresponding value is returned when it is found.
def get_widely_used_uri_by_namespace(namespace, widely_used_prefixes_dict):
    for key, value in widely_used_prefixes_dict.items():
        if key == namespace:
            # Since the namespace is unique, it ends when it is found.
            return value

    return None


# Obtain namespaces and URIs to suggest, formatting them for output
def get_suggest_string_for_widely_used_namespace_and_uri(input_namespace, input_uri, widely_used_prefixes_dict, refine_prefix_uris_file):
    suggest_string = input_namespace + "\t" + input_uri + "\t"
    exists_suggest = False

    refine_prefix_uris = get_refine_prefix_uris(refine_prefix_uris_file)

    # Obtain the corresponding namespace in the list obtained from prefixes.tsv using the URI as a key
    widely_used_namespaces = get_widely_used_namespace_by_uri(input_uri, widely_used_prefixes_dict)

    # Output only if input values differ from widely used values
    if len(widely_used_namespaces) > 0:
        match = False
        for widely_used_namespace in widely_used_namespaces:
            if widely_used_namespace == input_namespace:
                # If any of the Namespace of the prefixes entered correspond to the list retrieved from prefixes.tsv
                match = True

        if not match:
            # Suggest only if the prefix Namespace entered does not correspond to the list retrieved from prefixes.tsv
            suggest_string += '|'.join(widely_used_namespaces)
            exists_suggest = True
    else:
        # If the prefix URI entered corresponds to a key in the list obtained from refine-prefix-uris
        if input_uri in refine_prefix_uris:
            # Get the converted URI
            refine_prefix_uri = refine_prefix_uris[input_uri]
            # Refer to the list obtained from prefixes.tsv subject to the converted URI and obtain Namespace
            widely_used_namespaces = get_widely_used_namespace_by_uri(refine_prefix_uri, widely_used_prefixes_dict)
            if len(widely_used_namespaces) > 0:
                match = False
                for widely_used_namespace in widely_used_namespaces:
                    if widely_used_namespace == input_namespace:
                        # If any of the Namespace prefixes entered correspond to the list retrieved from prefixes.tsv
                        match = True
                if not match:
                    # Suggest only if the prefix Namespace entered does not correspond to the list retrieved from prefixes.tsv
                    suggest_string +=   '|'.join(widely_used_namespaces)
                    exists_suggest = True

    suggest_string += "\t"

    # Obtain the corresponding URI in the list obtained from prefixes.tsv using Namespace as a key
    widely_used_uri = get_widely_used_uri_by_namespace(input_namespace, widely_used_prefixes_dict)
    if widely_used_uri is not None:
        # If present in the list retrieved from prefixes.tsv
        if input_uri != widely_used_uri:
            suggest_string += widely_used_uri
            exists_suggest = True
    else:
        # If not present in the list retrieved from prefixes.tsv
        if input_uri in refine_prefix_uris:
            # If the entered prefix URI corresponds to a key in the list obtained from refine-prefix-uris, the URI is suggested.
            widely_used_uri = refine_prefix_uris[input_uri]
            suggest_string += widely_used_uri
            exists_suggest = True

    suggest_string += "\n"

    if exists_suggest:
        return suggest_string
    else:
        return ""

# Returns the usage percentage of the specified disk
def get_disk_usage_percentage(path):
    disk_usage = shutil.disk_usage(path)
    return disk_usage.used / disk_usage.total * 100