import unittest
from doctor.doctor import get_prefix_reuse_percentage
from shexer.consts import NT, TURTLE, GZ

class TestGetPrefixReusePercentage(unittest.TestCase):

    def test_get_prefix_reuse_percentage_nt(self):
        result = get_prefix_reuse_percentage("tests/test_files/test_nt_1.nt", NT, None)
        self.assertEqual(result, None)

    def test_get_prefix_reuse_percentage_ttl(self):
        result = get_prefix_reuse_percentage("tests/test_files/test_ttl_1.ttl", TURTLE, None)
        self.assertEqual(result, 100.0)

    def test_get_prefix_reuse_percentage_nt_gz(self):
        result = get_prefix_reuse_percentage("tests/test_files/test_nt_1.nt.gz", NT, GZ)
        self.assertEqual(result, None)

    def test_get_prefix_reuse_percentage_ttl_gz(self):
        result = get_prefix_reuse_percentage("tests/test_files/test_ttl_1.ttl.gz", TURTLE, GZ)
        self.assertEqual(result, 100.0)

if __name__ == "__main__":
    unittest.main()