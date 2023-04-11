import unittest
import rdflib
from doctor import get_md_result_prefix_errata, get_input_prefixes
from shexer.consts import NT, TURTLE

class TestGetMdResultClassErrata(unittest.TestCase):

    def test_get_md_result_prefix_errata_nt(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_nt_2.nt", NT, None)
        md_result_prefix_errata = get_md_result_prefix_errata(input_prefixes)
        self.assertEqual(md_result_prefix_errata, [])

    def test_get_md_result_prefix_errata_ttl(self):
        input_prefixes = get_input_prefixes("tests/test_files/test_ttl_2.ttl", TURTLE, None)
        md_result_prefix_errata = get_md_result_prefix_errata(input_prefixes)
        self.assertEqual(md_result_prefix_errata, ['## A prefix that appears to be incorrect was found.\n', \
                                                    '```\n', \
                                                    'Input\tCorrect\n', \
                                                    rdflib.term.URIRef('http://xmlns.com/foaf/0.1#\thttp://xmlns.com/foaf/0.1/\n'), \
                                                    '```\n\n'])

if __name__ == "__main__":
    unittest.main()