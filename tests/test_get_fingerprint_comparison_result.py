import unittest
from doctor.doctor import get_fingerprint_comparison_result, get_input_classes, get_class_comparison_result
from shexer.consts import NT, TURTLE
from collections import defaultdict

class TestGetMdResultClassFingerprint(unittest.TestCase):

    def test_get_fingerprint_comparison_result_nt_1(self):
        input_classes = get_input_classes("tests/test_files/test_nt_1.nt", NT, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list))
        md_result_class_fingerprint = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(md_result_class_fingerprint, [])


    def test_get_fingerprint_comparison_result_nt_2(self):
        input_classes = get_input_classes("tests/test_files/test_nt_2.nt", NT, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list))
        md_result_class_fingerprint = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(md_result_class_fingerprint, ['\nhttp://xmlns.com/foaf/0.1/Person', \
                                                        '\nhttp://xmlns.com/foaf/0.1/PErson', \
                                                        '\nhttp://xmlns.com/foaf/0.1#Person', \
                                                        '\n', \
                                                        '\nhttp://xmlns.com/foaf/0.1/Document', \
                                                        '\nhttp://xmlns.com/foaf/0.1#Document'])

    def test_get_fingerprint_comparison_result_ttl_1(self):
        input_classes = get_input_classes("tests/test_files/test_ttl_2.ttl", TURTLE, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list))
        md_result_class_fingerprint = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(md_result_class_fingerprint, [])

    def test_get_fingerprint_comparison_result_ttl_2(self):
        input_classes = get_input_classes("tests/test_files/test_ttl_3.ttl", TURTLE, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list))
        md_result_class_fingerprint = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(md_result_class_fingerprint, ['\nhttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson', \
                                                        '\nhttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson', \
                                                        '\nhttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APERSON', \
                                                        '\n', \
                                                        '\nhttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADocument', \
                                                        '\nhttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADOCUMENT'])


if __name__ == "__main__":
    unittest.main()