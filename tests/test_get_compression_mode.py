import unittest
from doctor.doctor import get_compression_mode
from tests.consts import NT_1, NT_1_GZ, NT_1_ZIP, TTL_1, TTL_1_GZ, TTL_1_ZIP, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP
from shexer.consts import GZ, ZIP

class TestGetCompressionMode(unittest.TestCase):

    def test_nt(self):
        compression_mode = get_compression_mode(NT_1)
        self.assertEqual(compression_mode, None)

    def test_nt_gz(self):
        compression_mode = get_compression_mode(NT_1_GZ)
        self.assertEqual(compression_mode, GZ)

    def test_nt_zip(self):
        compression_mode = get_compression_mode(NT_1_ZIP)
        self.assertEqual(compression_mode, ZIP)

    def test_ttl(self):
        compression_mode = get_compression_mode(TTL_1)
        self.assertEqual(compression_mode, None)

    def test_ttl_gz(self):
        compression_mode = get_compression_mode(TTL_1_GZ)
        self.assertEqual(compression_mode, GZ)

    def test_ttl_zip(self):
        compression_mode = get_compression_mode(TTL_1_ZIP)
        self.assertEqual(compression_mode, ZIP)

    def test_owl(self):
        compression_mode = get_compression_mode(OWL_1)
        self.assertEqual(compression_mode, None)

    def test_owl_gz(self):
        compression_mode = get_compression_mode(OWL_1_GZ)
        self.assertEqual(compression_mode, GZ)

    def test_owl_zip(self):
        compression_mode = get_compression_mode(OWL_1_ZIP)
        self.assertEqual(compression_mode, ZIP)

    def test_rdf(self):
        compression_mode = get_compression_mode(RDF_1)
        self.assertEqual(compression_mode, None)

    def test_rdf_gz(self):
        compression_mode = get_compression_mode(RDF_1_GZ)
        self.assertEqual(compression_mode, GZ)

    def test_rdf_zip(self):
        compression_mode = get_compression_mode(RDF_1_ZIP)
        self.assertEqual(compression_mode, ZIP)

    def test_xml(self):
        compression_mode = get_compression_mode(XML_1)
        self.assertEqual(compression_mode, None)

    def test_xml_gz(self):
        compression_mode = get_compression_mode(XML_1_GZ)
        self.assertEqual(compression_mode, GZ)

    def test_xml_zip(self):
        compression_mode = get_compression_mode(XML_1_ZIP)
        self.assertEqual(compression_mode, ZIP)
if __name__ == "__main__":
    unittest.main()