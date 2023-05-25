import unittest
from doctor.doctor import get_compression_mode
from tests.consts import NT_1, NT_1_GZ, TTL_1, TTL_1_GZ
from shexer.consts import GZ

class TestGetCompressionMode(unittest.TestCase):

    def test_nt(self):
        compression_mode = get_compression_mode(NT_1)
        self.assertEqual(compression_mode, None)

    def test_nt_gz(self):
        compression_mode = get_compression_mode(NT_1_GZ)
        self.assertEqual(compression_mode, GZ)

    def test_ttl(self):
        compression_mode = get_compression_mode(TTL_1)
        self.assertEqual(compression_mode, None)

    def test_ttl_gz(self):
        compression_mode = get_compression_mode(TTL_1_GZ)
        self.assertEqual(compression_mode, GZ)

if __name__ == "__main__":
    unittest.main()