import unittest
from pathlib import Path
import tempfile
from doctor.doctor import get_input_files_by_type
from doctor.consts import FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP
from shexer.consts import GZ, ZIP, TURTLE, NT, RDF_XML
from tests.consts import BASE_DIR, DIR_INPUT_TEST_DIR_TTL, DIR_INPUT_TEST_DIR_NT, DIR_INPUT_TEST_DIR_RDF_XML, COMPRESSED_DIR_TAR_GZ, COMPRESSED_DIR_ZIP, TTL_1, TTL_2, TTL_3, TTL_1_GZ, TTL_2_GZ, TTL_3_GZ, TTL_1_ZIP, NT_1, NT_2, NT_3, NT_1_GZ, NT_2_GZ, NT_3_GZ, NT_1_ZIP, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP

# INFO: Depending on the environment in which the test is run, there may be differences in the order in which file information is obtained, but this does not affect the results of the rdf-doctor process.
class TestGetInputFilesByType(unittest.TestCase):

    def test_file_ttl(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([TTL_1, TTL_2, TTL_3], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[TTL_1, TTL_2, TTL_3], None, TURTLE]])
        self.assertEqual(exists_file_types, [FILE_TYPE_TTL])
        self.assertEqual(error_msg, None)

    def test_file_ttl_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], GZ, TURTLE]])
        self.assertEqual(exists_file_types, [FILE_TYPE_TTL_GZ])
        self.assertEqual(error_msg, None)

    def test_file_ttl_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([TTL_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[TTL_1_ZIP], ZIP, TURTLE]])
        self.assertEqual(exists_file_types, [FILE_TYPE_TTL_ZIP])
        self.assertEqual(error_msg, None)


    def test_file_nt(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([NT_1, NT_2, NT_3], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[NT_1, NT_2, NT_3], None, NT]])
        self.assertEqual(exists_file_types, [FILE_TYPE_NT])
        self.assertEqual(error_msg, None)

    def test_file_nt_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([NT_1_GZ, NT_2_GZ, NT_3_GZ], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[NT_1_GZ, NT_2_GZ, NT_3_GZ], GZ, NT]])
        self.assertEqual(exists_file_types, [FILE_TYPE_NT_GZ])
        self.assertEqual(error_msg, None)


    def test_file_nt_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([NT_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[NT_1_ZIP], ZIP, NT]])
        self.assertEqual(exists_file_types, [FILE_TYPE_NT_ZIP])
        self.assertEqual(error_msg, None)


    def test_file_owl(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([OWL_1], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[OWL_1], None, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML])
        self.assertEqual(error_msg, None)

    def test_file_owl_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([OWL_1_GZ], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[OWL_1_GZ], GZ, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_GZ])
        self.assertEqual(error_msg, None)

    def test_file_owl_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([OWL_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[OWL_1_ZIP], ZIP, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(error_msg, None)

    def test_file_rdf(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([RDF_1], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[RDF_1], None, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML])
        self.assertEqual(error_msg, None)

    def test_file_rdf_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([RDF_1_GZ], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[RDF_1_GZ], GZ, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_GZ])
        self.assertEqual(error_msg, None)


    def test_file_rdf_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([RDF_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[RDF_1_ZIP], ZIP, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(error_msg, None)

    def test_file_xml(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([XML_1], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[XML_1], None, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML])
        self.assertEqual(error_msg, None)


    def test_file_xml_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([XML_1_GZ], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[XML_1_GZ], GZ, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_GZ])
        self.assertEqual(error_msg, None)


    def test_file_xml_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([XML_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[XML_1_ZIP], ZIP, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(error_msg, None)

    def test_file_mix(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([TTL_1, TTL_2, TTL_3, TTL_1_GZ, TTL_2_GZ, TTL_3_GZ, TTL_1_ZIP, NT_1, NT_2, NT_3, NT_1_GZ, NT_2_GZ, NT_3_GZ, NT_1_ZIP, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[TTL_1, TTL_2, TTL_3], None, TURTLE], \
                                                [[NT_1, NT_2, NT_3], None, NT], \
                                                [[OWL_1, RDF_1, XML_1], None, RDF_XML], \
                                                [[TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], GZ, TURTLE], \
                                                [[NT_1_GZ, NT_2_GZ, NT_3_GZ], GZ, NT], \
                                                [[OWL_1_GZ, RDF_1_GZ, XML_1_GZ], GZ, RDF_XML], \
                                                [[TTL_1_ZIP], ZIP, TURTLE], \
                                                [[NT_1_ZIP], ZIP, NT], \
                                                [[OWL_1_ZIP, RDF_1_ZIP, XML_1_ZIP], ZIP, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(error_msg, None)

    def test_dir_one(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([DIR_INPUT_TEST_DIR_TTL], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl')], None, 'turtle'], \
                                                [[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl.gz'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl.gz'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl.gz')], 'gz', 'turtle'], \
                                                [[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl.zip'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl.zip'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl.zip')], 'zip', 'turtle']])
        self.assertEqual(exists_file_types, [FILE_TYPE_TTL, FILE_TYPE_TTL_GZ, FILE_TYPE_TTL_ZIP])
        self.assertEqual(error_msg, None)


    def test_dir_multi(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([DIR_INPUT_TEST_DIR_TTL, DIR_INPUT_TEST_DIR_NT, DIR_INPUT_TEST_DIR_RDF_XML], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl')], None, 'turtle'], \
                                                [[Path(BASE_DIR+'dir_input_test_nt/test_nt_1.nt'), Path(BASE_DIR+'dir_input_test_nt/test_nt_3.nt'), Path(BASE_DIR+'dir_input_test_nt/test_nt_2.nt')], None, 'nt'], \
                                                [[Path(BASE_DIR+'dir_input_test_rdf_xml/test_rdf_1.rdf'), Path(BASE_DIR+'dir_input_test_rdf_xml/test_owl_1.owl'), Path(BASE_DIR+'dir_input_test_rdf_xml/test_xml_1.xml')], None, 'xml'], \
                                                [[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl.gz'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl.gz'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl.gz')], 'gz', 'turtle'], \
                                                [[Path(BASE_DIR+'dir_input_test_nt/test_nt_1.nt.gz'), Path(BASE_DIR+'dir_input_test_nt/test_nt_3.nt.gz'), Path(BASE_DIR+'dir_input_test_nt/test_nt_2.nt.gz')], 'gz', 'nt'], \
                                                [[Path(BASE_DIR+'dir_input_test_rdf_xml/test_xml_1.xml.gz'), Path(BASE_DIR+'dir_input_test_rdf_xml/test_rdf_1.rdf.gz'), Path(BASE_DIR+'dir_input_test_rdf_xml/test_owl_1.owl.gz')], 'gz', 'xml'], \
                                                [[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl.zip'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl.zip'), Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl.zip')], 'zip', 'turtle'], \
                                                [[Path(BASE_DIR+'dir_input_test_nt/test_nt_1.nt.zip')], 'zip', 'nt'], \
                                                [[Path(BASE_DIR+'dir_input_test_rdf_xml/test_xml_1.xml.zip'), Path(BASE_DIR+'dir_input_test_rdf_xml/test_owl_1.owl.zip'), Path(BASE_DIR+'dir_input_test_rdf_xml/test_rdf_1.rdf.zip')], 'zip', 'xml']])
        self.assertEqual(exists_file_types, [FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(error_msg, None)


    def test_tar_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([COMPRESSED_DIR_TAR_GZ], temp_dir, 95)

        # The temporary directory contains a UUID and the full path of the file is not fixed, so the confirmation method is different from other tests.
        self.assertTrue("test_ttl_1.ttl" in str(input_file_2d_list[0][0][0]))
        self.assertTrue("test_ttl_3.ttl" in str(input_file_2d_list[0][0][1]))
        self.assertTrue("test_ttl_2.ttl" in str(input_file_2d_list[0][0][2]))
        self.assertEqual(input_file_2d_list[0][1], None)
        self.assertEqual(input_file_2d_list[0][2], TURTLE)
        self.assertTrue("test_nt_1.nt" in str(input_file_2d_list[1][0][0]))
        self.assertTrue("test_nt_3.nt" in str(input_file_2d_list[1][0][1]))
        self.assertTrue("test_nt_2.nt" in str(input_file_2d_list[1][0][2]))
        self.assertEqual(input_file_2d_list[1][1], None)
        self.assertEqual(input_file_2d_list[1][2], NT)
        self.assertTrue("test_rdf_1.rdf" in str(input_file_2d_list[2][0][0]))
        self.assertTrue("test_owl_1.owl" in str(input_file_2d_list[2][0][1]))
        self.assertTrue("test_xml_1.xml" in str(input_file_2d_list[2][0][2]))
        self.assertEqual(input_file_2d_list[2][1], None)
        self.assertEqual(input_file_2d_list[2][2], RDF_XML)
        self.assertTrue("test_ttl_1.ttl.gz" in str(input_file_2d_list[3][0][0]))
        self.assertTrue("test_ttl_3.ttl.gz" in str(input_file_2d_list[3][0][1]))
        self.assertTrue("test_ttl_2.ttl.gz" in str(input_file_2d_list[3][0][2]))
        self.assertEqual(input_file_2d_list[3][1], GZ)
        self.assertEqual(input_file_2d_list[3][2], TURTLE)
        self.assertTrue("test_nt_1.nt.gz" in str(input_file_2d_list[4][0][0]))
        self.assertTrue("test_nt_3.nt.gz" in str(input_file_2d_list[4][0][1]))
        self.assertTrue("test_nt_2.nt.gz" in str(input_file_2d_list[4][0][2]))
        self.assertEqual(input_file_2d_list[4][1], GZ)
        self.assertEqual(input_file_2d_list[4][2], NT)
        self.assertTrue("test_xml_1.xml.gz" in str(input_file_2d_list[5][0][0]))
        self.assertTrue("test_rdf_1.rdf.gz" in str(input_file_2d_list[5][0][1]))
        self.assertTrue("test_owl_1.owl.gz" in str(input_file_2d_list[5][0][2]))
        self.assertEqual(input_file_2d_list[5][1], GZ)
        self.assertEqual(input_file_2d_list[5][2], RDF_XML)
        self.assertTrue("test_ttl_3.ttl.zip" in str(input_file_2d_list[6][0][0]))
        self.assertTrue("test_ttl_2.ttl.zip" in str(input_file_2d_list[6][0][1]))
        self.assertTrue("test_ttl_1.ttl.zip" in str(input_file_2d_list[6][0][2]))
        self.assertEqual(input_file_2d_list[6][1], ZIP)
        self.assertEqual(input_file_2d_list[6][2], TURTLE)
        self.assertTrue("test_nt_1.nt.zip" in str(input_file_2d_list[7][0][0]))
        self.assertEqual(input_file_2d_list[7][1], ZIP)
        self.assertEqual(input_file_2d_list[7][2], NT)
        self.assertTrue("test_xml_1.xml.zip" in str(input_file_2d_list[8][0][0]))
        self.assertTrue("test_owl_1.owl.zip" in str(input_file_2d_list[8][0][1]))
        self.assertTrue("test_rdf_1.rdf.zip" in str(input_file_2d_list[8][0][2]))
        self.assertEqual(input_file_2d_list[8][1], ZIP)
        self.assertEqual(input_file_2d_list[8][2], RDF_XML)

        self.assertEqual(exists_file_types, [FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(error_msg, None)

    def test_zipped_dir(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([COMPRESSED_DIR_ZIP], temp_dir, 95)

        # The temporary directory contains a UUID and the full path of the file is not fixed, so the confirmation method is different from other tests.
        self.assertTrue("test_ttl_1.ttl" in str(input_file_2d_list[0][0][0]))
        self.assertTrue("test_ttl_3.ttl" in str(input_file_2d_list[0][0][1]))
        self.assertTrue("test_ttl_2.ttl" in str(input_file_2d_list[0][0][2]))
        self.assertEqual(input_file_2d_list[0][1], None)
        self.assertEqual(input_file_2d_list[0][2], TURTLE)
        self.assertTrue("test_nt_1.nt" in str(input_file_2d_list[1][0][0]))
        self.assertTrue("test_nt_3.nt" in str(input_file_2d_list[1][0][1]))
        self.assertTrue("test_nt_2.nt" in str(input_file_2d_list[1][0][2]))
        self.assertEqual(input_file_2d_list[1][1], None)
        self.assertEqual(input_file_2d_list[1][2], NT)
        self.assertTrue("test_rdf_1.rdf" in str(input_file_2d_list[2][0][0]))
        self.assertTrue("test_owl_1.owl" in str(input_file_2d_list[2][0][1]))
        self.assertTrue("test_xml_1.xml" in str(input_file_2d_list[2][0][2]))
        self.assertEqual(input_file_2d_list[2][1], None)
        self.assertEqual(input_file_2d_list[2][2], RDF_XML)
        self.assertTrue("test_ttl_1.ttl.gz" in str(input_file_2d_list[3][0][0]))
        self.assertTrue("test_ttl_3.ttl.gz" in str(input_file_2d_list[3][0][1]))
        self.assertTrue("test_ttl_2.ttl.gz" in str(input_file_2d_list[3][0][2]))
        self.assertEqual(input_file_2d_list[3][1], GZ)
        self.assertEqual(input_file_2d_list[3][2], TURTLE)
        self.assertTrue("test_nt_1.nt.gz" in str(input_file_2d_list[4][0][0]))
        self.assertTrue("test_nt_3.nt.gz" in str(input_file_2d_list[4][0][1]))
        self.assertTrue("test_nt_2.nt.gz" in str(input_file_2d_list[4][0][2]))
        self.assertEqual(input_file_2d_list[4][1], GZ)
        self.assertEqual(input_file_2d_list[4][2], NT)
        self.assertTrue("test_xml_1.xml.gz" in str(input_file_2d_list[5][0][0]))
        self.assertTrue("test_rdf_1.rdf.gz" in str(input_file_2d_list[5][0][1]))
        self.assertTrue("test_owl_1.owl.gz" in str(input_file_2d_list[5][0][2]))
        self.assertEqual(input_file_2d_list[5][1], GZ)
        self.assertEqual(input_file_2d_list[5][2], RDF_XML)
        self.assertTrue("test_ttl_3.ttl.zip" in str(input_file_2d_list[6][0][0]))
        self.assertTrue("test_ttl_2.ttl.zip" in str(input_file_2d_list[6][0][1]))
        self.assertTrue("test_ttl_1.ttl.zip" in str(input_file_2d_list[6][0][2]))
        self.assertEqual(input_file_2d_list[6][1], ZIP)
        self.assertEqual(input_file_2d_list[6][2], TURTLE)
        self.assertTrue("test_nt_1.nt.zip" in str(input_file_2d_list[7][0][0]))
        self.assertEqual(input_file_2d_list[7][1], ZIP)
        self.assertEqual(input_file_2d_list[7][2], NT)
        self.assertTrue("test_xml_1.xml.zip" in str(input_file_2d_list[8][0][0]))
        self.assertTrue("test_owl_1.owl.zip" in str(input_file_2d_list[8][0][1]))
        self.assertTrue("test_rdf_1.rdf.zip" in str(input_file_2d_list[8][0][2]))
        self.assertEqual(input_file_2d_list[8][1], ZIP)
        self.assertEqual(input_file_2d_list[8][2], RDF_XML)

        self.assertEqual(exists_file_types, [FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(error_msg, None)

    def test_file_does_not_exist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([BASE_DIR+"aaa.txt"], temp_dir, 95)
        self.assertEqual(input_file_2d_list, None)
        self.assertEqual(exists_file_types, None)
        self.assertEqual(error_msg, '"' + BASE_DIR+'aaa.txt" does not exist.')

    def test_file_extension_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([BASE_DIR+"test_txt_1.txt"], temp_dir, 95)
        self.assertEqual(input_file_2d_list, None)
        self.assertEqual(exists_file_types, None)
        self.assertEqual(error_msg, '".txt" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.')

    def test_file_gz_extension_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([BASE_DIR+"test_txt_1.txt.gz"], temp_dir, 95)
        self.assertEqual(input_file_2d_list, None)
        self.assertEqual(exists_file_types, None)
        self.assertEqual(error_msg, '".txt.gz" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.')

    def test_file_zip_extension_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_by_type([BASE_DIR+"test_txt_1.txt.zip"], temp_dir, 95)
        self.assertEqual(input_file_2d_list, None)
        self.assertEqual(exists_file_types, None)
        self.assertEqual(error_msg, '".txt.zip" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.')

if __name__ == "__main__":
    unittest.main()