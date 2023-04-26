import unittest
from doctor.doctor import get_prefix_comparison_result, get_input_prefixes
from shexer.consts import NT, TURTLE

class TestGetMdResultClassErrata(unittest.TestCase):

    def test_get_prefix_comparison_result_nt(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_nt_2.nt", None)
        prefix_comparison_result = get_prefix_comparison_result(input_prefixes)
        self.assertEqual(prefix_comparison_result, [])

    def test_get_prefix_comparison_result_ttl(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_ttl_3.ttl", None)
        prefix_comparison_result = get_prefix_comparison_result(input_prefixes)
        self.assertEqual(prefix_comparison_result, ['chebi:\thttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A\thttp://purl.obolibrary.org/obo/CHEBI_\n'])

if __name__ == "__main__":
    unittest.main()