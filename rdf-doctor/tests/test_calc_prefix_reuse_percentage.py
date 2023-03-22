import unittest
from doctor import get_prefix_reuse_percentage
from shexer.consts import NT, TURTLE, GZ

class TestCalcPrefixReusePercentage(unittest.TestCase):

    def test_calc_prefix_reuse_percentage_nt(self):
        score, error_msg = get_prefix_reuse_percentage("tests/test_files/test_nt_1.nt", NT, None)
        self.assertEqual(score, None)
        self.assertEqual(error_msg, "Not calculated because there is no prefix defined.")

    def test_calc_prefix_reuse_percentage_ttl(self):
        score, error_msg = get_prefix_reuse_percentage("tests/test_files/test_ttl_1.ttl", TURTLE, None)
        self.assertEqual(score, 100.0)
        self.assertEqual(error_msg, None)

    def test_calc_prefix_reuse_percentage_nt_gz(self):
        score, error_msg = get_prefix_reuse_percentage("tests/test_files/test_nt_1.nt.gz", NT, GZ)
        self.assertEqual(score, None)
        self.assertEqual(error_msg, "Not calculated because there is no prefix defined.")

    def test_calc_prefix_reuse_percentage_ttl_gz(self):
        score, error_msg = get_prefix_reuse_percentage("tests/test_files/test_ttl_1.ttl.gz", TURTLE, GZ)
        self.assertEqual(score, 100.0)
        self.assertEqual(error_msg, None)

if __name__ == "__main__":
    unittest.main()