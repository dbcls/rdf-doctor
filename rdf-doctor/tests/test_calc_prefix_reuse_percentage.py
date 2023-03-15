import unittest
from doctor import calc_prefix_reuse_percentage

class TestCalcPrefixReusePercentage(unittest.TestCase):

    def test_calc_prefix_reuse_percentage_nt(self):
        score = calc_prefix_reuse_percentage("rdf-doctor/tests/test_files/test_ttl_1.ttl", "turtle")
        self.assertEqual(score, 85.71)

if __name__ == "__main__":
    unittest.main()