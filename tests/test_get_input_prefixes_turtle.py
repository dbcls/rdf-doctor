import unittest
from doctor.doctor import get_input_prefixes_turtle
from tests.consts import TTL_1, TTL_2, TTL_3, TTL_1_GZ, TTL_2_GZ, TTL_3_GZ, TTL_1_ZIP, TTL_2_ZIP, TTL_3_ZIP
from shexer.consts import GZ, ZIP

class TestGetInputPrefixesTurtle(unittest.TestCase):

    def test_ttl_1(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_1], None)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["rdfs:", "http://www.w3.org/2000/01/rdf-schema#"], \
                                            ["ex:", "http://example.org/"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1/"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"]])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_ttl_2(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_2], None)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["ex:", "http://example.org#"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1#"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"]])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_ttl_3(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_3], None)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["oboc:", "http://purl.obolibrary.org/obo/CHEBI_"], \
                                            ["chebi:", "http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"], \
                                            ["pobo:", "http://purl.obolibrary.org/obo/"]])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_ttl_gz(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_1_GZ], GZ)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["rdfs:", "http://www.w3.org/2000/01/rdf-schema#"], \
                                            ["ex:", "http://example.org/"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1/"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"]])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_ttl_zip(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_1_ZIP], ZIP)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["rdfs:", "http://www.w3.org/2000/01/rdf-schema#"], \
                                            ["ex:", "http://example.org/"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1/"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"]])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_ttl_multi(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_1, TTL_2, TTL_3], None)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["rdfs:", "http://www.w3.org/2000/01/rdf-schema#"], \
                                            ["ex:", "http://example.org/"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1/"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"], \
                                            ["ex:", "http://example.org#"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1#"], \
                                            ["oboc:", "http://purl.obolibrary.org/obo/CHEBI_"], \
                                            ["chebi:", "http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A"], \
                                            ["pobo:", "http://purl.obolibrary.org/obo/"]])
        self.assertEqual(duplicated_prefixes_list, ["ex:\thttp://example.org/\n", \
                                                "ex:\thttp://example.org#\n", \
                                                "foaf:\thttp://xmlns.com/foaf/0.1/\n", \
                                                "foaf:\thttp://xmlns.com/foaf/0.1#\n"])
        self.assertEqual(duplicated_prefixes_dict, {'ex:': ['http://example.org/', 'http://example.org#'], 'foaf:': ['http://xmlns.com/foaf/0.1/', 'http://xmlns.com/foaf/0.1#']})

    def test_ttl_gz_multi(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], GZ)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["rdfs:", "http://www.w3.org/2000/01/rdf-schema#"], \
                                            ["ex:", "http://example.org/"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1/"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"], \
                                            ["ex:", "http://example.org#"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1#"], \
                                            ["oboc:", "http://purl.obolibrary.org/obo/CHEBI_"], \
                                            ["chebi:", "http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A"], \
                                            ["pobo:", "http://purl.obolibrary.org/obo/"]])
        self.assertEqual(duplicated_prefixes_list, ["ex:\thttp://example.org/\n", \
                                                "ex:\thttp://example.org#\n", \
                                                "foaf:\thttp://xmlns.com/foaf/0.1/\n", \
                                                "foaf:\thttp://xmlns.com/foaf/0.1#\n"])
        self.assertEqual(duplicated_prefixes_dict, {'ex:': ['http://example.org/', 'http://example.org#'], 'foaf:': ['http://xmlns.com/foaf/0.1/', 'http://xmlns.com/foaf/0.1#']})

    def test_ttl_zip_multi(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_1_ZIP, TTL_2_ZIP, TTL_3_ZIP], ZIP)
        self.assertEqual(input_prefixes, [["rdf:", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"], \
                                            ["rdfs:", "http://www.w3.org/2000/01/rdf-schema#"], \
                                            ["ex:", "http://example.org/"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1/"], \
                                            ["xsd:", "http://www.w3.org/2001/XMLSchema#"], \
                                            ["ex:", "http://example.org#"], \
                                            ["foaf:", "http://xmlns.com/foaf/0.1#"], \
                                            ["oboc:", "http://purl.obolibrary.org/obo/CHEBI_"], \
                                            ["chebi:", "http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A"], \
                                            ["pobo:", "http://purl.obolibrary.org/obo/"]])
        self.assertEqual(duplicated_prefixes_list, ["ex:\thttp://example.org/\n", \
                                                "ex:\thttp://example.org#\n", \
                                                "foaf:\thttp://xmlns.com/foaf/0.1/\n", \
                                                "foaf:\thttp://xmlns.com/foaf/0.1#\n"])
        self.assertEqual(duplicated_prefixes_dict, {'ex:': ['http://example.org/', 'http://example.org#'], 'foaf:': ['http://xmlns.com/foaf/0.1/', 'http://xmlns.com/foaf/0.1#']})

if __name__ == "__main__":
    unittest.main()