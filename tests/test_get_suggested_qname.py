import unittest
from doctor.doctor import get_input_prefixes, get_correct_prefixes, get_suggested_qname
from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE, GZ, MIXED_INSTANCES

class TestGetSuggestedQName(unittest.TestCase):

    def test_get_sugggested_qname_nt(self):
        input_file = "tests/test_files/test_nt_1.nt"
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=NT,
                        compression_mode=None,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes = get_input_prefixes(input_file, None)
        correct_prefixes = get_correct_prefixes()
        suggested_qname = get_suggested_qname(shaper_result, input_prefixes, correct_prefixes)
        self.assertEqual(suggested_qname, ["Undefined\tex:\thttp://example.org/\n"])

    def test_get_sugggested_qname_ttl(self):
        input_file = "tests/test_files/test_ttl_1.ttl"
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=TURTLE,
                        compression_mode=None,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes = get_input_prefixes(input_file, None)
        correct_prefixes = get_correct_prefixes()
        suggested_qname = get_suggested_qname(shaper_result, input_prefixes, correct_prefixes)
        self.assertEqual(suggested_qname, [])

    def test_get_sugggested_qname_nt_gz(self):
        input_file = "tests/test_files/test_nt_1.nt.gz"
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=NT,
                        compression_mode=GZ,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes = get_input_prefixes(input_file, GZ)
        correct_prefixes = get_correct_prefixes()
        suggested_qname = get_suggested_qname(shaper_result, input_prefixes, correct_prefixes)
        self.assertEqual(suggested_qname, ['Undefined\tex:\thttp://example.org/\n'])

    def test_get_sugggested_qname_ttl_gz(self):
        input_file = "tests/test_files/test_ttl_1.ttl.gz"
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=TURTLE,
                        compression_mode=GZ,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes = get_input_prefixes(input_file, GZ)
        correct_prefixes = get_correct_prefixes()
        suggested_qname = get_suggested_qname(shaper_result, input_prefixes, correct_prefixes)
        self.assertEqual(suggested_qname, [])

if __name__ == "__main__":
    unittest.main()