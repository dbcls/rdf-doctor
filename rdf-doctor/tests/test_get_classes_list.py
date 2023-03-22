import unittest
from doctor import get_classes_list
from shexer.consts import NT, TURTLE, GZ

class TestGetClassesList(unittest.TestCase):

    def test_get_classes_list_nt(self):
        classes_list = get_classes_list("tests/test_files/test_nt_1.nt", NT, None)
        self.assertEqual(classes_list, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_get_classes_list_ttl(self):
        classes_list = get_classes_list("tests/test_files/test_ttl_1.ttl", TURTLE, None)
        self.assertEqual(classes_list, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_get_classes_list_nt_gz(self):
        classes_list = get_classes_list("tests/test_files/test_nt_1.nt.gz", NT, GZ)
        self.assertEqual(classes_list, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_get_classes_list_ttl_gz(self):
        classes_list = get_classes_list("tests/test_files/test_ttl_1.ttl.gz", TURTLE, GZ)
        self.assertEqual(classes_list, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

if __name__ == "__main__":
    unittest.main()