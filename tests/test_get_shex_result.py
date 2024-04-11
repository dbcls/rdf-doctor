import unittest
import argparse
import queue
from doctor.doctor import get_shex_result
from doctor.consts import TARGET_CLASS_ALL
from tests.consts import NT_1, NT_1_GZ, NT_2, NT_2_GZ, NT_3, NT_3_GZ, TTL_1, TTL_1_GZ, TTL_2, TTL_2_GZ, TTL_3, TTL_3_GZ, TTL_ERROR, REFINE_PREFIX_URIS_FILE_PATH, REFINE_CLASS_URIS_FILE_PATH, PREFIXES_FILE_PATH, PREFIXES_ERROR_FILE_PATH
from shexer.consts import NT, TURTLE, GZ
from pathlib import Path

# Since the order of the output of sheXer changes each time, only check that the result is list in the normal case.
class TestGetShexResult(unittest.TestCase):
    # TODO: Add value error case
    def test_nt(self):
        result_queue = queue.Queue()
        get_shex_result(argparse.Namespace(input=[NT_1], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [NT_1],
                                    NT,
                                    None,
                                    result_queue)
        self.assertIsInstance(result_queue.get(), list)

    def test_nt_multi(self):
        result_queue = queue.Queue()
        get_shex_result(argparse.Namespace(input=[NT_1, NT_2, NT_3], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [NT_1, NT_2, NT_3],
                                    NT,
                                    None,
                                    result_queue)

        self.assertIsInstance(result_queue.get(), list)

    def test_nt_gz(self):
        result_queue = queue.Queue()
        get_shex_result(argparse.Namespace(input=[NT_1_GZ], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [NT_1_GZ],
                                    NT,
                                    GZ,
                                    result_queue)

        self.assertIsInstance(result_queue.get(), list)

    def test_nt_gz_multi(self):
        result_queue = queue.Queue()
        get_shex_result(argparse.Namespace(input=[NT_1_GZ, NT_2_GZ, NT_3_GZ], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [NT_1_GZ, NT_2_GZ, NT_3_GZ],
                                    NT,
                                    GZ,
                                    result_queue)

        self.assertIsInstance(result_queue.get(), list)

    def test_ttl(self):
        result_queue = queue.Queue()
        get_shex_result(argparse.Namespace(input=[TTL_1], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_1],
                                    TURTLE,
                                    None,
                                    result_queue)

        self.assertIsInstance(result_queue.get(), list)

    def test_ttl_multi(self):
        result_queue = queue.Queue()
        get_shex_result(argparse.Namespace(input=[TTL_1, TTL_2, TTL_3], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_1, TTL_2, TTL_3],
                                    TURTLE,
                                    None,
                                    result_queue)

        self.assertIsInstance(result_queue.get(), list)

    def test_ttl_gz(self):
        result_queue = queue.Queue()
        get_shex_result(argparse.Namespace(input=[TTL_1_GZ], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_1_GZ],
                                    TURTLE,
                                    GZ,
                                    result_queue)

        self.assertIsInstance(result_queue.get(), list)

    def test_ttl_gz_multi(self):
        result_queue = queue.Queue()
        get_shex_result(argparse.Namespace(input=[TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_1_GZ, TTL_2_GZ, TTL_3_GZ],
                                    TURTLE,
                                    GZ,
                                    result_queue)

        self.assertIsInstance(result_queue.get(), list)

    def test_index_error(self):
        result_queue = queue.Queue()
        get_shex_result(argparse.Namespace(input=[TTL_3], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_ERROR_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_3],
                                    TURTLE,
                                    None,
                                    result_queue)
        self.assertEqual(str(result_queue.get()), str(IndexError('An index error has occurred.\n\nIndexError message: list index out of range')))

    def test_exception_error(self):
        result_queue = queue.Queue()
        get_shex_result(argparse.Namespace(input=[TTL_ERROR], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_ERROR],
                                    TURTLE,
                                    None,
                                    result_queue)
        self.assertEqual(str(result_queue.get()), str(Exception("An exception error has occurred.\n\nException message: [Errno 2] No such file or directory: '/test_ttl_error.ttl'")))

if __name__ == "__main__":
    unittest.main()
