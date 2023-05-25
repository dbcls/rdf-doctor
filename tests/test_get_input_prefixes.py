import unittest
from doctor.doctor import get_input_prefixes
from tests.consts import NT_1, NT_1_GZ, TTL_1, TTL_2, TTL_3, TTL_1_GZ
from shexer.consts import GZ

class TestGetInputPrefixes(unittest.TestCase):

    def test_nt(self):
        input_prefixes = get_input_prefixes(NT_1, None)
        self.assertEqual(input_prefixes, [])

    def test_ttl_1(self):
        input_prefixes = get_input_prefixes(TTL_1, None)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["rdfs:", "http://www.w3.org/2000/01/rdf-schema#"], \
                                            ["ex:", "http://example.org/"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1/"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"]])

    def test_ttl_2(self):
        input_prefixes = get_input_prefixes(TTL_2, None)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["ex:", "http://example.org#"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1#"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"]])

    def test_ttl_3(self):
        input_prefixes = get_input_prefixes(TTL_3, None)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["oboc:", "http://purl.obolibrary.org/obo/CHEBI_"], \
                                            ["chebi:", "http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"], \
                                            ["pobo:", "http://purl.obolibrary.org/obo/"]])

    def test_nt_gz(self):
        input_prefixes = get_input_prefixes(NT_1_GZ, GZ)
        self.assertEqual(input_prefixes, [])

    def test_ttl_gz(self):
        input_prefixes = get_input_prefixes(TTL_1_GZ, GZ)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["rdfs:", "http://www.w3.org/2000/01/rdf-schema#"], \
                                            ["ex:", "http://example.org/"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1/"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"]])

if __name__ == "__main__":
    unittest.main()