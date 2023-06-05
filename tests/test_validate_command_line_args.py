import unittest
from doctor.doctor import validate_command_line_args
from doctor.consts import REPORT_FORMAT_SHEX, REPORT_FORMAT_MD, TARGET_CLASS_ALL
from tests.consts import BASE_DIR, NT_1, NT_1_GZ, TTL_1, TTL_1_GZ, PREFIX_ERRATA_FILE_PATH, CLASS_ERRATA_FILE_PATH
import argparse
from pathlib import Path

class TestValidateCommnadLineArgs(unittest.TestCase):

    # [input/OK] n-triple
    def test_input_nt(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle
    def test_input_ttl(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple gz
    def test_input_nt_gz(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1_GZ], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple gz(report=md)
    def test_report_md_nt_gz(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[NT_1_GZ], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle gz
    def test_input_ttl_gz(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1_GZ], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle gz(report=md)
    def test_report_md_ttl_gz(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1_GZ], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/ERROR] Nonexistent file
    def test_input_nonexistent_file(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[BASE_DIR + "aaa.txt"], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Input file error: " + BASE_DIR + "aaa.txt" + " does not exist.")

    # [report/OK] shex
    def test_report_shex(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/OK] md
    def test_report_md(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/OK] markdown
    def test_report_markdown(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report="markdown", \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/ERROR] Bad report format
    def test_report_incorrect(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report="aaa", \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Report format error: "aaa" is an unsupported report format. "shex" and "md"(same as "markdown") are supported.')

    # [output/OK] ./output.shex
    def test_output_shex(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output="./output.shex", \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [output/ERROR] Permission denied directory
    def test_output_permission_denied(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output="/output.shex", \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Output file error: You don't have write permission on the output directory.")

    # [output/ERROR] Nonexistent directory
    def test_output_nonexistent_dir(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output="./aaa/output.shex", \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Output file error: Output directory does not exist.")

    # [class/OK] Specify one class
    def test_class_specify_one(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=["<http://xmlns.com/foaf/0.1/Person>"], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [class/OK] Specify multiple classes
    def test_class_specify_two(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [class/ERROR] Specify one class in addition to "all"
    def test_class_specify_one_and_all(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input=[TTL_1], \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL, "<http://xmlns.com/foaf/0.1/Person>"], \
                                                                            prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)), \
                                                                            class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH))))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Target class error: If "all" is specified, other classes cannot be specified.')

    # [prefix_dict]


    # [class_dict]


if __name__ == "__main__":
    unittest.main()
