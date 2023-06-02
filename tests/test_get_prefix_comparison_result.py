import unittest
from doctor.doctor import get_prefix_comparison_result, get_input_prefixes
from tests.consts import NT_1, TTL_3, PREFIX_ERRATA_FILE_PATH
from pathlib import Path

class TestGetPrefixComparisonResult(unittest.TestCase):

    def test_nt(self):
        input_prefixes = get_input_prefixes(NT_1, None)
        prefix_comparison_result = get_prefix_comparison_result(input_prefixes, str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)))
        self.assertEqual(prefix_comparison_result, [])

    def test_ttl(self):
        input_prefixes = get_input_prefixes(TTL_3, None)
        prefix_comparison_result = get_prefix_comparison_result(input_prefixes, str(Path(__file__).resolve().parent.joinpath(PREFIX_ERRATA_FILE_PATH)))
        self.assertEqual(prefix_comparison_result, ['chebi:\thttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A\thttp://purl.obolibrary.org/obo/CHEBI_\n'])

if __name__ == "__main__":
    unittest.main()