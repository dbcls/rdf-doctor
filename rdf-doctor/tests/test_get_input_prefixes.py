import unittest
from doctor import get_input_prefixes
import rdflib
from shexer.consts import NT, TURTLE, GZ

class TestGetNameSpacesList(unittest.TestCase):

    def test_get_input_prefixes_nt(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_nt_1.nt", NT, None)
        self.assertEqual(input_prefixes, [])

    def test_get_input_prefixes_ttl(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_ttl_1.ttl", TURTLE, None)
        self.assertEqual(input_prefixes, [('ex', rdflib.term.URIRef('http://example.org/')), \
                                            ('foaf', rdflib.term.URIRef('http://xmlns.com/foaf/0.1/'))])

    def test_get_input_prefixes_nt_gz(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_nt_1.nt.gz", NT, GZ)
        self.assertEqual(input_prefixes, [])

    def test_get_input_prefixesttl_gz(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_ttl_1.ttl.gz", TURTLE, GZ)
        self.assertEqual(input_prefixes, [('ex', rdflib.term.URIRef('http://example.org/')), \
                                            ('foaf', rdflib.term.URIRef('http://xmlns.com/foaf/0.1/'))])

if __name__ == "__main__":
    unittest.main()