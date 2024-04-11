import unittest
from doctor.doctor import is_target_file
from doctor.consts import FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP
from shexer.consts import GZ, ZIP
from tests.consts import TTL_1, TTL_2, TTL_3, TTL_1_GZ, TTL_1_ZIP, NT_1, NT_2, NT_3, NT_1_GZ, NT_1_ZIP, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP

class TestIsTargetFile(unittest.TestCase):

    def test_ttl_true(self):
        result = is_target_file([[TTL_1, TTL_2, TTL_3], None, "turtle"], [FILE_TYPE_TTL])
        self.assertEqual(result, True)

    def test_nt_true(self):
        result = is_target_file([[NT_1, NT_2, NT_3], None, "nt"], [FILE_TYPE_NT])
        self.assertEqual(result, True)

    def test_owl_true(self):
        result = is_target_file([[OWL_1], None, "xml"], [FILE_TYPE_RDF_XML])
        self.assertEqual(result, True)

    def test_rdf_true(self):
        result = is_target_file([[RDF_1], None, "xml"], [FILE_TYPE_RDF_XML])
        self.assertEqual(result, True)

    def test_xml_true(self):
        result = is_target_file([[XML_1], None, "xml"], [FILE_TYPE_RDF_XML])
        self.assertEqual(result, True)

    def test_ttl_gz_true(self):
        result = is_target_file([[TTL_1_GZ], GZ, "turtle"], [FILE_TYPE_TTL_GZ])
        self.assertEqual(result, True)

    def test_nt_gz_true(self):
        result = is_target_file([[NT_1_GZ], GZ, "nt"], [FILE_TYPE_NT_GZ])
        self.assertEqual(result, True)

    def test_owl_gz_true(self):
        result = is_target_file([[OWL_1_GZ], GZ, "xml"], [FILE_TYPE_RDF_XML_GZ])
        self.assertEqual(result, True)

    def test_rdf_gz_true(self):
        result = is_target_file([[RDF_1_GZ], GZ, "xml"], [FILE_TYPE_RDF_XML_GZ])
        self.assertEqual(result, True)

    def test_xml_gz_true(self):
        result = is_target_file([[XML_1_GZ], GZ, "xml"], [FILE_TYPE_RDF_XML_GZ])
        self.assertEqual(result, True)

    def test_ttl_zip_true(self):
        result = is_target_file([[TTL_1_ZIP], ZIP, "turtle"], [FILE_TYPE_TTL_ZIP])
        self.assertEqual(result, True)

    def test_nt_zip_true(self):
        result = is_target_file([[NT_1_ZIP], ZIP, "nt"], [FILE_TYPE_NT_ZIP])
        self.assertEqual(result, True)

    def test_owl_zip_true(self):
        result = is_target_file([[OWL_1_ZIP], ZIP, "xml"], [FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(result, True)

    def test_rdf_zip_true(self):
        result = is_target_file([[RDF_1_ZIP], ZIP, "xml"], [FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(result, True)

    def test_xml_zip_true(self):
        result = is_target_file([[XML_1_ZIP], ZIP, "xml"], [FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(result, True)

    def test_ttl_false(self):
        result = is_target_file([[TTL_1, TTL_2, TTL_3], None, "turtle"], [FILE_TYPE_NT])
        self.assertEqual(result, False)

    def test_nt_false(self):
        result = is_target_file([[NT_1, NT_2, NT_3], None, "nt"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_owl_false(self):
        result = is_target_file([[OWL_1], None, "xml"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_rdf_false(self):
        result = is_target_file([[RDF_1], None, "xml"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_xml_false(self):
        result = is_target_file([[XML_1], None, "xml"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_ttl_gz_false(self):
        result = is_target_file([[TTL_1_GZ], GZ, "turtle"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_nt_gz_false(self):
        result = is_target_file([[NT_1_GZ], GZ, "nt"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_owl_gz_false(self):
        result = is_target_file([[OWL_1_GZ], GZ, "xml"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_rdf_gz_false(self):
        result = is_target_file([[RDF_1_GZ], GZ, "xml"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_xml_gz_false(self):
        result = is_target_file([[XML_1_GZ], GZ, "xml"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_ttl_zip_false(self):
        result = is_target_file([[TTL_1_ZIP], ZIP, "turtle"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_nt_zip_false(self):
        result = is_target_file([[NT_1_ZIP], ZIP, "nt"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_owl_zip_false(self):
        result = is_target_file([[OWL_1_ZIP], ZIP, "xml"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_rdf_zip_false(self):
        result = is_target_file([[RDF_1_ZIP], ZIP, "xml"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

    def test_xml_zip_false(self):
        result = is_target_file([[XML_1_ZIP], ZIP, "xml"], [FILE_TYPE_TTL])
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()