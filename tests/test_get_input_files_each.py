import unittest
from pathlib import Path
from doctor.doctor import get_input_files_each
from tests.consts import BASE_DIR, NT_1, NT_1_GZ, NT_2, NT_2_GZ, NT_3, NT_3_GZ, TTL_1, TTL_1_GZ, TTL_2, TTL_2_GZ, TTL_3, TTL_3_GZ


class TestGetInputFilesByType(unittest.TestCase):

    def test_file_single(self):
        input_file_2d_list, exists_file_types, error_msg = get_input_files_each([TTL_1], None, 95)
        self.assertEqual(input_file_2d_list, [[[BASE_DIR+'test_ttl_1.ttl'], None, 'turtle']])
        self.assertEqual(exists_file_types, ['ttl'])
        self.assertEqual(error_msg, None)

    def test_file_multi(self):
        input_file_2d_list, exists_file_types, error_msg = get_input_files_each([NT_1, NT_1_GZ, NT_2, NT_2_GZ, NT_3, NT_3_GZ, TTL_1, TTL_1_GZ, TTL_2, TTL_2_GZ, TTL_3, TTL_3_GZ], None, 95)
        print(input_file_2d_list)
        print(exists_file_types)
        self.assertEqual(input_file_2d_list, [[[BASE_DIR+'test_nt_1.nt'], None, 'nt'], \
                                                [[BASE_DIR+'test_nt_1.nt.gz'], 'gz', 'nt'], \
                                                [[BASE_DIR+'test_nt_2.nt'], None, 'nt'], \
                                                [[BASE_DIR+'test_nt_2.nt.gz'], 'gz', 'nt'], \
                                                [[BASE_DIR+'test_nt_3.nt'], None, 'nt'], \
                                                [[BASE_DIR+'test_nt_3.nt.gz'], 'gz', 'nt'], \
                                                [[BASE_DIR+'test_ttl_1.ttl'], None, 'turtle'], \
                                                [[BASE_DIR+'test_ttl_1.ttl.gz'], 'gz', 'turtle'], \
                                                [[BASE_DIR+'test_ttl_2.ttl'], None, 'turtle'], \
                                                [[BASE_DIR+'test_ttl_2.ttl.gz'], 'gz', 'turtle'], \
                                                [[BASE_DIR+'test_ttl_3.ttl'], None, 'turtle'], \
                                                [[BASE_DIR+'test_ttl_3.ttl.gz'], 'gz', 'turtle']])
        self.assertEqual(exists_file_types, ['nt', 'nt_gz', 'ttl', 'ttl_gz'])
        self.assertEqual(error_msg, None)

    def test_dir(self):
        input_file_2d_list, exists_file_types, error_msg = get_input_files_each([BASE_DIR], None, 95)
        print(input_file_2d_list)
        print(exists_file_types)
        self.assertEqual(input_file_2d_list, [[[Path(BASE_DIR+'test_nt_1.nt.gz')], 'gz', 'nt'], \
                                                [[Path(BASE_DIR+'test_ttl_1.ttl.gz')], 'gz', 'turtle'], \
                                                [[Path(BASE_DIR+'test_nt_1.nt.zip')], 'zip', 'nt'], \
                                                [[Path(BASE_DIR+'test_xml_1.xml.gz')], 'gz', 'xml'], \
                                                [[Path(BASE_DIR+'test_rdf_1.rdf.gz')], 'gz', 'xml'], \
                                                [[Path(BASE_DIR+'test_nt_3.nt.gz')], 'gz', 'nt'], \
                                                [[Path(BASE_DIR+'test_owl_1.owl.gz')], 'gz', 'xml'], \
                                                [[Path(BASE_DIR+'test_ttl_3.ttl.gz')], 'gz', 'turtle'], \
                                                [[Path(BASE_DIR+'test_rdf_1.rdf')], None, 'xml'], \
                                                [[Path(BASE_DIR+'test_xml_1.xml.zip')], 'zip', 'xml'], \
                                                [[Path(BASE_DIR+'test_nt_1.nt')], None, 'nt'], \
                                                [[Path(BASE_DIR+'test_nt_2.nt.gz')], 'gz', 'nt'], \
                                                [[Path(BASE_DIR+'test_owl_1.owl.zip')], 'zip', 'xml'], \
                                                [[Path(BASE_DIR+'test_rdf_1.rdf.zip')], 'zip', 'xml'], \
                                                [[Path(BASE_DIR+'test_nt_3.nt')], None, 'nt'], \
                                                [[Path(BASE_DIR+'test_nt_2.nt')], None, 'nt'], \
                                                [[Path(BASE_DIR+'test_ttl_2.ttl.gz')], 'gz', 'turtle'], \
                                                [[Path(BASE_DIR+'test_owl_1.owl')], None, 'xml'], \
                                                [[Path(BASE_DIR+'test_xml_1.xml')], None, 'xml'], \
                                                [[Path(BASE_DIR+'test_ttl_5.ttl')], None, 'turtle'], \
                                                [[Path(BASE_DIR+'test_ttl_4.ttl')], None, 'turtle'], \
                                                [[Path(BASE_DIR+'test_ttl_1.ttl')], None, 'turtle'], \
                                                [[Path(BASE_DIR+'test_ttl_3.ttl')], None, 'turtle'], \
                                                [[Path(BASE_DIR+'test_ttl_1.ttl.zip')], 'zip', 'turtle'], \
                                                [[Path(BASE_DIR+'test_ttl_2.ttl')], None, 'turtle']])
        self.assertEqual(exists_file_types, ['nt_gz', 'ttl_gz', 'nt_zip', 'rdf_xml_gz', 'rdf_xml', 'rdf_xml_zip', 'nt', 'ttl', 'ttl_zip'])
        self.assertEqual(error_msg, None)


if __name__ == "__main__":
    unittest.main()