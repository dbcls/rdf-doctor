import unittest
from doctor.doctor import get_prefix_reuse_percentage, get_input_prefixes
from tests.consts import NT_1, NT_1_GZ, TTL_1, TTL_2, TTL_3, TTL_1_GZ, PREFIXES_FILE_PATH
from shexer.consts import GZ
from pathlib import Path

class TestGetPrefixReusePercentage(unittest.TestCase):

    def test_nt(self):
        input_prefixes, _ = get_input_prefixes([NT_1], None)
        result = get_prefix_reuse_percentage(input_prefixes, str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        self.assertEqual(result, None)

    def test_ttl_1(self):
        input_prefixes, _ = get_input_prefixes([TTL_1], None)
        result = get_prefix_reuse_percentage(input_prefixes, str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        self.assertEqual(result, 100.0)

    def test_ttl_2(self):
        input_prefixes, _ = get_input_prefixes([TTL_2], None)
        result = get_prefix_reuse_percentage(input_prefixes, str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        self.assertEqual(result, 50.0)

    def test_ttl_3(self):
        input_prefixes, _ = get_input_prefixes([TTL_3], None)
        result = get_prefix_reuse_percentage(input_prefixes, str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        self.assertEqual(result, 80.0)

    def test_nt_gz(self):
        input_prefixes, _ = get_input_prefixes([NT_1_GZ], GZ)
        result = get_prefix_reuse_percentage(input_prefixes, str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        self.assertEqual(result, None)

    def test_ttl_gz(self):
        input_prefixes, _ = get_input_prefixes([TTL_1_GZ], GZ)
        result = get_prefix_reuse_percentage(input_prefixes, str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        self.assertEqual(result, 100.0)

if __name__ == "__main__":
    unittest.main()