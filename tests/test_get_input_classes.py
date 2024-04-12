import unittest
from doctor.doctor import get_input_classes
from doctor.consts import TARGET_CLASS_ALL
from tests.consts import TTL_1, TTL_2, TTL_3, TTL_1_GZ, TTL_2_GZ, TTL_3_GZ, TTL_1_ZIP, NT_1, NT_2, NT_3, NT_1_GZ, NT_2_GZ, NT_3_GZ, NT_1_ZIP, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP
from shexer.consts import NT, TURTLE, RDF_XML, GZ, ZIP

class TestGetClassesList(unittest.TestCase):

    def test_nt_all(self):
        input_classes = get_input_classes([NT_1], NT, None, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_nt_specify_one(self):
        input_classes = get_input_classes([NT_1], NT, None, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_nt_specify_two(self):
        input_classes = get_input_classes([NT_1], NT, None, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_ttl_all(self):
        input_classes = get_input_classes([TTL_1], TURTLE, None, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_ttl_specify_one(self):
        input_classes = get_input_classes([TTL_1], TURTLE, None, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_ttl_specify_two(self):
        input_classes = get_input_classes([TTL_1], TURTLE, None, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_nt_gz_all(self):
        input_classes = get_input_classes([NT_1_GZ], NT, GZ, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_nt_gz_specify_one(self):
        input_classes = get_input_classes([NT_1_GZ], NT, GZ, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_nt_gz_specify_two(self):
        input_classes = get_input_classes([NT_1_GZ], NT, GZ, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_ttl_gz_all(self):
        input_classes = get_input_classes([TTL_1_GZ], TURTLE, GZ, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_ttl_gz_specify_one(self):
        input_classes = get_input_classes([TTL_1_GZ], TURTLE, GZ, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_ttl_gz_specify_two(self):
        input_classes = get_input_classes([TTL_1_GZ], TURTLE, GZ, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_nt_multi(self):
        input_classes = get_input_classes([NT_1, NT_2, NT_3], NT, None, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document', 'http://xmlns.com/foaf/0.1/PErson', 'http://xmlns.com/foaf/0.1#Person', 'http://xmlns.com/foaf/0.1#Document'])

    def test_ttl_multi(self):
        input_classes = get_input_classes([TTL_1, TTL_2, TTL_3], TURTLE, None, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document', 'http://xmlns.com/foaf/0.1#Person', 'http://xmlns.com/foaf/0.1#Document', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APERSON', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3AParson', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADocument', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADOCUMENT'])

    def test_nt_gz_multi(self):
        input_classes = get_input_classes([NT_1_GZ, NT_2_GZ, NT_3_GZ], NT, GZ, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document', 'http://xmlns.com/foaf/0.1/PErson', 'http://xmlns.com/foaf/0.1#Person', 'http://xmlns.com/foaf/0.1#Document'])

    def test_ttl_gz_multi(self):
        input_classes = get_input_classes([TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], TURTLE, GZ, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document', 'http://xmlns.com/foaf/0.1#Person', 'http://xmlns.com/foaf/0.1#Document', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APERSON', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3AParson', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADocument', 'http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADOCUMENT'])

    def test_nt_gz_all(self):
        input_classes = get_input_classes([NT_1_GZ], NT, GZ, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_nt_zip_specify_one(self):
        input_classes = get_input_classes([NT_1_ZIP], NT, ZIP, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_nt_zip_specify_two(self):
        input_classes = get_input_classes([NT_1_ZIP], NT, ZIP, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_ttl_zip_all(self):
        input_classes = get_input_classes([TTL_1_ZIP], TURTLE, ZIP, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_ttl_zip_specify_one(self):
        input_classes = get_input_classes([TTL_1_ZIP], TURTLE, ZIP, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_ttl_zip_specify_two(self):
        input_classes = get_input_classes([TTL_1_ZIP], TURTLE, ZIP, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_owl_all(self):
        input_classes = get_input_classes([OWL_1], RDF_XML, None, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document'])

    def test_owl_specify_one(self):
        input_classes = get_input_classes([OWL_1], RDF_XML, None, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_owl_specify_two(self):
        input_classes = get_input_classes([OWL_1], RDF_XML, None, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_owl_gz_all(self):
        input_classes = get_input_classes([OWL_1_GZ], RDF_XML, GZ, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document'])

    def test_owl_gz_specify_one(self):
        input_classes = get_input_classes([OWL_1_GZ], RDF_XML, GZ, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_owl_gz_specify_two(self):
        input_classes = get_input_classes([OWL_1_GZ], RDF_XML, GZ, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_owl_zip_all(self):
        input_classes = get_input_classes([OWL_1_ZIP], RDF_XML, ZIP, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document'])

    def test_owl_zip_specify_one(self):
        input_classes = get_input_classes([OWL_1_ZIP], RDF_XML, ZIP, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_owl_zip_specify_two(self):
        input_classes = get_input_classes([OWL_1_ZIP], RDF_XML, ZIP, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_rdf_all(self):
        input_classes = get_input_classes([RDF_1], RDF_XML, None, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document'])

    def test_rdf_specify_one(self):
        input_classes = get_input_classes([RDF_1], RDF_XML, None, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_rdf_specify_two(self):
        input_classes = get_input_classes([RDF_1], RDF_XML, None, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_rdf_gz_all(self):
        input_classes = get_input_classes([RDF_1_GZ], RDF_XML, GZ, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document'])

    def test_rdf_gz_specify_one(self):
        input_classes = get_input_classes([RDF_1_GZ], RDF_XML, GZ, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_rdf_gz_specify_two(self):
        input_classes = get_input_classes([RDF_1_GZ], RDF_XML, GZ, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_rdf_zip_all(self):
        input_classes = get_input_classes([RDF_1_ZIP], RDF_XML, ZIP, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document'])

    def test_rdf_zip_specify_one(self):
        input_classes = get_input_classes([RDF_1_ZIP], RDF_XML, ZIP, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_rdf_zip_specify_two(self):
        input_classes = get_input_classes([RDF_1_ZIP], RDF_XML, ZIP, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_xml_all(self):
        input_classes = get_input_classes([XML_1], RDF_XML, None, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document'])

    def test_xml_specify_one(self):
        input_classes = get_input_classes([XML_1], RDF_XML, None, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_xml_specify_two(self):
        input_classes = get_input_classes([XML_1], RDF_XML, None, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_xml_gz_all(self):
        input_classes = get_input_classes([XML_1_GZ], RDF_XML, GZ, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document'])

    def test_xml_gz_specify_one(self):
        input_classes = get_input_classes([XML_1_GZ], RDF_XML, GZ, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_xml_gz_specify_two(self):
        input_classes = get_input_classes([XML_1_GZ], RDF_XML, GZ, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_xml_zip_all(self):
        input_classes = get_input_classes([XML_1_ZIP], RDF_XML, ZIP, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ['http://xmlns.com/foaf/0.1/Person', 'http://xmlns.com/foaf/0.1/Document'])

    def test_xml_zip_specify_one(self):
        input_classes = get_input_classes([XML_1_ZIP], RDF_XML, ZIP, ["http://xmlns.com/foaf/0.1/Person"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_xml_zip_specify_two(self):
        input_classes = get_input_classes([XML_1_ZIP], RDF_XML, ZIP, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

if __name__ == "__main__":
    unittest.main()