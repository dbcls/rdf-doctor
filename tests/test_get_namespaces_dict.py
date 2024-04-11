import unittest
from pathlib import Path
from doctor.doctor import get_input_prefixes_turtle, get_input_prefixes_rdf_xml, get_widely_used_prefixes_dict, get_namespaces_dict
from shexer.consts import GZ, ZIP
from tests.consts import PREFIXES_FILE_PATH, TTL_1, TTL_2, TTL_3, TTL_1_GZ, TTL_2_GZ, TTL_3_GZ, TTL_1_ZIP, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP


class TestGetNamespacesDict(unittest.TestCase):

    def test_ttl(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_1, TTL_2, TTL_3], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://www.w3.org/2000/01/rdf-schema#': 'rdfs', \
                                            'http://example.org/': 'ex', \
                                            'http://xmlns.com/foaf/0.1/': 'foaf', \
                                            'http://www.w3.org/2001/XMLSchema#': 'xsd', \
                                            'http://example.org#': 'ns1', \
                                            'http://xmlns.com/foaf/0.1#': 'ns2', \
                                            'http://purl.obolibrary.org/obo/CHEBI_': 'oboc', \
                                            'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A': 'chebi', \
                                            'http://purl.obolibrary.org/obo/': 'pobo'})

    def test_ttl_gz(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://www.w3.org/2000/01/rdf-schema#': 'rdfs', \
                                            'http://example.org/': 'ex', \
                                            'http://xmlns.com/foaf/0.1/': 'foaf', \
                                            'http://www.w3.org/2001/XMLSchema#': 'xsd', \
                                            'http://example.org#': 'ns1', \
                                            'http://xmlns.com/foaf/0.1#': 'ns2', \
                                            'http://purl.obolibrary.org/obo/CHEBI_': 'oboc', \
                                            'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A': 'chebi', \
                                            'http://purl.obolibrary.org/obo/': 'pobo'})

    def test_ttl_zip(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_turtle([TTL_1_ZIP], ZIP)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        print(namespaces_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://www.w3.org/2000/01/rdf-schema#': 'rdfs', \
                                            'http://example.org/': 'ex', \
                                            'http://xmlns.com/foaf/0.1/': 'foaf', \
                                            'http://www.w3.org/2001/XMLSchema#': 'xsd'})

    def test_owl(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([OWL_1], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/2001/XMLSchema#': 'xsd', \
                                            'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://www.w3.org/2000/01/rdf-schema#': 'rdfs', \
                                            'http://www.w3.org/2002/07/owl#': 'owl', \
                                            'file://www.ibm.com/WSRR/Transport#': 'ns_transport', \
                                            'http://www.ibm.com/xmlns/prod/serviceregistry/6/1/model#': 'wsrr'})

    def test_owl_gz(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([OWL_1_GZ], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/2001/XMLSchema#': 'xsd', \
                                            'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://www.w3.org/2000/01/rdf-schema#': 'rdfs', \
                                            'http://www.w3.org/2002/07/owl#': 'owl', \
                                            'file://www.ibm.com/WSRR/Transport#': 'ns_transport', \
                                            'http://www.ibm.com/xmlns/prod/serviceregistry/6/1/model#': 'wsrr'})

    def test_owl_zip(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([OWL_1_ZIP], ZIP)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/2001/XMLSchema#': 'xsd', \
                                            'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://www.w3.org/2000/01/rdf-schema#': 'rdfs', \
                                            'http://www.w3.org/2002/07/owl#': 'owl', \
                                            'file://www.ibm.com/WSRR/Transport#': 'ns_transport', \
                                            'http://www.ibm.com/xmlns/prod/serviceregistry/6/1/model#': 'wsrr'})

    def test_rdf(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([RDF_1], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://xmlns.com/foaf/0.1/': 'foaf'})

    def test_rdf_gz(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([RDF_1_GZ], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://xmlns.com/foaf/0.1/': 'foaf'})

    def test_rdf_zip(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([RDF_1_ZIP], ZIP)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://xmlns.com/foaf/0.1/': 'foaf'})

    def test_xml(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([XML_1], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://xmlns.com/foaf/0.1/': 'foaf'})

    def test_xml_gz(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([XML_1_GZ], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://xmlns.com/foaf/0.1/': 'foaf'})

    def test_xml_zip(self):
        input_prefixes, _, duplicated_prefixes_dict = get_input_prefixes_rdf_xml([XML_1_ZIP], ZIP)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        namespaces_dict = get_namespaces_dict(input_prefixes, duplicated_prefixes_dict, widely_used_prefixes_dict)
        self.assertEqual(namespaces_dict, {'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', \
                                            'http://xmlns.com/foaf/0.1/': 'foaf'})


if __name__ == "__main__":
    unittest.main()