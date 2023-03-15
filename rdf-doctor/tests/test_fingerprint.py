import unittest
from doctor import fingerprint

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

if __name__ == "__main__":
    unittest.main()