import unittest
from pathlib import Path
from doctor.doctor import get_widely_used_prefixes_dict, get_refine_prefix_uris, get_suggest_string_for_widely_used_namespace_and_uri
from tests.consts import PREFIXES_FILE_PATH, REFINE_PREFIX_URIS_FILE_PATH

class TestGetSuggestStringForWidelyUsedNamespaceAndUri(unittest.TestCase):

    def test_chebi(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        suggest_string = get_suggest_string_for_widely_used_namespace_and_uri("oboc:", "http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A", widely_used_prefixes_dict, refine_prefix_uris)
        self.assertEqual(suggest_string, "oboc:\thttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A\tchebi:\thttp://purl.obolibrary.org/obo/CHEBI_\n")


if __name__ == "__main__":
    unittest.main()