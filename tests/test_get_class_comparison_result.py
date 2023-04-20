import unittest
from doctor.doctor import get_class_comparison_result, get_input_classes
from shexer.consts import NT, TURTLE, GZ
from collections import defaultdict

class TestGetMdResultClassErrata(unittest.TestCase):

    def test_get_class_comparison_result_nt(self):
        input_classes = get_input_classes("tests/test_files/test_nt_2.nt", TURTLE, None, ["all"])
        md_result_class_errata, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list))
        self.assertEqual(md_result_class_errata, ['http://xmlns.com/foaf/0.1/PErson\thttp://xmlns.com/foaf/0.1/Person\n', \
                                                    'http://xmlns.com/foaf/0.1#Person\thttp://xmlns.com/foaf/0.1/Person\n', \
                                                    'http://xmlns.com/foaf/0.1#Document\thttp://xmlns.com/foaf/0.1/Document\n'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01person'], ['http://xmlns.com/foaf/0.1/Person', \
                                                                                'http://xmlns.com/foaf/0.1/PErson', \
                                                                                'http://xmlns.com/foaf/0.1#Person'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01document'], ['http://xmlns.com/foaf/0.1/Document', \
                                                                                'http://xmlns.com/foaf/0.1#Document'])

    def test_get_class_comparison_result_ttl(self):
        input_classes = get_input_classes("tests/test_files/test_ttl_2.ttl", TURTLE, None, ["all"])
        md_result_class_errata, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list))
        self.assertEqual(md_result_class_errata, ['http://xmlns.com/foaf/0.1#Person\thttp://xmlns.com/foaf/0.1/Person\n', \
                                                    'http://xmlns.com/foaf/0.1#Document\thttp://xmlns.com/foaf/0.1/Document\n'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01person'], ['http://xmlns.com/foaf/0.1#Person'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01document'], ['http://xmlns.com/foaf/0.1#Document'])

if __name__ == "__main__":
    unittest.main()