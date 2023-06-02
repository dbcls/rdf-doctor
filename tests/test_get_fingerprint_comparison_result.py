import unittest
from doctor.doctor import get_fingerprint_comparison_result, get_input_classes, get_class_comparison_result
from tests.consts import NT_1, NT_2, TTL_2, TTL_3, CLASS_ERRATA_FILE_PATH
from shexer.consts import NT, TURTLE
from collections import defaultdict
from pathlib import Path

class TestGetFingerprintComparisonResult(unittest.TestCase):

    def test_nt_no_result(self):
        input_classes = get_input_classes(NT_1, NT, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list), str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH)))
        fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(fingerprint_comparison_result, [])


    def test_nt_with_result(self):
        input_classes = get_input_classes(NT_2, NT, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list), str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH)))
        fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(fingerprint_comparison_result, ['\nhttp://xmlns.com/foaf/0.1/Person', \
                                                        '\nhttp://xmlns.com/foaf/0.1/PErson', \
                                                        '\nhttp://xmlns.com/foaf/0.1#Person', \
                                                        '\n', \
                                                        '\nhttp://xmlns.com/foaf/0.1/Document', \
                                                        '\nhttp://xmlns.com/foaf/0.1#Document'])

    def test_ttl_no_result(self):
        input_classes = get_input_classes(TTL_2, TURTLE, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list), str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH)))
        fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(fingerprint_comparison_result, [])

    def test_ttl_with_result(self):
        input_classes = get_input_classes(TTL_3, TURTLE, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, defaultdict(list), str(Path(__file__).resolve().parent.joinpath(CLASS_ERRATA_FILE_PATH)))
        fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(fingerprint_comparison_result, ['\nhttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson', \
                                                        '\nhttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson', \
                                                        '\nhttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APERSON', \
                                                        '\n', \
                                                        '\nhttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADocument', \
                                                        '\nhttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADOCUMENT'])


if __name__ == "__main__":
    unittest.main()