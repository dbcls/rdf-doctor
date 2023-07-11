import unittest
from doctor.doctor import get_refine_prefix_uris
from tests.consts import REFINE_PREFIX_URIS_FILE_PATH
from pathlib import Path

class TestGetRefinePrefixUris(unittest.TestCase):

    def test_get_refine_prefix_uris(self):
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        self.assertEqual(refine_prefix_uris, [['http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A', 'http://purl.obolibrary.org/obo/CHEBI_'], \
                                                ['http://identifiers.org/dbsnp/', 'https://identifiers.org/dbsnp:'], \
                                                ['http://identifiers.org/dbsnp', 'https://identifiers.org/dbsnp:'], \
                                                ['http://purl.jp/bio/10/dbsnp/', 'https://identifiers.org/dbsnp:'], \
                                                ['http://identifiers.org/chebi/CHEBI:', 'http://purl.obolibrary.org/obo/CHEBI_'], \
                                                ['http://purl.obolibrary.org/obo/chebi/', 'http://purl.obolibrary.org/obo/CHEBI_'], \
                                                ['http://purl.obolibrary.org/obo/chebi.', 'http://purl.obolibrary.org/obo/CHEBI_'], \
                                                ['http://purl.obolibrary.org/obo/chebi#', 'http://purl.obolibrary.org/obo/CHEBI_']])

if __name__ == "__main__":
    unittest.main()