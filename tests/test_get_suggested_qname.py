import unittest
from doctor.doctor import get_input_prefixes, get_correct_prefixes, get_suggested_qname
from tests.consts import NT_1, NT_1_GZ, NT_3, TTL_1, TTL_3, TTL_1_GZ
from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE, GZ, MIXED_INSTANCES

class TestGetSuggestedQName(unittest.TestCase):

    def test_nt_1(self):
        input_file = NT_1
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

    def test_nt_2(self):
        input_file = NT_3
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
        self.assertEqual(suggested_qname, ["Undefined\tobo:\thttp://purl.obolibrary.org/obo/\n", "Undefined\tuo:\thttp://purl.obolibrary.org/obo/\n"])

    def test_ttl_1(self):
        input_file = TTL_1
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

    def test_ttl_2(self):
        input_file = TTL_3
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
        self.assertEqual(suggested_qname, ["pobo:\tobo:\thttp://purl.obolibrary.org/obo/\n", "pobo:\tuo:\thttp://purl.obolibrary.org/obo/\n"])

    def test_nt_gz(self):
        input_file = NT_1_GZ
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

    def test_ttl_gz(self):
        input_file = TTL_1_GZ
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