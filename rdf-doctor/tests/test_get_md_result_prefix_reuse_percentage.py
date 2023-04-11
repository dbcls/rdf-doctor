import unittest
from doctor import get_md_result_prefix_reuse_percentage
from shexer.consts import NT, TURTLE, GZ

class TestGetMdResultPrefixReusePercentage(unittest.TestCase):

    def test_get_md_result_prefix_reuse_percentage_nt(self):
        result = get_md_result_prefix_reuse_percentage("tests/test_files/test_nt_1.nt", NT, None)
        self.assertEqual(result, [
                                    '## Reuse percentage\n', \
                                    '```\n', \
                                    'Not calculated because there is no prefix defined.\n', \
                                    '```\n\n'])

    def test_get_md_result_prefix_reuse_percentage_ttl(self):
        result = get_md_result_prefix_reuse_percentage("tests/test_files/test_ttl_1.ttl", TURTLE, None)
        self.assertEqual(result, [
                                    '## Reuse percentage\n', \
                                    '```\n', \
                                    '100.0%\n', \
                                    '```\n\n'])

    def test_get_md_result_prefix_reuse_percentage_nt_gz(self):
        result = get_md_result_prefix_reuse_percentage("tests/test_files/test_nt_1.nt.gz", NT, GZ)
        self.assertEqual(result, [
                                    '## Reuse percentage\n', \
                                    '```\n', \
                                    'Not calculated because there is no prefix defined.\n', \
                                    '```\n\n'])

    def test_get_md_result_prefix_reuse_percentage_ttl_gz(self):
        result = get_md_result_prefix_reuse_percentage("tests/test_files/test_ttl_1.ttl.gz", TURTLE, GZ)
        self.assertEqual(result, [
                                    '## Reuse percentage\n', \
                                    '```\n', \
                                    '100.0%\n', \
                                    '```\n\n'])

if __name__ == "__main__":
    unittest.main()