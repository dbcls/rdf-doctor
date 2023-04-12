import unittest
from doctor import get_md_result_class_errata, get_input_classes
from shexer.consts import NT, TURTLE, GZ
from collections import defaultdict

class TestGetMdResultClassErrata(unittest.TestCase):

    def test_get_md_result_class_errata_nt(self):
        input_classes = get_input_classes("tests/test_files/test_nt_2.nt", TURTLE, None, ["all"])
        md_result_class_errata, fingerprint_class_dict = get_md_result_class_errata(input_classes, defaultdict(list))
        self.assertEqual(md_result_class_errata, ['## Found a class name that looks incorrect.\n', \
                                                    '```\n', \
                                                    'Input class name\tSuggested class name\n', \
                                                    'http://xmlns.com/foaf/0.1/PErson\thttp://xmlns.com/foaf/0.1/Person\n', \
                                                    'http://xmlns.com/foaf/0.1#Person\thttp://xmlns.com/foaf/0.1/Person\n', \
                                                    'http://xmlns.com/foaf/0.1#Document\thttp://xmlns.com/foaf/0.1/Document\n', \
                                                    '```\n\n'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01person'], ['http://xmlns.com/foaf/0.1/Person', \
                                                                                'http://xmlns.com/foaf/0.1/PErson', \
                                                                                'http://xmlns.com/foaf/0.1#Person'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01document'], ['http://xmlns.com/foaf/0.1/Document', \
                                                                                'http://xmlns.com/foaf/0.1#Document'])

    def test_get_md_result_class_errata_ttl(self):
        input_classes = get_input_classes("tests/test_files/test_ttl_2.ttl", TURTLE, None, ["all"])
        md_result_class_errata, fingerprint_class_dict = get_md_result_class_errata(input_classes, defaultdict(list))
        self.assertEqual(md_result_class_errata, ['## Found a class name that looks incorrect.\n', \
                                                    '```\n', \
                                                    'Input class name\tSuggested class name\n', \
                                                    'http://xmlns.com/foaf/0.1#Person\thttp://xmlns.com/foaf/0.1/Person\n', \
                                                    'http://xmlns.com/foaf/0.1#Document\thttp://xmlns.com/foaf/0.1/Document\n', \
                                                    '```\n\n'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01person'], ['http://xmlns.com/foaf/0.1#Person'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01document'], ['http://xmlns.com/foaf/0.1#Document'])

if __name__ == "__main__":
    unittest.main()