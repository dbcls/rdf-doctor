import unittest
from doctor.doctor import get_extension
from tests.consts import TTL_1, TTL_1_GZ, TTL_1_ZIP, NT_1, NT_1_GZ, NT_1_ZIP, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP

class TestGetExtension(unittest.TestCase):

    def test_ttl(self):
        extension = get_extension(TTL_1)
        self.assertEqual(extension, ".ttl")

    def test_ttl_gz(self):
        extension = get_extension(TTL_1_GZ)
        self.assertEqual(extension, ".gz")

    def test_ttl_zip(self):
        extension = get_extension(TTL_1_ZIP)
        self.assertEqual(extension, ".zip")

    def test_nt(self):
        extension = get_extension(NT_1)
        self.assertEqual(extension, ".nt")

    def test_nt_gz(self):
        extension = get_extension(NT_1_GZ)
        self.assertEqual(extension, ".gz")

    def test_nt_zip(self):
        extension = get_extension(NT_1_ZIP)
        self.assertEqual(extension, ".zip")

    def test_owl(self):
        extension = get_extension(OWL_1)
        self.assertEqual(extension, ".owl")

    def test_owl_gz(self):
        extension = get_extension(OWL_1_GZ)
        self.assertEqual(extension, ".gz")

    def test_owl_zip(self):
        extension = get_extension(OWL_1_ZIP)
        self.assertEqual(extension, ".zip")

    def test_rdf(self):
        extension = get_extension(RDF_1)
        self.assertEqual(extension, ".rdf")

    def test_rdf_gz(self):
        extension = get_extension(RDF_1_GZ)
        self.assertEqual(extension, ".gz")

    def test_rdf_zip(self):
        extension = get_extension(RDF_1_ZIP)
        self.assertEqual(extension, ".zip")

    def test_xml(self):
        extension = get_extension(XML_1)
        self.assertEqual(extension, ".xml")

    def test_xml_gz(self):
        extension = get_extension(XML_1_GZ)
        self.assertEqual(extension, ".gz")

    def test_xml_zip(self):
        extension = get_extension(XML_1_ZIP)
        self.assertEqual(extension, ".zip")


if __name__ == "__main__":
    unittest.main()