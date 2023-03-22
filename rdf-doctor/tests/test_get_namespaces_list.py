import unittest
from doctor import get_namespaces_list
import rdflib
from shexer.consts import NT, TURTLE, GZ

class TestGetNameSpacesList(unittest.TestCase):

    def test_get_namespaces_list_nt(self):
        namespaces_list = get_namespaces_list("tests/test_files/test_nt_1.nt", NT, None)
        self.assertEqual(namespaces_list, [])

    def test_get_namespaces_list_ttl(self):
        namespaces_list = get_namespaces_list("tests/test_files/test_ttl_1.ttl", TURTLE, None)
        self.assertEqual(namespaces_list, [('ex', rdflib.term.URIRef('http://example.org/')), ('foaf', rdflib.term.URIRef('http://xmlns.com/foaf/0.1/'))])

    def test_get_namespaces_list_nt_gz(self):
        namespaces_list = get_namespaces_list("tests/test_files/test_nt_1.nt.gz", NT, GZ)
        self.assertEqual(namespaces_list, [])

    def test_get_namespaces_list_ttl_gz(self):
        namespaces_list = get_namespaces_list("tests/test_files/test_ttl_1.ttl.gz", TURTLE, GZ)
        self.assertEqual(namespaces_list, [('ex', rdflib.term.URIRef('http://example.org/')), ('foaf', rdflib.term.URIRef('http://xmlns.com/foaf/0.1/'))])

if __name__ == "__main__":
    unittest.main()