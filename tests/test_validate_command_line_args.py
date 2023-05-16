import unittest
from doctor.doctor import validate_command_line_args
from doctor.consts import REPORT_FORMAT_SHEX, REPORT_FORMAT_MD, TARGET_CLASS_ALL
import argparse

class TestValidateCommnadLineArgs(unittest.TestCase):

    # [input/OK] n-triple
    def test_validate_command_line_args_input_1(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_nt_1.nt", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle
    def test_validate_command_line_args_input_2(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple gz
    def test_validate_command_line_args_input_3(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_nt_1.nt.gz", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle gz
    def test_validate_command_line_args_input_4(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl.gz", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/ERROR] Nonexistent file
    def test_validate_command_line_args_input_5(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/aaa.txt", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Input file error: Input file does not exist.")

    # [report/OK] shex
    def test_validate_command_line_args_report_1(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/OK] md
    def test_validate_command_line_args_report_2(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/OK] md gz
    def test_validate_command_line_args_report_3(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl.gz", \
                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/OK] markdown
    def test_validate_command_line_args_report_4(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report="markdown", \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/ERROR] Bad report format
    def test_validate_command_line_args_report_5(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report="aaa", \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Report format error: "aaa" is an unsupported report format. "shex" and "md"(same as "markdown") are supported.')

    # [output/OK] ./test.shex
    def test_validate_command_line_args_output_1(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output="./output.shex", \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [output/ERROR] Permission denied directory
    def test_validate_command_line_args_output_2(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output="/output.shex", \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Output file error: You don't have write permission on the output directory.")

    # [output/ERROR] Nonexistent directory
    def test_validate_command_line_args_output_3(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output="./aaa/output.shex", \
                                                                            classes=[TARGET_CLASS_ALL]))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Output file error: Output directory does not exist.")

    # [class/OK] Specify one class
    def test_validate_command_line_args_class_1(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=["<http://xmlns.com/foaf/0.1/Person>"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [class/OK] Specify multiple classes
    def test_validate_command_line_args_class_2(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [class/ERROR] Specify one class in addition to "all"
    def test_validate_command_line_args_class_3(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", \
                                                                            report=REPORT_FORMAT_SHEX, \
                                                                            output=None, \
                                                                            classes=["all", "<http://xmlns.com/foaf/0.1/Person>"]))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Target class error: If "all" is specified, other classes cannot be specified.')

if __name__ == "__main__":
    unittest.main()
