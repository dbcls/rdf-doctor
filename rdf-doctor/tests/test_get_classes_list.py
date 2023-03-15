import unittest
from doctor import get_classes_list

class TestGetClassesList(unittest.TestCase):

    def test_get_classes_list_nt(self):
        classes_list = get_classes_list("rdf-doctor/tests/test_files/test_nt_1.nt", "nt")
        self.assertEqual(classes_list, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_get_classes_list_ttl(self):
        classes_list = get_classes_list("rdf-doctor/tests/test_files/test_ttl_1.ttl", "turtle")
        self.assertEqual(classes_list, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

if __name__ == "__main__":
    unittest.main()