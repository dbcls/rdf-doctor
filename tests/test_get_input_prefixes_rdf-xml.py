import unittest
from doctor.doctor import get_input_prefixes_rdf_xml
from tests.consts import OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_2, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP
from shexer.consts import GZ, ZIP

class TestGetInputPrefixesRdfXml(unittest.TestCase):

    def test_owl(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([OWL_1], None)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], ['foaf:', 'http://xmlns.com/foaf/0.1/']])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_rdf(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([RDF_1], None)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], ['foaf:', 'http://xmlns.com/foaf/0.1/']])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_rdf_2(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([RDF_2], None)
        print(input_prefixes)
        print(duplicated_prefixes_list)
        print(duplicated_prefixes_dict)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], ['foaf:', 'http://xmlns.com/foaf/0.1#']])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_rdf_multi(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([RDF_1, RDF_2], None)
        print(input_prefixes)
        print(duplicated_prefixes_list)
        print(duplicated_prefixes_dict)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], \
                                            ['foaf:', 'http://xmlns.com/foaf/0.1/'], \
                                            ['foaf:', 'http://xmlns.com/foaf/0.1#']])
        self.assertEqual(duplicated_prefixes_list, ['foaf:\thttp://xmlns.com/foaf/0.1/\n', 'foaf:\thttp://xmlns.com/foaf/0.1#\n'])
        self.assertEqual(duplicated_prefixes_dict, {'foaf:': ['http://xmlns.com/foaf/0.1/', 'http://xmlns.com/foaf/0.1#']})

    def test_xml(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([XML_1], None)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], ['foaf:', 'http://xmlns.com/foaf/0.1/']])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_owl_gz(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([OWL_1_GZ], GZ)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], ['foaf:', 'http://xmlns.com/foaf/0.1/']])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_rdf_gz(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([RDF_1_GZ], GZ)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], ['foaf:', 'http://xmlns.com/foaf/0.1/']])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_xml_gz(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([XML_1_GZ], GZ)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], ['foaf:', 'http://xmlns.com/foaf/0.1/']])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_owl_zip(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([OWL_1_ZIP], ZIP)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], ['foaf:', 'http://xmlns.com/foaf/0.1/']])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_rdf_zip(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([RDF_1_ZIP], ZIP)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], ['foaf:', 'http://xmlns.com/foaf/0.1/']])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})

    def test_xml_zip(self):
        input_prefixes, duplicated_prefixes_list, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([XML_1_ZIP], ZIP)
        self.assertEqual(input_prefixes, [['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'], ['foaf:', 'http://xmlns.com/foaf/0.1/']])
        self.assertEqual(duplicated_prefixes_list, [])
        self.assertEqual(duplicated_prefixes_dict, {})


if __name__ == "__main__":
    unittest.main()