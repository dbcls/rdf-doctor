import unittest
from doctor.doctor import get_command_line_args
from doctor.consts import TARGET_CLASS_ALL, PREFIXES_FILE_PATH, TMP_DISK_USAGE_LIMIT_DEFAULT
from tests.consts import NT_1, TTL_1, TTL_2, TTL_3, REFINE_PREFIX_URIS_FILE_PATH, REFINE_CLASS_URIS_FILE_PATH
import argparse
from pathlib import Path

class TestGetCommandLineArgs(unittest.TestCase):

    def test_nt(self):
        result = get_command_line_args(["--input", NT_1])
        self.assertEqual(result, argparse.Namespace(verbose=False, \
                                                    input=[NT_1], \
                                                    type=None, \
                                                    report=False, \
                                                    output=None, \
                                                    classes=[TARGET_CLASS_ALL], \
                                                    each=False, \
                                                    tmp_dir=None, \
                                                    tmp_dir_disk_usage_limit=TMP_DISK_USAGE_LIMIT_DEFAULT, \
                                                    prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                    class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                    prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                    force_format=None))

    def test_ttl(self):
        result = get_command_line_args(["--input", TTL_1, TTL_2, TTL_3, \
                                        "--report", \
                                        "--output", "./output.shex", \
                                        "--classes", "<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>", \
                                        "--force-format", "turtle", \
                                        "--prefix-uri-dict", str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                        "--class-uri-dict", str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                        "--prefix-list", str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH))])
        self.assertEqual(result, argparse.Namespace(verbose=False, \
                                                    input=[TTL_1, TTL_2, TTL_3], \
                                                    type=None, \
                                                    report=True, \
                                                    output="./output.shex", \
                                                    classes=["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"], \
                                                    each=False, \
                                                    tmp_dir=None, \
                                                    tmp_dir_disk_usage_limit=TMP_DISK_USAGE_LIMIT_DEFAULT, \
                                                    prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                    class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                    prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                    force_format="turtle"))

    def test_ttl_format_nt(self):
        result = get_command_line_args(["--input", TTL_1, \
                                        "--force-format", "nt"])
        self.assertEqual(result, argparse.Namespace(verbose=False, \
                                                    input=[TTL_1], \
                                                    type=None, \
                                                    report=False, \
                                                    output=None, \
                                                    classes=[TARGET_CLASS_ALL], \
                                                    each=False, \
                                                    tmp_dir=None, \
                                                    tmp_dir_disk_usage_limit=TMP_DISK_USAGE_LIMIT_DEFAULT, \
                                                    prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                    class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                    prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                    force_format="nt"))

    def test_tmp_dir(self):
        result = get_command_line_args(["--input", TTL_1, \
                                        "--tmp-dir", "/tmp"])
        self.assertEqual(result, argparse.Namespace(verbose=False, \
                                                    input=[TTL_1], \
                                                    type=None, \
                                                    report=False, \
                                                    output=None, \
                                                    classes=[TARGET_CLASS_ALL], \
                                                    each=False, \
                                                    tmp_dir="/tmp", \
                                                    tmp_dir_disk_usage_limit=TMP_DISK_USAGE_LIMIT_DEFAULT, \
                                                    prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                    class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                    prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                    force_format=None))

    def test_tmp_dir_disk_usage_limit(self):
        result = get_command_line_args(["--input", TTL_1, \
                                        "--tmp-dir-disk-usage-limit", "70"])
        self.assertEqual(result, argparse.Namespace(verbose=False, \
                                                    input=[TTL_1], \
                                                    type=None, \
                                                    report=False, \
                                                    output=None, \
                                                    classes=[TARGET_CLASS_ALL], \
                                                    each=False, \
                                                    tmp_dir=None, \
                                                    tmp_dir_disk_usage_limit=70, \
                                                    prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                    class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                    prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                    force_format=None))

if __name__ == "__main__":
    unittest.main()