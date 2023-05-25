import unittest
from doctor.doctor import fingerprint

class TestFingerPrint(unittest.TestCase):

    def test_finger_print(self):
        result1 = fingerprint("http://xmlns.com/foaf/0.1/Document")
        result2 = fingerprint("http://XMLNS.com/FOAF/0.1/DOCUMENT")
        result3 = fingerprint("http://xmlns.com/foaf/0.1#Document")
        result4 = fingerprint("http://xmlns.com/foaf/0.1/Person")
        result5 = fingerprint("http://XMLNS.com/FOAF/0.1/PERSON")
        result6 = fingerprint("http://xmlns.com/foaf/0.1#Person")
        self.assertEqual(result1, "httpxmlnscomfoaf01document")
        self.assertEqual(result2, "httpxmlnscomfoaf01document")
        self.assertEqual(result3, "httpxmlnscomfoaf01document")
        self.assertEqual(result4, "httpxmlnscomfoaf01person")
        self.assertEqual(result5, "httpxmlnscomfoaf01person")
        self.assertEqual(result6, "httpxmlnscomfoaf01person")

if __name__ == "__main__":
    unittest.main()