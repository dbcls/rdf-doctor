import unittest
from doctor.doctor import get_markdown_result
from doctor.consts import REPORT_FORMAT_SHEX, REPORT_FORMAT_MD, TARGET_CLASS_ALL
from shexer.consts import NT, TURTLE, GZ
import argparse

class TestGetOutputMarkdown(unittest.TestCase):

    def test_get_markdown_result_nt(self):
        output = get_markdown_result(argparse.Namespace(input="tests/test_files/test_nt_3.nt", \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL]),
                                    NT,
                                    None)

        with open("tests/test_files/output/test_nt_3.md", "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

    def test_get_markdown_result_nt_gz(self):
        output = get_markdown_result(argparse.Namespace(input="tests/test_files/test_nt_1.nt.gz", \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL]),
                                    NT,
                                    GZ)

        with open("tests/test_files/output/test_nt_1_gz.md", "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

    def test_get_markdown_result_ttl(self):
        output = get_markdown_result(argparse.Namespace(input="tests/test_files/test_ttl_3.ttl", \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL]),
                                    TURTLE,
                                    None)

        with open("tests/test_files/output/test_ttl_3.md", "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

    def test_get_markdown_result_ttl_gz(self):
        output = get_markdown_result(argparse.Namespace(input="tests/test_files/test_ttl_1.ttl.gz", \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL]),
                                    TURTLE,
                                    GZ)

        with open("tests/test_files/output/test_ttl_1_gz.md", "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

if __name__ == "__main__":
    unittest.main()
