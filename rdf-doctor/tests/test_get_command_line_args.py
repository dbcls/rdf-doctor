import unittest
from doctor import get_command_line_args
import argparse

class TestGetCommandLineArgs(unittest.TestCase):

    def test_get_command_line_args_1(self):
        result = get_command_line_args(["--input", "tests/test_files/test_nt_1.nt"])
        self.assertEqual(result, argparse.Namespace(classes=["all"], input="tests/test_files/test_nt_1.nt", output=None, report="shex", version=False))

    def test_get_command_line_args_2(self):
        result = get_command_line_args(["--input", "tests/test_files/test_ttl_1.ttl", "--report", "md", "--output", "./output.shex", "--classes", "<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"])
        self.assertEqual(result, argparse.Namespace(classes=["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"], input="tests/test_files/test_ttl_1.ttl", output="./output.shex", report="md", version=False))

    def test_get_command_line_args_3(self):
        result = get_command_line_args(["--input", "tests/test_files/test_ttl_1.ttl", "--report", "shex+", "--classes", "all"])
        self.assertEqual(result, argparse.Namespace(classes=["all"], input="tests/test_files/test_ttl_1.ttl", output=None, report="shex+", version=False))

if __name__ == "__main__":
    unittest.main()