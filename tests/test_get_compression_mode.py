import unittest
from doctor.doctor import get_compression_mode
from shexer.consts import GZ
import argparse

class TestGetCompressionMode(unittest.TestCase):

    def test_get_compression_mode_nt(self):
        compression_mode = get_compression_mode("tests/test_files/test_nt_1.nt")
        self.assertEqual(compression_mode, None)

    def test_get_compression_mode_nt_gz(self):
        compression_mode = get_compression_mode("tests/test_files/test_nt_1.nt.gz")
        self.assertEqual(compression_mode, GZ)

    def test_get_compression_mode_ttl(self):
        compression_mode = get_compression_mode("tests/test_files/test_ttl_1.ttl")
        self.assertEqual(compression_mode, None)

    def test_get_compression_mode_ttl_gz(self):
        compression_mode = get_compression_mode("tests/test_files/test_ttl_1.ttl.gz")
        self.assertEqual(compression_mode, GZ)

if __name__ == "__main__":
    unittest.main()