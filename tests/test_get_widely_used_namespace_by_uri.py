import unittest
from pathlib import Path
from doctor.doctor import get_widely_used_prefixes_dict, get_widely_used_namespace_by_uri
from tests.consts import PREFIXES_FILE_PATH

class TestGetWidelyUsedNamespaceByUri(unittest.TestCase):

    def test_ex(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace = get_widely_used_namespace_by_uri("http://example.org/", widely_used_prefixes_dict)
        self.assertEqual(widely_used_namespace, ['ex:', 'ex2:'])

    def test_foaf(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace = get_widely_used_namespace_by_uri("http://xmlns.com/foaf/0.1/", widely_used_prefixes_dict)
        self.assertEqual(widely_used_namespace, ['foaf:'])

    def test_obo(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace = get_widely_used_namespace_by_uri("http://purl.obolibrary.org/obo/", widely_used_prefixes_dict)
        self.assertEqual(widely_used_namespace, ['obo:', 'uo:'])


if __name__ == "__main__":
    unittest.main()