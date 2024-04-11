import unittest
from doctor.doctor import get_prefix_reuse_percentage, get_input_prefixes_turtle, get_widely_used_prefixes_dict
from tests.consts import NT_1, NT_1_GZ, TTL_1, TTL_2, TTL_3, TTL_1_GZ, PREFIXES_FILE_PATH
from shexer.consts import GZ
from pathlib import Path

class TestGetPrefixReusePercentage(unittest.TestCase):

    def test_nt(self):
        input_prefixes, _, _ = get_input_prefixes_turtle([NT_1], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        result = get_prefix_reuse_percentage(input_prefixes, widely_used_prefixes_dict)
        self.assertEqual(result, None)

    def test_ttl_1(self):
        input_prefixes, _, _ = get_input_prefixes_turtle([TTL_1], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        result = get_prefix_reuse_percentage(input_prefixes, widely_used_prefixes_dict)
        self.assertEqual(result, 100.0)

    def test_ttl_2(self):
        input_prefixes, _, _ = get_input_prefixes_turtle([TTL_2], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        result = get_prefix_reuse_percentage(input_prefixes, widely_used_prefixes_dict)
        self.assertEqual(result, 50.0)

    def test_ttl_3(self):
        input_prefixes, _, _ = get_input_prefixes_turtle([TTL_3], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        result = get_prefix_reuse_percentage(input_prefixes, widely_used_prefixes_dict)
        self.assertEqual(result, 40.0)

    def test_nt_gz(self):
        input_prefixes, _, _ = get_input_prefixes_turtle([NT_1_GZ], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        result = get_prefix_reuse_percentage(input_prefixes, widely_used_prefixes_dict)
        self.assertEqual(result, None)

    def test_ttl_gz(self):
        input_prefixes, _, _ = get_input_prefixes_turtle([TTL_1_GZ], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        result = get_prefix_reuse_percentage(input_prefixes, widely_used_prefixes_dict)
        self.assertEqual(result, 100.0)

if __name__ == "__main__":
    unittest.main()