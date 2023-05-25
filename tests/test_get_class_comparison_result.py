import unittest
from doctor.doctor import get_class_comparison_result, get_input_classes
from doctor.consts import TARGET_CLASS_ALL
from tests.consts import NT_2, TTL_2
from shexer.consts import NT, TURTLE
from collections import defaultdict

class TestGetClassComparisonResult(unittest.TestCase):

    def test_nt(self):
        input_classes = get_input_classes(NT_2, NT, None, [TARGET_CLASS_ALL])
        class_comparison_result, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list))
        self.assertEqual(class_comparison_result, ['http://xmlns.com/foaf/0.1/PErson\thttp://xmlns.com/foaf/0.1/Person\n', \
                                                    'http://xmlns.com/foaf/0.1#Person\thttp://xmlns.com/foaf/0.1/Person\n', \
                                                    'http://xmlns.com/foaf/0.1#Document\thttp://xmlns.com/foaf/0.1/Document\n'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01person'], ['http://xmlns.com/foaf/0.1/Person', \
                                                                                'http://xmlns.com/foaf/0.1/PErson', \
                                                                                'http://xmlns.com/foaf/0.1#Person'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01document'], ['http://xmlns.com/foaf/0.1/Document', \
                                                                                'http://xmlns.com/foaf/0.1#Document'])

    def test_ttl(self):
        input_classes = get_input_classes(TTL_2, TURTLE, None, [TARGET_CLASS_ALL])
        class_comparison_result, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list))
        self.assertEqual(class_comparison_result, ['http://xmlns.com/foaf/0.1#Person\thttp://xmlns.com/foaf/0.1/Person\n', \
                                                    'http://xmlns.com/foaf/0.1#Document\thttp://xmlns.com/foaf/0.1/Document\n'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01person'], ['http://xmlns.com/foaf/0.1#Person'])
        self.assertEqual(fingerprint_class_dict['httpxmlnscomfoaf01document'], ['http://xmlns.com/foaf/0.1#Document'])

if __name__ == "__main__":
    unittest.main()