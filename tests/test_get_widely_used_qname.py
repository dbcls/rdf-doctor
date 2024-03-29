import unittest
from doctor.doctor import get_input_prefixes, get_widely_used_prefixes, get_widely_used_qname
from tests.consts import NT_1, NT_1_GZ, NT_3, TTL_1, TTL_3, TTL_1_GZ, PREFIXES_FILE_PATH
from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE, GZ, MIXED_INSTANCES
from pathlib import Path

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
        input_prefixes, _ = get_input_prefixes([input_file], None)
        widely_used_prefixes = get_widely_used_prefixes(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_qname = get_widely_used_qname(shaper_result, input_prefixes, widely_used_prefixes)
        self.assertEqual(widely_used_qname, ["Undefined\tex:\thttp://example.org/\n", \
                                            "Undefined\tex2:\thttp://example.org/\n"])

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
        input_prefixes, _ = get_input_prefixes([input_file], None)
        widely_used_prefixes = get_widely_used_prefixes(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_qname = get_widely_used_qname(shaper_result, input_prefixes, widely_used_prefixes)
        self.assertEqual(widely_used_qname, ["Undefined\tobo:\thttp://purl.obolibrary.org/obo/\n", \
                                            "Undefined\tuo:\thttp://purl.obolibrary.org/obo/\n"])

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
        input_prefixes, _ = get_input_prefixes([input_file], None)
        widely_used_prefixes = get_widely_used_prefixes(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_qname = get_widely_used_qname(shaper_result, input_prefixes, widely_used_prefixes)
        self.assertEqual(widely_used_qname, [])

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
        input_prefixes, _ = get_input_prefixes([input_file], None)
        widely_used_prefixes = get_widely_used_prefixes(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_qname = get_widely_used_qname(shaper_result, input_prefixes, widely_used_prefixes)
        self.assertEqual(widely_used_qname, ["pobo:\tobo:\thttp://purl.obolibrary.org/obo/\n", \
                                            "pobo:\tuo:\thttp://purl.obolibrary.org/obo/\n", \
                                            'oboc:\tchebi:\thttp://purl.obolibrary.org/obo/CHEBI_\n'])

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
        input_prefixes, _ = get_input_prefixes([input_file], GZ)
        widely_used_prefixes = get_widely_used_prefixes(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_qname = get_widely_used_qname(shaper_result, input_prefixes, widely_used_prefixes)
        self.assertEqual(widely_used_qname, ['Undefined\tex:\thttp://example.org/\n', \
                                            "Undefined\tex2:\thttp://example.org/\n"])

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
        input_prefixes, _ = get_input_prefixes([input_file], GZ)
        widely_used_prefixes = get_widely_used_prefixes(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_qname = get_widely_used_qname(shaper_result, input_prefixes, widely_used_prefixes)
        self.assertEqual(widely_used_qname, [])

if __name__ == "__main__":
    unittest.main()