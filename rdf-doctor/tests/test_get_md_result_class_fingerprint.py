import unittest
from doctor import get_md_result_class_fingerprint, get_input_classes, get_md_result_class_errata
from shexer.consts import NT, TURTLE
from collections import defaultdict

class TestGetMdResultClassFingerprint(unittest.TestCase):

    def test_get_md_result_class_fingerprint_nt(self):
        input_classes = get_input_classes("tests/test_files/test_nt_2.nt", NT, None, ["all"])
        _, fingerprint_class_dict = get_md_result_class_errata(input_classes, defaultdict(list))
        md_result_class_fingerprint = get_md_result_class_fingerprint(fingerprint_class_dict)
        self.assertEqual(md_result_class_fingerprint, ['## Multiple strings were found that appear to represent the same class name.\n', \
                                                '```', '\nhttp://xmlns.com/foaf/0.1/Person', \
                                                '\nhttp://xmlns.com/foaf/0.1/PErson', \
                                                '\nhttp://xmlns.com/foaf/0.1#Person', \
                                                '\n', \
                                                '\nhttp://xmlns.com/foaf/0.1/Document', \
                                                '\nhttp://xmlns.com/foaf/0.1#Document', \
                                                '\n```\n\n'])

    def test_get_md_result_class_fingerprint_ttl(self):
        input_classes = get_input_classes("tests/test_files/test_ttl_2.ttl", TURTLE, None, ["all"])
        _, fingerprint_class_dict = get_md_result_class_errata(input_classes, defaultdict(list))
        md_result_class_fingerprint = get_md_result_class_fingerprint(fingerprint_class_dict)
        self.assertEqual(md_result_class_fingerprint, [])

if __name__ == "__main__":
    unittest.main()