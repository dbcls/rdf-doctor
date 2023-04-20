import unittest
from doctor.doctor import get_input_classes
from shexer.consts import NT, TURTLE, GZ

class TestGetClassesList(unittest.TestCase):

    def test_get_input_classes_nt(self):
        input_classes = get_input_classes("tests/test_files/test_nt_1.nt", NT, None, ["all"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_get_input_classes_ttl(self):
        input_classes = get_input_classes("tests/test_files/test_ttl_1.ttl", TURTLE, None, ["all"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_get_input_classes_nt_gz(self):
        input_classes = get_input_classes("tests/test_files/test_nt_1.nt.gz", NT, GZ, ["all"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_get_input_classes_ttl_gz(self):
        input_classes = get_input_classes("tests/test_files/test_ttl_1.ttl.gz", TURTLE, GZ, ["all"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

if __name__ == "__main__":
    unittest.main()