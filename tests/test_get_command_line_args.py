import unittest
from doctor.doctor import get_command_line_args
from doctor.consts import TARGET_CLASS_ALL, REPORT_FORMAT_SHEX, REPORT_FORMAT_MD, PREFIX_LIST_FILE_PATH
from tests.consts import NT_1, TTL_1, TTL_2, TTL_3, PREFIX_URI_ERRATA_FILE_PATH, CLASS_URI_ERRATA_FILE_PATH
import argparse
from pathlib import Path

class TestGetCommandLineArgs(unittest.TestCase):

    def test_nt(self):
        result = get_command_line_args(["--input", NT_1])
        self.assertEqual(result, argparse.Namespace(input=[NT_1], \
                                                    report=REPORT_FORMAT_SHEX, \
                                                    output=None, \
                                                    classes=[TARGET_CLASS_ALL], \
                                                    prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIX_URI_ERRATA_FILE_PATH)), \
                                                    class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(CLASS_URI_ERRATA_FILE_PATH)), \
                                                    prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIX_LIST_FILE_PATH)), \
                                                    force_format=None, \
                                                    verbose=False))

    def test_ttl(self):
        result = get_command_line_args(["--input", TTL_1, TTL_2, TTL_3, \
                                        "--report", REPORT_FORMAT_MD, \
                                        "--output", "./output.shex", \
                                        "--classes", "<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>", \
                                        "--force-format", "turtle", \
                                        "--prefix-dict", str(Path(__file__).resolve().parent.joinpath(PREFIX_URI_ERRATA_FILE_PATH)), \
                                        "--class-dict", str(Path(__file__).resolve().parent.joinpath(CLASS_URI_ERRATA_FILE_PATH)), \
                                        "--prefix-list", str(Path(__file__).resolve().parent.joinpath(PREFIX_LIST_FILE_PATH))])
        self.assertEqual(result, argparse.Namespace(input=[TTL_1, TTL_2, TTL_3], \
                                                    report=REPORT_FORMAT_MD, \
                                                    output="./output.shex", \
                                                    classes=["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"], \
                                                    prefix_dict=str(Path(__file__).resolve().parent.joinpath(PREFIX_URI_ERRATA_FILE_PATH)), \
                                                    class_dict=str(Path(__file__).resolve().parent.joinpath(CLASS_URI_ERRATA_FILE_PATH)), \
                                                    prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIX_LIST_FILE_PATH)), \
                                                    force_format="turtle", \
                                                    verbose=False))

    def test_ttl_format_nt(self):
        result = get_command_line_args(["--input", TTL_1, \
                                        "--force-format", "nt"])
        self.assertEqual(result, argparse.Namespace(input=[TTL_1], \
                                                    report=REPORT_FORMAT_SHEX, \
                                                    output=None, \
                                                    classes=[TARGET_CLASS_ALL], \
                                                    prefix_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIX_URI_ERRATA_FILE_PATH)), \
                                                    class_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(CLASS_URI_ERRATA_FILE_PATH)), \
                                                    prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIX_LIST_FILE_PATH)), \
                                                    force_format="nt", \
                                                    verbose=False))

if __name__ == "__main__":
    unittest.main()