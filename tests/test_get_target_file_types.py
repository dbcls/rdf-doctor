import unittest
import sys
import io
from doctor.doctor import get_target_file_types
from doctor.consts import FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP

FILE_TYPE_ALL = "all"

class TestGetTargetFileTypes(unittest.TestCase):

    def test_ttl(self):
        target_file_types = get_target_file_types([FILE_TYPE_TTL])
        self.assertEqual(target_file_types, [FILE_TYPE_TTL])

    def test_nt(self):
        target_file_types = get_target_file_types([FILE_TYPE_NT])
        self.assertEqual(target_file_types, [FILE_TYPE_NT])

    def test_rdf_xml(self):
        target_file_types = get_target_file_types([FILE_TYPE_RDF_XML])
        self.assertEqual(target_file_types, [FILE_TYPE_RDF_XML])

    def test_ttl_gz(self):
        target_file_types = get_target_file_types([FILE_TYPE_TTL_GZ])
        self.assertEqual(target_file_types, [FILE_TYPE_TTL_GZ])

    def test_nt_gz(self):
        target_file_types = get_target_file_types([FILE_TYPE_NT_GZ])
        self.assertEqual(target_file_types, [FILE_TYPE_NT_GZ])

    def test_rdf_xml_gz(self):
        target_file_types = get_target_file_types([FILE_TYPE_RDF_XML_GZ])
        self.assertEqual(target_file_types, [FILE_TYPE_RDF_XML_GZ])

    def test_ttl_zip(self):
        target_file_types = get_target_file_types([FILE_TYPE_TTL_ZIP])
        self.assertEqual(target_file_types, [FILE_TYPE_TTL_ZIP])

    def test_nt_zip(self):
        target_file_types = get_target_file_types([FILE_TYPE_NT_ZIP])
        self.assertEqual(target_file_types, [FILE_TYPE_NT_ZIP])

    def test_rdf_xml_zip(self):
        target_file_types = get_target_file_types([FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(target_file_types, [FILE_TYPE_RDF_XML_ZIP])

    def test_all(self):
        sys.stdin = io.StringIO('1')
        target_file_types = get_target_file_types([FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(target_file_types, [FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP])

if __name__ == "__main__":
    unittest.main()