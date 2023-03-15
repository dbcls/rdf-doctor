import unittest
from doctor import validate_command_line_args
import argparse

class TestValidateCommnadLineArgs(unittest.TestCase):

    # [input/OK] n-triple
    def test_validate_command_line_args_1(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_nt_1.nt", report="shex", output=None, classes=["all"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/OK] turtle
    def test_validate_command_line_args_2(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="shex", output=None, classes=["all"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [input/ERROR] Nonexistent file
    def test_validate_command_line_args_3(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/aaa.txt", report="shex", output=None, classes=["all"]))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Input file error: Input file does not exist.")

    # [report/OK] shex
    def test_validate_command_line_args_4(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="shex", output=None, classes=["all"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/OK] md
    def test_validate_command_line_args_5(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="md", output=None, classes=["all"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/OK] markdown
    def test_validate_command_line_args_6(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="markdown", output=None, classes=["all"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/OK] shex+
    def test_validate_command_line_args_7(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="shex+", output=None, classes=["all"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [report/ERROR] Bad report format
    def test_validate_command_line_args_8(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="aaa", output=None, classes=["all"]))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Report format error: "aaa" is an unsupported report format. "shex", "markdown", "md" and "shex+" are supported.')

    # [output/OK] ./test.shex
    def test_validate_command_line_args_9(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="shex", output="./output.shex", classes=["all"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [output/ERROR] Permission denied directory
    def test_validate_command_line_args_10(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="shex", output="/output.shex", classes=["all"]))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Output file error: You don't have write permission on the output directory.")

    # [output/ERROR] Nonexistent directory
    def test_validate_command_line_args_11(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="shex", output="./aaa/output.shex", classes=["all"]))
        self.assertFalse(result)
        self.assertEqual(error_msg, "Output file error: Output directory does not exist.")

    # [class/OK] Specify one class
    def test_validate_command_line_args_12(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="shex", output=None, classes=["<http://xmlns.com/foaf/0.1/Person>"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [class/OK] Specify multiple classes
    def test_validate_command_line_args_13(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="shex", output=None, classes=["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"]))
        self.assertTrue(result)
        self.assertEqual(error_msg, None)

    # [class/ERROR] Specify one class in addition to "all"
    def test_validate_command_line_args_14(self):
        result, error_msg = validate_command_line_args(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl", report="shex", output=None, classes=["all", "<http://xmlns.com/foaf/0.1/Person>"]))
        self.assertFalse(result)
        self.assertEqual(error_msg, 'Target class error: If "all" is specified, other classes cannot be specified.')

if __name__ == "__main__":
    unittest.main()
