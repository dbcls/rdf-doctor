import unittest
from pathlib import Path
from doctor.doctor import get_input_files_by_type
from tests.consts import BASE_DIR, NT_1, NT_1_GZ, NT_2, NT_2_GZ, NT_3, NT_3_GZ, TTL_1, TTL_1_GZ, TTL_2, TTL_2_GZ, TTL_3, TTL_3_GZ, REFINE_PREFIX_URIS_FILE_PATH, REFINE_CLASS_URIS_FILE_PATH, PREFIXES_FILE_PATH


class TestGetInputFilesByType(unittest.TestCase):

    def test_file_single(self):
        input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([TTL_1], None, 95)
        self.assertEqual(input_file_2d_list, [[[BASE_DIR+'test_ttl_1.ttl'], None, 'turtle']])
        self.assertEqual(exists_file_types, ['ttl'])
        self.assertEqual(error_msg, None)

    def test_file_multi(self):
        input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([NT_1, NT_1_GZ, NT_2, NT_2_GZ, NT_3, NT_3_GZ, TTL_1, TTL_1_GZ, TTL_2, TTL_2_GZ, TTL_3, TTL_3_GZ], None, 95)
        self.assertEqual(input_file_2d_list, [[[BASE_DIR+'test_ttl_1.ttl', BASE_DIR+'test_ttl_2.ttl', BASE_DIR+'test_ttl_3.ttl'], None, 'turtle'], \
                                                [[BASE_DIR+'test_nt_1.nt', BASE_DIR+'test_nt_2.nt', BASE_DIR+'test_nt_3.nt'], None, 'nt'], \
                                                [[BASE_DIR+'test_ttl_1.ttl.gz', BASE_DIR+'test_ttl_2.ttl.gz', BASE_DIR+'test_ttl_3.ttl.gz'], 'gz', 'turtle'], \
                                                [[BASE_DIR+'test_nt_1.nt.gz', BASE_DIR+'test_nt_2.nt.gz', BASE_DIR+'test_nt_3.nt.gz'], 'gz', 'nt']])
        self.assertEqual(exists_file_types, ['ttl', 'nt', 'ttl_gz', 'nt_gz'])
        self.assertEqual(error_msg, None)

    def test_dir(self):
        input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([BASE_DIR], None, 95)
        self.assertEqual(input_file_2d_list, [[[Path(BASE_DIR+'test_ttl_5.ttl'), Path(BASE_DIR+'test_ttl_4.ttl'), Path(BASE_DIR+'test_ttl_1.ttl'), Path(BASE_DIR+'test_ttl_3.ttl'), Path(BASE_DIR+'test_ttl_2.ttl')], None, 'turtle'], \
                                                [[Path(BASE_DIR+'test_nt_1.nt'), Path(BASE_DIR+'test_nt_3.nt'), Path(BASE_DIR+'test_nt_2.nt')], None, 'nt'], \
                                                [[Path(BASE_DIR+'test_rdf_1.rdf'), Path(BASE_DIR+'test_owl_1.owl'), Path(BASE_DIR+'test_xml_1.xml')], None, 'xml'], \
                                                [[Path(BASE_DIR+'test_ttl_1.ttl.gz'), Path(BASE_DIR+'test_ttl_3.ttl.gz'), Path(BASE_DIR+'test_ttl_2.ttl.gz')], 'gz', 'turtle'], \
                                                [[Path(BASE_DIR+'test_nt_1.nt.gz'), Path(BASE_DIR+'test_nt_3.nt.gz'), Path(BASE_DIR+'test_nt_2.nt.gz')], 'gz', 'nt'], \
                                                [[Path(BASE_DIR+'test_xml_1.xml.gz'), Path(BASE_DIR+'test_rdf_1.rdf.gz'), Path(BASE_DIR+'test_owl_1.owl.gz')], 'gz', 'xml'], \
                                                [[Path(BASE_DIR+'test_ttl_1.ttl.zip')], 'zip', 'turtle'], [[Path(BASE_DIR+'test_nt_1.nt.zip')], 'zip', 'nt'], \
                                                [[Path(BASE_DIR+'test_xml_1.xml.zip'), Path(BASE_DIR+'test_owl_1.owl.zip'), Path(BASE_DIR+'test_rdf_1.rdf.zip')], 'zip', 'xml']])
        self.assertEqual(exists_file_types, ['ttl', 'nt', 'rdf_xml', 'ttl_gz', 'nt_gz', 'rdf_xml_gz', 'ttl_zip', 'nt_zip', 'rdf_xml_zip'])
        self.assertEqual(error_msg, None)


if __name__ == "__main__":
    unittest.main()