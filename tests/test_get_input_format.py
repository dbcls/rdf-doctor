import unittest
from doctor.doctor import get_input_format
from shexer.consts import NT, TURTLE, GZ

class TestGetInputFormat(unittest.TestCase):

    def test_get_input_format_nt(self):
        input_format = get_input_format("tests/test_files/test_nt_1.nt", None)
        self.assertEqual(input_format, NT)

    def test_get_input_format_ttl(self):
        input_format = get_input_format("tests/test_files/test_ttl_1.ttl", None)
        self.assertEqual(input_format, TURTLE)

    def test_get_input_format_nt_gz(self):
        input_format = get_input_format("tests/test_files/test_nt_1.nt.gz", GZ)
        self.assertEqual(input_format, NT)

    def test_get_input_format_ttl_gz(self):
        input_format = get_input_format("tests/test_files/test_ttl_1.ttl.gz", GZ)
        self.assertEqual(input_format, TURTLE)

if __name__ == "__main__":
    unittest.main()