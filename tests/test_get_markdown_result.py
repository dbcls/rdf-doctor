import unittest
import argparse
import queue
from doctor.doctor import get_markdown_result
from doctor.consts import REPORT_FORMAT_MD, TARGET_CLASS_ALL
from tests.consts import NT_1_GZ, NT_3, TTL_1_GZ, TTL_3, OUTPUT_NT_1_GZ_MD, OUTPUT_NT_3_MD, OUTPUT_TTL_1_GZ_MD, OUTPUT_TTL_3_MD, PREFIX_URI_ERRATA_FILE_PATH, CLASS_URI_ERRATA_FILE_PATH, PREFIX_LIST_FILE_PATH
from shexer.consts import NT, TURTLE, GZ
from pathlib import Path


class TestGetMarkdownResult(unittest.TestCase):

    def test_nt(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[NT_3], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_URI_ERRATA_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_URI_ERRATA_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIX_LIST_FILE_PATH)), \
                                                        verbose=False),
                                    NT,
                                    None,
                                    result_queue)

        with open(OUTPUT_NT_3_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()
        self.assertEqual("".join(result_queue.get()), correct_output)

    def test_nt_gz(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[NT_1_GZ], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_URI_ERRATA_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_URI_ERRATA_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIX_LIST_FILE_PATH)), \
                                                        verbose=False),
                                    NT,
                                    GZ,
                                    result_queue)

        with open(OUTPUT_NT_1_GZ_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(result_queue.get()), correct_output)

    def test_ttl(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[TTL_3], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_URI_ERRATA_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_URI_ERRATA_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIX_LIST_FILE_PATH)), \
                                                        verbose=False),
                                    TURTLE,
                                    None,
                                    result_queue)

        with open(OUTPUT_TTL_3_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(result_queue.get()), correct_output)

    def test_ttl_gz(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[TTL_1_GZ], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_URI_ERRATA_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_URI_ERRATA_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIX_LIST_FILE_PATH)), \
                                                        verbose=False),
                                    TURTLE,
                                    GZ,
                                    result_queue)

        with open(OUTPUT_TTL_1_GZ_MD, "r", encoding="utf-8") as f:
            correct_output = f.read()

        self.assertEqual("".join(result_queue.get()), correct_output)

if __name__ == "__main__":
    unittest.main()
