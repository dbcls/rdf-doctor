import unittest
from doctor.doctor import validate_command_line_args_other
from doctor.consts import TARGET_CLASS_ALL
from tests.consts import BASE_DIR, NT_1, NT_1_GZ, NT_2, NT_2_GZ, NT_3, NT_3_GZ, TTL_1, TTL_1_GZ, TTL_2, TTL_2_GZ, TTL_3, TTL_3_GZ, REFINE_PREFIX_URIS_FILE_PATH, REFINE_CLASS_URIS_FILE_PATH, PREFIXES_FILE_PATH
from shexer.consts import NT, TURTLE
import argparse
from pathlib import Path

class TestValidateCommnadLineArgsOther(unittest.TestCase):

    # [output/OK] ./output.shex
    def test_output_shex(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[TTL_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output="./", \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, None)

    # [output/ERROR] Permission denied directory
    def test_output_permission_denied(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[TTL_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output="/", \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        print(error_msg)
        self.assertEqual(error_msg, "Output directory error: You don't have write permission on the output directory.")

    # [output/ERROR] Nonexistent directory
    def test_output_nonexistent_dir(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[TTL_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output="./aaa/output.shex", \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, "Output directory error: Output directory does not exist.")

    # [class/OK] Specify one class
    def test_class_specify_one(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[TTL_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=["<http://xmlns.com/foaf/0.1/Person>"], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, None)

    # [class/OK] Specify multiple classes
    def test_class_specify_two(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[TTL_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, None)

    # [class/ERROR] Specify one class in addition to "all"
    def test_class_specify_one_and_all(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[TTL_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL, "<http://xmlns.com/foaf/0.1/Person>"], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, 'Target class error: If "all" is specified, other classes cannot be specified.')

    # [prefix_uri_dict/OK] default file
    def test_prefix_uri_dict_default_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, None)

    # [prefix_uri_dict/OK] specified file
    def test_prefix_uri_dict_specified_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, None)

    # [prefix_uri_dict/NG] Nonexistent file
    def test_prefix_uri_dict_nonexistent_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath("aaa.tsv")), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, "Prefix URIs dictionary file error: Prefix dictionary does not exist or you don't have read permission.")

    # [prefix_uri_dict/NG] shex mode and specified_file
    def test_prefix_uri_dict_shex_specified_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
#        self.assertFalse(result)
#        self.assertEqual(error_msg, 'Prefix URIs dictionary file error: Prefix URIs dictionary file can only be specified if "md"(same as "markdown") is specified in the -r, --report option.')
        self.assertEqual(error_msg, None)

    # [class_uri_dict/OK] default file
    def test_class_uri_dict_default_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, None)

    # [class_uri_dict/OK] specified file
    def test_class_uri_dict_specified_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, None)

    # [class_uri_dict/NG] Nonexistent file
    def test_class_uri_dict_nonexistent_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath("aaa.tsv")), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, "Class URIs dictionary file error: Class dictionary does not exist or you don't have read permission.")

    # [class_uri_dict/NG] shex mode and specified_file
    def test_class_uri_dict_shex_specified_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
#        self.assertFalse(result)
#        self.assertEqual(error_msg, 'Class URIs dictionary file error: Class URIs dictionary file can only be specified if "md"(same as "markdown") is specified in the -r, --report option.')
        self.assertEqual(error_msg, None)


    # [force_format/NG] Bad input format
    def test_force_format_invalid(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format="aaa"))
        self.assertEqual(error_msg, 'Input format error: "aaa" is an unsupported input format. "turtle", "nt" and "xml"(=RDF/XML) are supported.')

    # [prefix_list/OK] default file
    def test_prefix_list_default_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, None)

    # [prefix_list/OK] specified file
    def test_prefix_list_specified_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_MD, \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, None)

    # [prefix_list/NG] Nonexistent file
    def test_prefix_list_nonexistent_file(self):
        error_msg = validate_command_line_args_other(argparse.Namespace(input=[NT_1], \
#                                                                            report=REPORT_FORMAT_SHEX, \ \
                                                                            output=None, \
                                                                            classes=[TARGET_CLASS_ALL], \
                                                                            prefix_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                                            class_uri_dict=str(Path(__file__).resolve().parent.parent.joinpath("doctor").joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                                            prefix_list=str(Path(__file__).resolve().parent.joinpath("aaa.tsv")), \
                                                                            force_format=None, \
                                                                            type=None, \
                                                                            tmp_dir=None, \
                                                                            tmp_dir_disk_usage_limit=95))
        self.assertEqual(error_msg, "Prefix list file error: Prefix list does not exist or you don't have read permission.")

if __name__ == "__main__":
    unittest.main()
