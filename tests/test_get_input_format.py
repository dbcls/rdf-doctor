import unittest
from doctor.doctor import get_input_format
from tests.consts import NT_1, NT_1_GZ, TTL_1, TTL_1_GZ
from shexer.consts import NT, TURTLE, GZ

class TestGetInputFormat(unittest.TestCase):

    def test_nt(self):
        input_format = get_input_format(NT_1, None)
        self.assertEqual(input_format, NT)

    def test_ttl(self):
        input_format = get_input_format(TTL_1, None)
        self.assertEqual(input_format, TURTLE)

    def test_nt_gz(self):
        input_format = get_input_format(NT_1_GZ, GZ)
        self.assertEqual(input_format, NT)

    def test_ttl_gz(self):
        input_format = get_input_format(TTL_1_GZ, GZ)
        self.assertEqual(input_format, TURTLE)

if __name__ == "__main__":
    unittest.main()