import unittest
from doctor.doctor import validate_command_line_args
from doctor.consts import REPORT_FORMAT_SHEX, REPORT_FORMAT_MD, REPORT_FORMAT_MARKDOWN, TARGET_CLASS_ALL
from tests.consts import BASE_DIR, NT_1, NT_1_GZ, NT_2, NT_2_GZ, NT_3, NT_3_GZ, TTL_1, TTL_1_GZ, TTL_2, TTL_2_GZ, TTL_3, TTL_3_GZ, REFINE_PREFIX_URIS_FILE_PATH, REFINE_CLASS_URIS_FILE_PATH, PREFIXES_FILE_PATH
from shexer.consts import NT, TURTLE
import argparse
from pathlib import Path

class TestValidateCommnadLineArgs(unittest.TestCase):

    # [input/OK] n-triple
    def test_input_nt(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple multi
    def test_input_nt_multi(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1, NT_2, NT_3], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle
    def test_input_ttl(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle multi
    def test_input_ttl_multi(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1, TTL_2, TTL_3], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple gz
    def test_input_nt_gz(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1_GZ], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple gz multi
    def test_input_nt_gz_multi(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1_GZ, NT_2_GZ, NT_3_GZ], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple gz(report=md)
    def test_report_md_nt_gz(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1_GZ], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle gz
    def test_input_ttl_gz(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1_GZ], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle gz multi
    def test_input_ttl_gz_multi(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle gz(report=md)
    def test_report_md_ttl_gz(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1_GZ], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/ERROR] Nonexistent file
    def test_input_nonexistent_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[BASE_DIR + "aaa.txt"], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Input file error: " + BASE_DIR + "aaa.txt" + " does not exist.")

    # [input/ERROR] Unsupported extension
    def test_input_unsupported_extension(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH))], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Input file error: ".tsv" is an unsupported extension. ".ttl", ".ttl.gz", ".nt" and ".nt.gz" are supported.')

    # [input/ERROR] Different extensions for multiple file input
    def test_input_different_extension(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1, NT_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Input file error: If you enter multiple files, please use the same extension.")


    # [report/OK] shex
    def test_report_shex(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/OK] md
    def test_report_md(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/OK] markdown
    def test_report_markdown(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_MARKDOWN, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/ERROR] Bad report format
    def test_report_invalid(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report="aaa", \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Report format error: "aaa" is an unsupported report format. "' + REPORT_FORMAT_SHEX + '" and "' + REPORT_FORMAT_MD + '"(same as "' + REPORT_FORMAT_MARKDOWN + '") are supported.')

    # [output/OK] ./output.shex
    def test_output_shex(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output="./output.shex", \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [output/ERROR] Permission denied directory
    def test_output_permission_denied(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output="/output.shex", \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Output file error: You don't have write permission on the output directory.")

    # [output/ERROR] Nonexistent directory
    def test_output_nonexistent_dir(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output="./aaa/output.shex", \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Output file error: Output directory does not exist.")

    # [class/OK] Specify one class
    def test_class_specify_one(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=["<http://xmlns.com/foaf/0.1/Person>"], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [class/OK] Specify multiple classes
    def test_class_specify_two(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [class/ERROR] Specify one class in addition to "all"
    def test_class_specify_one_and_all(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL, "<http://xmlns.com/foaf/0.1/Person>"], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Target class error: If "all" is specified, other classes cannot be specified.')

    # [prefix_dict/OK] default file
    def test_prefix_dict_default_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [prefix_dict/OK] specified file
    def test_prefix_dict_specified_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [prefix_dict/NG] Nonexistent file
    def test_prefix_dict_nonexistent_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath("aaa.tsv")), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Prefix URIs dictionary file error: Prefix dictionary does not exist or you don't have read permission.")

    # [prefix_dict/NG] shex mode and specified_file
    def test_prefix_dict_shex_specified_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Prefix URIs dictionary file error: Prefix URIs dictionary file can only be specified if "md"(same as "markdown") is specified in the -r, --report option.')

    # [class_dict/OK] default file
    def test_class_dict_default_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [class_dict/OK] specified file
    def test_class_dict_specified_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [class_dict/NG] Nonexistent file
    def test_class_dict_nonexistent_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath("aaa.tsv")), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Class URIs dictionary file error: Class dictionary does not exist or you don't have read permission.")

    # [class_dict/NG] shex mode and specified_file
    def test_class_dict_shex_specified_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Class URIs dictionary file error: Class URIs dictionary file can only be specified if "md"(same as "markdown") is specified in the -r, --report option.')


    # [force_format/NG] Bad input format
    def test_force_format_invalid(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format="aaa"))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Input format error: "aaa" is an unsupported input format. "' + TURTLE + '" and "' + NT + '" are supported.')

    # [prefix_list/OK] default file
    def test_prefix_list_default_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [prefix_list/OK] specified file
    def test_prefix_list_specified_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [prefix_list/NG] Nonexistent file
    def test_prefix_list_nonexistent_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.joinpath("aaa.tsv")), \
                                                                            force_format=None))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Prefix list file error: Prefix list does not exist or you don't have read permission.")

if __name__ == "__main__":
    unittest.main()
