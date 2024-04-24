import unittest
from pathlib import Path
import tempfile
from doctor.doctor import get_input_files_each
from doctor.consts import FILE_TYPE_TTL, FILE_TYPE_NT, FILE_TYPE_RDF_XML, FILE_TYPE_TTL_GZ, FILE_TYPE_NT_GZ, FILE_TYPE_RDF_XML_GZ, FILE_TYPE_TTL_ZIP, FILE_TYPE_NT_ZIP, FILE_TYPE_RDF_XML_ZIP
from shexer.consts import GZ, ZIP, TURTLE, NT, RDF_XML
from tests.consts import BASE_DIR, DIR_INPUT_TEST_DIR_TTL, DIR_INPUT_TEST_DIR_NT, DIR_INPUT_TEST_DIR_RDF_XML, COMPRESSED_DIR_TAR_GZ, COMPRESSED_DIR_ZIP, TTL_1, TTL_2, TTL_3, TTL_1_GZ, TTL_2_GZ, TTL_3_GZ, TTL_1_ZIP, NT_1, NT_2, NT_3, NT_1_GZ, NT_2_GZ, NT_3_GZ, NT_1_ZIP, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP

# INFO: Depending on the environment in which the test is run, there may be differences in the order in which file information is obtained, but this does not affect the results of the rdf-doctor process.
class TestGetInputFilesEach(unittest.TestCase):

    def test_file_ttl(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([TTL_1, TTL_2, TTL_3], temp_dir, 95)
        self.assertTrue([[TTL_1], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[TTL_2], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[TTL_3], None, TURTLE] in input_file_2d_list)
        self.assertEqual(exists_file_types, [FILE_TYPE_TTL])
        self.assertEqual(error_msg, None)

    def test_file_ttl_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], temp_dir, 95)
        self.assertTrue([[TTL_1_GZ], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[TTL_2_GZ], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[TTL_3_GZ], GZ, TURTLE] in input_file_2d_list)
        self.assertEqual(exists_file_types, [FILE_TYPE_TTL_GZ])
        self.assertEqual(error_msg, None)

    def test_file_ttl_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([TTL_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[TTL_1_ZIP], ZIP, TURTLE]])
        self.assertEqual(exists_file_types, [FILE_TYPE_TTL_ZIP])
        self.assertEqual(error_msg, None)


    def test_file_nt(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([NT_1, NT_2, NT_3], temp_dir, 95)
        self.assertTrue([[NT_1], None, NT] in input_file_2d_list)
        self.assertTrue([[NT_2], None, NT] in input_file_2d_list)
        self.assertTrue([[NT_3], None, NT] in input_file_2d_list)
        self.assertEqual(exists_file_types, [FILE_TYPE_NT])
        self.assertEqual(error_msg, None)

    def test_file_nt_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([NT_1_GZ, NT_2_GZ, NT_3_GZ], temp_dir, 95)
        self.assertTrue([[NT_1_GZ], GZ, NT] in input_file_2d_list)
        self.assertTrue([[NT_2_GZ], GZ, NT] in input_file_2d_list)
        self.assertTrue([[NT_3_GZ], GZ, NT] in input_file_2d_list)
        self.assertEqual(exists_file_types, [FILE_TYPE_NT_GZ])
        self.assertEqual(error_msg, None)


    def test_file_nt_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([NT_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[NT_1_ZIP], ZIP, NT]])
        self.assertEqual(exists_file_types, [FILE_TYPE_NT_ZIP])
        self.assertEqual(error_msg, None)


    def test_file_owl(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([OWL_1], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[OWL_1], None, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML])
        self.assertEqual(error_msg, None)

    def test_file_owl_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([OWL_1_GZ], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[OWL_1_GZ], GZ, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_GZ])
        self.assertEqual(error_msg, None)

    def test_file_owl_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([OWL_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[OWL_1_ZIP], ZIP, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(error_msg, None)

    def test_file_rdf(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([RDF_1], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[RDF_1], None, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML])
        self.assertEqual(error_msg, None)

    def test_file_rdf_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([RDF_1_GZ], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[RDF_1_GZ], GZ, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_GZ])
        self.assertEqual(error_msg, None)


    def test_file_rdf_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([RDF_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[RDF_1_ZIP], ZIP, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(error_msg, None)

    def test_file_xml(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([XML_1], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[XML_1], None, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML])
        self.assertEqual(error_msg, None)


    def test_file_xml_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([XML_1_GZ], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[XML_1_GZ], GZ, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_GZ])
        self.assertEqual(error_msg, None)

    def test_file_xml_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([XML_1_ZIP], temp_dir, 95)
        self.assertEqual(input_file_2d_list, [[[XML_1_ZIP], ZIP, RDF_XML]])
        self.assertEqual(exists_file_types, [FILE_TYPE_RDF_XML_ZIP])
        self.assertEqual(error_msg, None)

    def test_file_mix(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([TTL_1, TTL_2, TTL_3, TTL_1_GZ, TTL_2_GZ, TTL_3_GZ, TTL_1_ZIP, NT_1, NT_2, NT_3, NT_1_GZ, NT_2_GZ, NT_3_GZ, NT_1_ZIP, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP], temp_dir, 95)

        self.assertTrue([[TTL_1], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[TTL_2], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[TTL_3], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[TTL_1_GZ], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[TTL_2_GZ], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[TTL_3_GZ], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[TTL_1_ZIP], ZIP, TURTLE] in input_file_2d_list)
        self.assertTrue([[NT_1], None, NT] in input_file_2d_list)
        self.assertTrue([[NT_2], None, NT] in input_file_2d_list)
        self.assertTrue([[NT_3], None, NT] in input_file_2d_list)
        self.assertTrue([[NT_1_GZ], GZ, NT] in input_file_2d_list)
        self.assertTrue([[NT_2_GZ], GZ, NT] in input_file_2d_list)
        self.assertTrue([[NT_3_GZ], GZ, NT] in input_file_2d_list)
        self.assertTrue([[NT_1_ZIP], ZIP, NT] in input_file_2d_list)
        self.assertTrue([[OWL_1], None, RDF_XML] in input_file_2d_list)
        self.assertTrue([[OWL_1_GZ], GZ, RDF_XML] in input_file_2d_list)
        self.assertTrue([[OWL_1_ZIP], ZIP, RDF_XML] in input_file_2d_list)
        self.assertTrue([[RDF_1], None, RDF_XML] in input_file_2d_list)
        self.assertTrue([[RDF_1_GZ], GZ, RDF_XML] in input_file_2d_list)
        self.assertTrue([[RDF_1_ZIP], ZIP, RDF_XML] in input_file_2d_list)
        self.assertTrue([[XML_1], None, RDF_XML] in input_file_2d_list)
        self.assertTrue([[XML_1_GZ], GZ, RDF_XML] in input_file_2d_list)
        self.assertTrue([[XML_1_ZIP], ZIP, RDF_XML] in input_file_2d_list)

        self.assertTrue(FILE_TYPE_TTL in exists_file_types)
        self.assertTrue(FILE_TYPE_TTL_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_TTL_ZIP in exists_file_types)
        self.assertTrue(FILE_TYPE_NT in exists_file_types)
        self.assertTrue(FILE_TYPE_NT_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_NT_ZIP in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML_ZIP in exists_file_types)
        self.assertEqual(error_msg, None)

    def test_dir_one(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([DIR_INPUT_TEST_DIR_TTL], temp_dir, 95)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl')], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl')], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl')], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl.gz')], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl.gz')], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl.gz')], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl.zip')], ZIP, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl.zip')], ZIP, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl.zip')], ZIP, TURTLE] in input_file_2d_list)

        self.assertTrue(FILE_TYPE_TTL in exists_file_types)
        self.assertTrue(FILE_TYPE_TTL_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_TTL_ZIP in exists_file_types)
        self.assertEqual(error_msg, None)


    def test_dir_multi(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([DIR_INPUT_TEST_DIR_TTL, DIR_INPUT_TEST_DIR_NT, DIR_INPUT_TEST_DIR_RDF_XML], temp_dir, 95)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl')], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl')], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl')], None, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl.gz')], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl.gz')], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl.gz')], GZ, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_1.ttl.zip')], ZIP, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_2.ttl.zip')], ZIP, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_turtle/test_ttl_3.ttl.zip')], ZIP, TURTLE] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_nt/test_nt_1.nt')], None, NT] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_nt/test_nt_2.nt')], None, NT] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_nt/test_nt_3.nt')], None, NT] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_nt/test_nt_1.nt.gz')], GZ, NT] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_nt/test_nt_2.nt.gz')], GZ, NT] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_nt/test_nt_3.nt.gz')], GZ, NT] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_nt/test_nt_1.nt.zip')], ZIP, NT] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_rdf_xml/test_owl_1.owl')], None, RDF_XML] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_rdf_xml/test_rdf_1.rdf')], None, RDF_XML] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_rdf_xml/test_xml_1.xml')], None, RDF_XML] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_rdf_xml/test_owl_1.owl.gz')], GZ, RDF_XML] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_rdf_xml/test_xml_1.xml.gz')], GZ, RDF_XML] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_rdf_xml/test_rdf_1.rdf.gz')], GZ, RDF_XML] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_rdf_xml/test_owl_1.owl.zip')], ZIP, RDF_XML] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_rdf_xml/test_rdf_1.rdf.zip')], ZIP, RDF_XML] in input_file_2d_list)
        self.assertTrue([[Path(BASE_DIR+'dir_input_test_rdf_xml/test_xml_1.xml.zip')], ZIP, RDF_XML] in input_file_2d_list)

        self.assertTrue(FILE_TYPE_TTL in exists_file_types)
        self.assertTrue(FILE_TYPE_TTL_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_TTL_ZIP in exists_file_types)
        self.assertTrue(FILE_TYPE_NT in exists_file_types)
        self.assertTrue(FILE_TYPE_NT_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_NT_ZIP in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML_ZIP in exists_file_types)
        self.assertEqual(error_msg, None)


    def test_tar_gz(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([COMPRESSED_DIR_TAR_GZ], temp_dir, 95)

        input_file_2d_list_mod = []
        for input_file_list in input_file_2d_list:
            input_file_2d_list_mod.append([Path(input_file_list[0][0]).name, input_file_list[1], input_file_list[2]])

        self.assertTrue(["test_ttl_1.ttl", None ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_2.ttl", None ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_3.ttl", None ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_1.nt", None, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_2.nt", None, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_3.nt", None, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_owl_1.owl", None, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_rdf_1.rdf", None, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_xml_1.xml", None, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_1.ttl.gz", GZ ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_2.ttl.gz", GZ ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_3.ttl.gz", GZ ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_1.nt.gz", GZ, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_2.nt.gz", GZ, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_3.nt.gz", GZ, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_owl_1.owl.gz", GZ, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_rdf_1.rdf.gz", GZ, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_xml_1.xml.gz", GZ, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_1.ttl.zip", ZIP ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_2.ttl.zip", ZIP ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_3.ttl.zip", ZIP ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_1.nt.zip", ZIP, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_owl_1.owl.zip", ZIP, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_rdf_1.rdf.zip", ZIP, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_xml_1.xml.zip", ZIP, RDF_XML] in input_file_2d_list_mod)

        self.assertTrue(FILE_TYPE_TTL in exists_file_types)
        self.assertTrue(FILE_TYPE_TTL_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_TTL_ZIP in exists_file_types)
        self.assertTrue(FILE_TYPE_NT in exists_file_types)
        self.assertTrue(FILE_TYPE_NT_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_NT_ZIP in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML_ZIP in exists_file_types)
        self.assertEqual(error_msg, None)

    def test_zipped_dir(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([COMPRESSED_DIR_ZIP], temp_dir, 95)
        input_file_2d_list_mod = []
        for input_file_list in input_file_2d_list:
            input_file_2d_list_mod.append([Path(input_file_list[0][0]).name, input_file_list[1], input_file_list[2]])

        self.assertTrue(["test_ttl_1.ttl", None ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_2.ttl", None ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_3.ttl", None ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_1.nt", None, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_2.nt", None, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_3.nt", None, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_owl_1.owl", None, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_rdf_1.rdf", None, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_xml_1.xml", None, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_1.ttl.gz", GZ ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_2.ttl.gz", GZ ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_3.ttl.gz", GZ ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_1.nt.gz", GZ, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_2.nt.gz", GZ, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_3.nt.gz", GZ, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_owl_1.owl.gz", GZ, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_rdf_1.rdf.gz", GZ, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_xml_1.xml.gz", GZ, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_1.ttl.zip", ZIP ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_2.ttl.zip", ZIP ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_ttl_3.ttl.zip", ZIP ,TURTLE] in input_file_2d_list_mod)
        self.assertTrue(["test_nt_1.nt.zip", ZIP, NT] in input_file_2d_list_mod)
        self.assertTrue(["test_owl_1.owl.zip", ZIP, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_rdf_1.rdf.zip", ZIP, RDF_XML] in input_file_2d_list_mod)
        self.assertTrue(["test_xml_1.xml.zip", ZIP, RDF_XML] in input_file_2d_list_mod)

        self.assertTrue(FILE_TYPE_TTL in exists_file_types)
        self.assertTrue(FILE_TYPE_TTL_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_TTL_ZIP in exists_file_types)
        self.assertTrue(FILE_TYPE_NT in exists_file_types)
        self.assertTrue(FILE_TYPE_NT_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_NT_ZIP in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML_GZ in exists_file_types)
        self.assertTrue(FILE_TYPE_RDF_XML_ZIP in exists_file_types)
        self.assertEqual(error_msg, None)


    def test_file_doed_not_exist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([BASE_DIR+"aaa.txt"], temp_dir, 95)
        self.assertEqual(input_file_2d_list, None)
        self.assertEqual(exists_file_types, None)
        self.assertEqual(error_msg, '"' + BASE_DIR+'aaa.txt" does not exist.')

    def test_file_extension_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([BASE_DIR+"test_txt_1.txt"], temp_dir, 95)
        self.assertEqual(input_file_2d_list, None)
        self.assertEqual(exists_file_types, None)
        self.assertEqual(error_msg, '".txt" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.')

    def test_file_gz_extension_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([BASE_DIR+"test_txt_1.txt.gz"], temp_dir, 95)
        self.assertEqual(input_file_2d_list, None)
        self.assertEqual(exists_file_types, None)
        self.assertEqual(error_msg, '".txt.gz" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.')

    def test_file_zip_extension_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file_2d_list, exists_file_types, error_msg = get_input_files_each([BASE_DIR+"test_txt_1.txt.zip"], temp_dir, 95)
        self.assertEqual(input_file_2d_list, None)
        self.assertEqual(exists_file_types, None)
        self.assertEqual(error_msg, '".txt.zip" is an unsupported extension. ".ttl", ".nt", ".rdf", ".xml", ".owl" and their compressed versions are supported.')

if __name__ == "__main__":
    unittest.main()