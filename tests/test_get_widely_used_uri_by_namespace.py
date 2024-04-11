import unittest
from pathlib import Path
from doctor.doctor import get_widely_used_prefixes_dict, get_widely_used_uri_by_namespace
from tests.consts import PREFIXES_FILE_PATH

class TestGetWidelyUsedUriByNamespace(unittest.TestCase):

    def test_ex(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_uri = get_widely_used_uri_by_namespace("ex:", widely_used_prefixes_dict)
        self.assertEqual(widely_used_uri, "http://example.org/")

    def test_ex2(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_uri = get_widely_used_uri_by_namespace("ex2:", widely_used_prefixes_dict)
        self.assertEqual(widely_used_uri, "http://example.org/")

    def test_foaf(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_uri = get_widely_used_uri_by_namespace("foaf:", widely_used_prefixes_dict)
        self.assertEqual(widely_used_uri, "http://xmlns.com/foaf/0.1/")

    def test_obo(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_uri = get_widely_used_uri_by_namespace("obo:", widely_used_prefixes_dict)
        self.assertEqual(widely_used_uri, "http://purl.obolibrary.org/obo/")


if __name__ == "__main__":
    unittest.main()