import unittest
from doctor.doctor import fingerprint

class TestFingerPrint(unittest.TestCase):

    def test_fingerprint_1(self):
        result = fingerprint("http://xmlns.com/foaf/0.1/Document")
        self.assertEqual(result, "httpxmlnscomfoaf01document")

    def test_fingerprint_2(self):
        result = fingerprint("http://xmlns.com/foaf/0.1/DOCUMENT")
        self.assertEqual(result, "httpxmlnscomfoaf01document")

    def test_fingerprint_3(self):
        result = fingerprint("http://xmlns.com/foaf/0.1#Document")
        self.assertEqual(result, "httpxmlnscomfoaf01document")

    def test_fingerprint_4(self):
        result = fingerprint("http://xmlns.com/foaf/0.1/Person")
        self.assertEqual(result, "httpxmlnscomfoaf01person")

    def test_fingerprint_5(self):
        result = fingerprint("http://xmlns.com/foaf/0.1/PERSON")
        self.assertEqual(result, "httpxmlnscomfoaf01person")

    def test_fingerprint_6(self):
        result = fingerprint("http://xmlns.com/foaf/0.1#Person")
        self.assertEqual(result, "httpxmlnscomfoaf01person")

if __name__ == "__main__":
    unittest.main()