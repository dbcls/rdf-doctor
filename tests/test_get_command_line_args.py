import unittest
from doctor.doctor import get_command_line_args
from doctor.consts import TARGET_CLASS_ALL, REPORT_FORMAT_SHEX, REPORT_FORMAT_MD
import argparse

class TestGetCommandLineArgs(unittest.TestCase):

    def test_get_command_line_args_1(self):
        result = get_command_line_args(["--input", "tests/test_files/test_nt_1.nt"])
        self.assertEqual(result, argparse.Namespace(classes=[TARGET_CLASS_ALL], \
                                                    input="tests/test_files/test_nt_1.nt", \
                                                    output=None, \
                                                    report=REPORT_FORMAT_SHEX))

    def test_get_command_line_args_2(self):
        result = get_command_line_args(["--input", "tests/test_files/test_ttl_1.ttl", \
                                        "--report", REPORT_FORMAT_MD, \
                                        "--output", "./output.shex", \
                                        "--classes", "<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"])
        self.assertEqual(result, argparse.Namespace(classes=["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"], \
                                                    input="tests/test_files/test_ttl_1.ttl", \
                                                    output="./output.shex", \
                                                    report=REPORT_FORMAT_MD))

if __name__ == "__main__":
    unittest.main()