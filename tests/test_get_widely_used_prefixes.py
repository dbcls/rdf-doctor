import unittest
from doctor.doctor import get_widely_used_prefixes
from tests.consts import PREFIXES_FILE_PATH
from pathlib import Path

class TestGetWidelyUsedPrefixes(unittest.TestCase):

    def test_get_widely_used_prefixes(self):
        widely_used_prefixes = get_widely_used_prefixes(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        self.assertEqual(widely_used_prefixes, [['chebi:', 'http://purl.obolibrary.org/obo/CHEBI_'], \
                                            ['ex:', 'http://example.org/'], \
                                            ['ex2:', 'http://example.org/'], \
                                            ['foaf:', 'http://xmlns.com/foaf/0.1/'], \
                                            ['obo:', 'http://purl.obolibrary.org/obo/'], \
                                            ['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], \
                                            ['rdfs:', 'http://www.w3.org/2000/01/rdf-schema#'], \
                                            ['uo:', 'http://purl.obolibrary.org/obo/'], \
                                            ['xsd:', 'http://www.w3.org/2001/XMLSchema#']])

if __name__ == "__main__":
    unittest.main()