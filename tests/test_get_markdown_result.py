import unittest
from doctor.doctor import get_markdown_result
from doctor.consts import REPORT_FORMAT_MD, TARGET_CLASS_ALL
from tests.consts import NT_1_GZ, NT_3, TTL_1_GZ, TTL_3, OUTPUT_NT_1_GZ_MD, OUTPUT_NT_3_MD, OUTPUT_TTL_1_GZ_MD, OUTPUT_TTL_3_MD
from shexer.consts import NT, TURTLE, GZ
import argparse

class TestGetOutputMarkdown(unittest.TestCase):

    def test_nt(self):
        output = get_markdown_result(argparse.Namespace(input=NT_3, \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL]),
                                    NT,
                                    None)

        with open(OUTPUT_NT_3_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

    def test_nt_gz(self):
        output = get_markdown_result(argparse.Namespace(input=NT_1_GZ, \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL]),
                                    NT,
                                    GZ)

        with open(OUTPUT_NT_1_GZ_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

    def test_ttl(self):
        output = get_markdown_result(argparse.Namespace(input=TTL_3, \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL]),
                                    TURTLE,
                                    None)

        with open(OUTPUT_TTL_3_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

    def test_ttl_gz(self):
        output = get_markdown_result(argparse.Namespace(input=TTL_1_GZ, \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL]),
                                    TURTLE,
                                    GZ)

        with open(OUTPUT_TTL_1_GZ_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

if __name__ == "__main__":
    unittest.main()