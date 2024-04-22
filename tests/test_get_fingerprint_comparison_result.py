import unittest
from doctor.doctor import get_fingerprint_comparison_result, get_input_classes, get_class_comparison_result
from tests.consts import NT_1, NT_2, TTL_1, TTL_2, TTL_3, REFINE_CLASS_URIS_FILE_PATH
from shexer.consts import NT, TURTLE
from pathlib import Path

class TestGetFingerprintComparisonResult(unittest.TestCase):

    def test_no_result_1(self):
        input_classes = get_input_classes([NT_1], NT, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(fingerprint_comparison_result, [])

    def test_no_result_2(self):
        input_classes = get_input_classes([TTL_2], TURTLE, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(fingerprint_comparison_result, [])

    def test_with_result_1(self):
        input_classes = get_input_classes([NT_2], NT, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(fingerprint_comparison_result, ['http://xmlns.com/foaf/0.1/Person', \
                                                        '\n# http://xmlns.com/foaf/0.1/PErson', \
                                                        '\n# http://xmlns.com/foaf/0.1#Person', \
                                                        '\n# ', \
                                                        '\n# http://xmlns.com/foaf/0.1/Document', \
                                                        '\n# http://xmlns.com/foaf/0.1#Document'])

    def test_with_result_2(self):
        input_classes = get_input_classes([TTL_1, TTL_2, TTL_3], TURTLE, None, ["all"])
        _, fingerprint_class_dict = get_class_comparison_result(input_classes, str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        fingerprint_comparison_result = get_fingerprint_comparison_result(fingerprint_class_dict)
        self.assertEqual(fingerprint_comparison_result, ['http://xmlns.com/foaf/0.1/Person', \
                                                        '\n# http://xmlns.com/foaf/0.1#Person', \
                                                        '\n# ', \
                                                        '\n# http://xmlns.com/foaf/0.1/Document', \
                                                        '\n# http://xmlns.com/foaf/0.1#Document', \
                                                        '\n# ', \
                                                        '\n# http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson', \
                                                        '\n# http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson', \
                                                        '\n# http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APERSON', \
                                                        '\n# ', \
                                                        '\n# http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADocument', \
                                                        '\n# http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADOCUMENT'])


if __name__ == "__main__":
    unittest.main()