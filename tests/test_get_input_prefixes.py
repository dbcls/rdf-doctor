import unittest
from doctor.doctor import get_input_prefixes
from shexer.consts import NT, TURTLE, GZ

class TestGetInputPrefixes(unittest.TestCase):

    def test_get_input_prefixes_nt(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_nt_1.nt", None)
        self.assertEqual(input_prefixes, [])

    def test_get_input_prefixes_ttl_1(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_ttl_1.ttl", None)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["rdfs:", "http://www.w3.org/2000/01/rdf-schema#"], \
                                            ["ex:", "http://example.org/"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1/"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"]])

    def test_get_input_prefixes_ttl_2(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_ttl_2.ttl", None)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["ex:", "http://example.org#"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1#"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"]])

    def test_get_input_prefixes_ttl_3(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_ttl_3.ttl", None)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["oboc:", "http://purl.obolibrary.org/obo/CHEBI_"], \
                                            ["chebi:", "http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"], \
                                            ["pobo:", "http://purl.obolibrary.org/obo/"]])

    def test_get_input_prefixes_nt_gz(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_nt_1.nt.gz", GZ)
        self.assertEqual(input_prefixes, [])

    def test_get_input_prefixes_ttl_gz(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_ttl_1.ttl.gz", GZ)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["rdfs:", "http://www.w3.org/2000/01/rdf-schema#"], \
                                            ["ex:", "http://example.org/"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1/"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"]])

if __name__ == "__main__":
    unittest.main()