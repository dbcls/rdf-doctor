import unittest
from doctor.doctor import get_default_namespaces_dict

class TestGetDefaultNamespacesDict(unittest.TestCase):

    def test_get_default_namespaces_dict(self):
        namespaces_dict = get_default_namespaces_dict()
        self.assertEqual(namespaces_dict, {
                                            "http://www.w3.org/2002/07/owl#": "owl",
                                            "http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                                            "http://www.w3.org/2000/01/rdf-schema#": "rdfs",
                                            "http://www.w3.org/2001/XMLSchema#": "xsd",
                                            "http://www.w3.org/XML/1998/namespace": "xml",
                                            "http://www.w3.org/2004/02/skos/core#": "skos",
                                            "http://purl.obolibrary.org/obo/": "obo",
                                            })

if __name__ == "__main__":
    unittest.main()