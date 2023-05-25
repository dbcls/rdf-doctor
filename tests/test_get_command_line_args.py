import unittest
from doctor.doctor import get_command_line_args
from doctor.consts import TARGET_CLASS_ALL, REPORT_FORMAT_SHEX, REPORT_FORMAT_MD
from tests.consts import NT_1, TTL_1
import argparse

class TestGetCommandLineArgs(unittest.TestCase):

    def test_nt(self):
        result = get_command_line_args(["--input", NT_1])
        self.assertEqual(result, argparse.Namespace(classes=[TARGET_CLASS_ALL], \
                                                    input=NT_1, \
                                                    output=None, \
                                                    report=REPORT_FORMAT_SHEX))

    def test_ttl(self):
        result = get_command_line_args(["--input", TTL_1, \
                                        "--report", REPORT_FORMAT_MD, \
                                        "--output", "./output.shex", \
                                        "--classes", "<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"])
        self.assertEqual(result, argparse.Namespace(classes=["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"], \
                                                    input=TTL_1, \
                                                    output="./output.shex", \
                                                    report=REPORT_FORMAT_MD))

if __name__ == "__main__":
    unittest.main()