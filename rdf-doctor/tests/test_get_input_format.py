import unittest
from doctor import get_input_format

class TestGetInputFormat(unittest.TestCase):

    def test_get_input_format_nt(self):
        input_format = get_input_format("rdf-doctor/tests/test_files/test_nt_1.nt")
        self.assertEqual(input_format, "nt")

    def test_get_input_format_ttl(self):
        input_format = get_input_format("rdf-doctor/tests/test_files/test_ttl_1.ttl")
        self.assertEqual(input_format, "turtle")

if __name__ == "__main__":
    unittest.main()