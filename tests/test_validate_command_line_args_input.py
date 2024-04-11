import unittest
from doctor.doctor import validate_command_line_args_input
from doctor.consts import TARGET_CLASS_ALL
from tests.consts import BASE_DIR, NT_1, NT_1_GZ, NT_2, NT_2_GZ, NT_3, NT_3_GZ, TTL_1, TTL_1_GZ, TTL_2, TTL_2_GZ, TTL_3, TTL_3_GZ, REFINE_PREFIX_URIS_FILE_PATH, REFINE_CLASS_URIS_FILE_PATH, PREFIXES_FILE_PATH
import argparse
from pathlib import Path

class TestValidateCommnadLineArgsInput(unittest.TestCase):

    # [input/OK] n-triple
    def test_input_nt(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [NT_1])
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple multi
    def test_input_nt_multi(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[NT_1, NT_2, NT_3], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [NT_1, NT_2, NT_3])
        self.assertEqual(error_msg, None)

    # [input/OK] turtle
    def test_input_ttl(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[TTL_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [TTL_1])
        self.assertEqual(error_msg, None)

    # [input/OK] turtle multi
    def test_input_ttl_multi(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[TTL_1, TTL_2, TTL_3], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [TTL_1, TTL_2, TTL_3])
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple gz
    def test_input_nt_gz(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[NT_1_GZ], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [NT_1_GZ])
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple gz multi
    def test_input_nt_gz_multi(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[NT_1_GZ, NT_2_GZ, NT_3_GZ], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [NT_1_GZ, NT_2_GZ, NT_3_GZ])
        self.assertEqual(error_msg, None)

    # [input/OK] n-triple gz(report=md)
    def test_report_md_nt_gz(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[NT_1_GZ], \
#                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [NT_1_GZ])
        self.assertEqual(error_msg, None)

    # [input/OK] turtle gz
    def test_input_ttl_gz(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[TTL_1_GZ], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [TTL_1_GZ])
        self.assertEqual(error_msg, None)

    # [input/OK] turtle gz multi
    def test_input_ttl_gz_multi(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [TTL_1_GZ, TTL_2_GZ, TTL_3_GZ])
        self.assertEqual(error_msg, None)

    # [input/OK] turtle gz(report=md)
    def test_report_md_ttl_gz(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[TTL_1_GZ], \
#                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [TTL_1_GZ])
        self.assertEqual(error_msg, None)

    # [input/ERROR] Nonexistent file
    def test_input_nonexistent_file(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[BASE_DIR + "aaa.txt"], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [BASE_DIR + "aaa.txt"])
        self.assertEqual(error_msg, "Input file error: " + BASE_DIR + "aaa.txt" + " does not exist.")

    # [input/ERROR] Unsupported extension
    def test_input_unsupported_extension(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH))], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH))])
        self.assertEqual(error_msg, 'Input file error: ".tsv" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.')

    # [input/ERROR] Different extensions for multiple file input
    def test_input_different_extension(self):
        error_msg = validate_command_line_args_input(argparse.Namespace(input=[TTL_1, NT_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95), \
                                                                            [TTL_1, NT_1])
        self.assertEqual(error_msg, 'Input file error: Input file extension could not be processed properly.')


if __name__ == "__main__":
    unittest.main()
