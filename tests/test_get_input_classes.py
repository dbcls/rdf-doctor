import unittest
from doctor.doctor import get_input_classes
from doctor.consts import TARGET_CLASS_ALL
from tests.consts import NT_1, NT_1_GZ, TTL_1, TTL_1_GZ
from shexer.consts import NT, TURTLE, GZ

class TestGetClassesList(unittest.TestCase):

    def test_nt_all(self):
        input_classes = get_input_classes(NT_1, NT, None, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_nt_specify_one(self):
        input_classes = get_input_classes(NT_1, NT, None, ["<http://xmlns.com/foaf/0.1/Person>"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_nt_specify_two(self):
        input_classes = get_input_classes(NT_1, NT, None, ["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_ttl_all(self):
        input_classes = get_input_classes(TTL_1, TURTLE, None, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_ttl_specify_one(self):
        input_classes = get_input_classes(TTL_1, TURTLE, None, ["<http://xmlns.com/foaf/0.1/Person>"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_ttl_specify_two(self):
        input_classes = get_input_classes(TTL_1, TURTLE, None, ["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_nt_gz_all(self):
        input_classes = get_input_classes(NT_1_GZ, NT, GZ, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_nt_gz_specify_one(self):
        input_classes = get_input_classes(NT_1_GZ, NT, GZ, ["<http://xmlns.com/foaf/0.1/Person>"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_nt_gz_specify_two(self):
        input_classes = get_input_classes(NT_1_GZ, NT, GZ, ["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_ttl_gz_all(self):
        input_classes = get_input_classes(TTL_1_GZ, TURTLE, GZ, [TARGET_CLASS_ALL])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

    def test_ttl_gz_specify_one(self):
        input_classes = get_input_classes(TTL_1_GZ, TURTLE, GZ, ["<http://xmlns.com/foaf/0.1/Person>"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person"])

    def test_ttl_gz_specify_two(self):
        input_classes = get_input_classes(TTL_1_GZ, TURTLE, GZ, ["<http://xmlns.com/foaf/0.1/Person>", "<http://xmlns.com/foaf/0.1/Document>"])
        self.assertEqual(input_classes, ["http://xmlns.com/foaf/0.1/Person", "http://xmlns.com/foaf/0.1/Document"])

if __name__ == "__main__":
    unittest.main()