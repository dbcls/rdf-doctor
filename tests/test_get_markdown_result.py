import unittest
from doctor.doctor import get_markdown_result
from doctor.consts import REPORT_FORMAT_MD, TARGET_CLASS_ALL
from tests.consts import NT_1_GZ, NT_3, TTL_1_GZ, TTL_3, OUTPUT_NT_1_GZ_MD, OUTPUT_NT_3_MD, OUTPUT_TTL_1_GZ_MD, OUTPUT_TTL_3_MD, PREFIX_ERRATA_FILE_PATH, CLASS_ERRATA_FILE_PATH
from shexer.consts import NT, TURTLE, GZ
import argparse
from pathlib import Path

class TestGetOutputMarkdown(unittest.TestCase):

    def test_nt(self):
        output = get_markdown_result(NT_3,
                                    NT,
                                    None,
                                    [TARGET_CLASS_ALL],
                                    str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)),
                                    str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH)))

        with open(OUTPUT_NT_3_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

    def test_nt_gz(self):
        output = get_markdown_result(NT_1_GZ,
                                    NT,
                                    GZ,
                                    [TARGET_CLASS_ALL],
                                    str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)),
                                    str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH)))

        with open(OUTPUT_NT_1_GZ_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

    def test_ttl(self):
        output = get_markdown_result(TTL_3,
                                    TURTLE,
                                    None,
                                    [TARGET_CLASS_ALL],
                                    str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)),
                                    str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH)))

        with open(OUTPUT_TTL_3_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

    def test_ttl_gz(self):
        output = get_markdown_result(TTL_1_GZ,
                                    TURTLE,
                                    GZ,
                                    [TARGET_CLASS_ALL],
                                    str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)),
                                    str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH)))

        with open(OUTPUT_TTL_1_GZ_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(output), correct_output)

if __name__ == "__main__":
    unittest.main()
