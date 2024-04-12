import unittest
from doctor.doctor import get_input_format
from tests.consts import TTL_1, TTL_1_GZ, TTL_1_ZIP, NT_1, NT_1_GZ, NT_1_ZIP, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP
from shexer.consts import NT, TURTLE, RDF_XML, GZ, ZIP

class TestGetInputFormat(unittest.TestCase):

    def test_nt(self):
        input_format = get_input_format(NT_1, None)
        self.assertEqual(input_format, NT)

    def test_ttl(self):
        input_format = get_input_format(TTL_1, None)
        self.assertEqual(input_format, TURTLE)

    def test_owl(self):
        input_format = get_input_format(OWL_1, None)
        self.assertEqual(input_format, RDF_XML)

    def test_rdf(self):
        input_format = get_input_format(RDF_1, None)
        self.assertEqual(input_format, RDF_XML)

    def test_xml(self):
        input_format = get_input_format(XML_1, None)
        self.assertEqual(input_format, RDF_XML)

    def test_nt_gz(self):
        input_format = get_input_format(NT_1_GZ, GZ)
        self.assertEqual(input_format, NT)

    def test_ttl_gz(self):
        input_format = get_input_format(TTL_1_GZ, GZ)
        self.assertEqual(input_format, TURTLE)

    def test_owl_gz(self):
        input_format = get_input_format(OWL_1_GZ, GZ)
        self.assertEqual(input_format, RDF_XML)

    def test_rdf_gz(self):
        input_format = get_input_format(RDF_1_GZ, GZ)
        self.assertEqual(input_format, RDF_XML)

    def test_xml_gz(self):
        input_format = get_input_format(XML_1_GZ, GZ)
        self.assertEqual(input_format, RDF_XML)

    def test_owl_zip(self):
        input_format = get_input_format(OWL_1_ZIP, ZIP)
        self.assertEqual(input_format, RDF_XML)

    def test_rdf_zip(self):
        input_format = get_input_format(RDF_1_ZIP, ZIP)
        self.assertEqual(input_format, RDF_XML)

    def test_xml_zip(self):
        input_format = get_input_format(XML_1_ZIP, ZIP)
        self.assertEqual(input_format, RDF_XML)

if __name__ == "__main__":
    unittest.main()