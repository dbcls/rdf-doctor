import unittest
from doctor import get_namespaces_list
import rdflib

class TestGetNameSpacesList(unittest.TestCase):

    def test_get_namespaces_list_nt(self):
        namespaces_list = get_namespaces_list("rdf-doctor/tests/test_files/test_nt_1.nt", "nt")
        self.assertEqual(namespaces_list, [('owl', rdflib.term.URIRef('http://www.w3.org/2002/07/owl#')), ('rdf', rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#')), ('rdfs', rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#')), ('xsd', rdflib.term.URIRef('http://www.w3.org/2001/XMLSchema#')), ('xml', rdflib.term.URIRef('http://www.w3.org/XML/1998/namespace'))])

    def test_get_namespaces_list_ttl(self):
        namespaces_list = get_namespaces_list("rdf-doctor/tests/test_files/test_ttl_1.ttl", "turtle")
        self.assertEqual(namespaces_list, [('owl', rdflib.term.URIRef('http://www.w3.org/2002/07/owl#')), ('rdf', rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#')), ('rdfs', rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#')), ('xsd', rdflib.term.URIRef('http://www.w3.org/2001/XMLSchema#')), ('xml', rdflib.term.URIRef('http://www.w3.org/XML/1998/namespace')), ('ex', rdflib.term.URIRef('http://example.org/')), ('foaf', rdflib.term.URIRef('http://xmlns.com/foaf/0.1/'))])

if __name__ == "__main__":
    unittest.main()