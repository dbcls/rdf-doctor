import unittest
import argparse
import queue
from doctor.doctor import get_markdown_result
from doctor.consts import REPORT_FORMAT_MD, TARGET_CLASS_ALL
from tests.consts import NT_1, NT_1_GZ, NT_2, NT_2_GZ, NT_3, NT_3_GZ, TTL_1, TTL_1_GZ, TTL_2, TTL_2_GZ, TTL_3, TTL_3_GZ, OUTPUT_NT_1_GZ_MD, OUTPUT_NT_3_MD, OUTPUT_NT_1_2_3_MD, OUTPUT_NT_1_2_3_GZ_MD, OUTPUT_TTL_1_GZ_MD, OUTPUT_TTL_3_MD, OUTPUT_TTL_1_2_3_MD, OUTPUT_TTL_1_2_3_GZ_MD, REFINE_PREFIX_URIS_FILE_PATH, REFINE_CLASS_URIS_FILE_PATH, PREFIXES_FILE_PATH
from shexer.consts import NT, TURTLE, GZ
from pathlib import Path


class TestGetMarkdownResult(unittest.TestCase):

    def test_nt(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[NT_3], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                        verbose=False),
                                    NT,
                                    None,
                                    result_queue)

        with open(OUTPUT_NT_3_MD, "r", encoding="utf-8") as f:
            sample_output = f.read()
        self.assertEqual("".join(result_queue.get()), sample_output)

    def test_nt_multi(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[NT_1, NT_2, NT_3], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                        verbose=False),
                                    NT,
                                    None,
                                    result_queue)

        with open(OUTPUT_NT_1_2_3_MD, "r", encoding="utf-8") as f:
            sample_output = f.read()
        self.assertEqual("".join(result_queue.get()), sample_output)

    def test_nt_gz(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[NT_1_GZ], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                        verbose=False),
                                    NT,
                                    GZ,
                                    result_queue)

        with open(OUTPUT_NT_1_GZ_MD, "r", encoding="utf-8") as f:
            sample_output = f.read()
        self.assertEqual("".join(result_queue.get()), sample_output)

    def test_nt_gz_multi(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[NT_1_GZ, NT_2_GZ, NT_3_GZ], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                        verbose=False),
                                    NT,
                                    GZ,
                                    result_queue)

        with open(OUTPUT_NT_1_2_3_GZ_MD, "r", encoding="utf-8") as f:
            sample_output = f.read()
        self.assertEqual("".join(result_queue.get()), sample_output)

    def test_ttl(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[TTL_3], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                        verbose=False),
                                    TURTLE,
                                    None,
                                    result_queue)

        with open(OUTPUT_TTL_3_MD, "r", encoding="utf-8") as f:
            sample_output = f.read()
        self.assertEqual("".join(result_queue.get()), sample_output)

    def test_ttl_multi(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[TTL_1, TTL_2, TTL_3], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                        verbose=False),
                                    TURTLE,
                                    None,
                                    result_queue)

        with open(OUTPUT_TTL_1_2_3_MD, "r", encoding="utf-8") as f:
            sample_output = f.read()
        self.assertEqual("".join(result_queue.get()), sample_output)

    def test_ttl_gz(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[TTL_1_GZ], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                        verbose=False),
                                    TURTLE,
                                    GZ,
                                    result_queue)

        with open(OUTPUT_TTL_1_GZ_MD, "r", encoding="utf-8") as f:
            sample_output = f.read()
        self.assertEqual("".join(result_queue.get()), sample_output)

    def test_ttl_gz_multi(self):
        result_queue = queue.Queue()
        get_markdown_result(argparse.Namespace(input=[TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], \
                                                        report=REPORT_FORMAT_MD, \
                                                        output=None, \
                                                        classes=[TARGET_CLASS_ALL], \
                                                        prefix_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                        class_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                        prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                        verbose=False),
                                    TURTLE,
                                    GZ,
                                    result_queue)

        with open(OUTPUT_TTL_1_2_3_GZ_MD, "r", encoding="utf-8") as f:
            sample_output = f.read()
        self.assertEqual("".join(result_queue.get()), sample_output)

if __name__ == "__main__":
    unittest.main()
