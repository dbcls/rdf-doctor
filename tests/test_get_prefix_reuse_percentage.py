import unittest
from doctor.doctor import get_prefix_reuse_percentage, get_input_prefixes
from shexer.consts import GZ

class TestGetPrefixReusePercentage(unittest.TestCase):

    def test_get_prefix_reuse_percentage_nt(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_nt_1.nt", None)
        result = get_prefix_reuse_percentage(input_prefixes)
        self.assertEqual(result, None)

    def test_get_prefix_reuse_percentage_ttl(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_ttl_1.ttl", None)
        result = get_prefix_reuse_percentage(input_prefixes)
        self.assertEqual(result, 100.0)

    def test_get_prefix_reuse_percentage_nt_gz(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_nt_1.nt.gz", GZ)
        result = get_prefix_reuse_percentage(input_prefixes)
        self.assertEqual(result, None)

    def test_get_prefix_reuse_percentage_ttl_gz(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_ttl_1.ttl.gz", GZ)
        result = get_prefix_reuse_percentage(input_prefixes)
        self.assertEqual(result, 100.0)

if __name__ == "__main__":
    unittest.main()