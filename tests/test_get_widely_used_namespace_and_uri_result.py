import unittest
from doctor.doctor import get_input_prefixes_turtle, get_input_prefixes_rdf_xml, get_widely_used_prefixes_dict, get_refine_prefix_uris, get_widely_used_namespace_and_uri_result
from tests.consts import NT_1, NT_1_GZ, NT_1_ZIP, NT_3, TTL_1, TTL_1_GZ, TTL_1_ZIP, TTL_3, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP, PREFIXES_FILE_PATH, REFINE_PREFIX_URIS_FILE_PATH
from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE, RDF_XML, GZ, ZIP, MIXED_INSTANCES
from pathlib import Path

class TestGetWidelyUsedNamespaceAndUriResult(unittest.TestCase):

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
        input_prefixes, _, _ = get_input_prefixes_turtle([input_file], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, refine_prefix_uris)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

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
        input_prefixes, _, _ = get_input_prefixes_turtle([input_file], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, refine_prefix_uris)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://purl.obolibrary.org/obo/\tobo:|uo:\t\n'])

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
        input_prefixes, _, _ = get_input_prefixes_turtle([input_file], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

    def test_nt_zip(self):
        input_file = NT_1_ZIP
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=NT,
                        compression_mode=ZIP,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_turtle([input_file], ZIP)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

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
        input_prefixes, _, _ = get_input_prefixes_turtle([input_file], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        self.assertEqual(widely_used_namespace_and_uri, [])

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
        input_prefixes, _, _ = get_input_prefixes_turtle([input_file], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        self.assertEqual(widely_used_namespace_and_uri, ['pobo:\thttp://purl.obolibrary.org/obo/\tobo:|uo:\t\n', \
                                                        'oboc:\thttp://purl.obolibrary.org/obo/CHEBI_\tchebi:\t\n', \
                                                        'chebi:\thttp://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A\t\thttp://purl.obolibrary.org/obo/CHEBI_\n'])

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
        input_prefixes, _, _ = get_input_prefixes_turtle([input_file], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, [])

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
        input_prefixes, _, _ = get_input_prefixes_turtle([input_file], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, [])

    def test_ttl_zip(self):
        input_file = TTL_1_ZIP
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=TURTLE,
                        compression_mode=ZIP,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_turtle([input_file], ZIP)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, [])

    def test_owl_1(self):
        input_file = OWL_1
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=RDF_XML,
                        compression_mode=None,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_rdf_xml([input_file], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

    def test_owl_1_gz(self):
        input_file = OWL_1_GZ
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=RDF_XML,
                        compression_mode=GZ,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_rdf_xml([input_file], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

    def test_owl_1_zip(self):
        input_file = OWL_1_ZIP
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=RDF_XML,
                        compression_mode=ZIP,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_rdf_xml([input_file], ZIP)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

    def test_rdf_1(self):
        input_file = RDF_1
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=RDF_XML,
                        compression_mode=None,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_rdf_xml([input_file], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

    def test_rdf_1_gz(self):
        input_file = RDF_1_GZ
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=RDF_XML,
                        compression_mode=GZ,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_rdf_xml([input_file], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

    def test_rdf_1_zip(self):
        input_file = RDF_1_ZIP
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=RDF_XML,
                        compression_mode=ZIP,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_rdf_xml([input_file], ZIP)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

    def test_xml_1(self):
        input_file = XML_1
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=RDF_XML,
                        compression_mode=None,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_rdf_xml([input_file], None)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

    def test_xml_1_gz(self):
        input_file = XML_1_GZ
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=RDF_XML,
                        compression_mode=GZ,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_rdf_xml([input_file], GZ)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])

    def test_xml_1_zip(self):
        input_file = XML_1_ZIP
        shaper = Shaper(graph_file_input=input_file,
                        target_classes=None,
                        all_classes_mode=True,
                        input_format=RDF_XML,
                        compression_mode=ZIP,
                        instances_report_mode=MIXED_INSTANCES,
                        detect_minimal_iri=True)

        shaper_result = shaper.shex_graph(string_output=True)
        input_prefixes, _, _ = get_input_prefixes_rdf_xml([input_file], ZIP)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        widely_used_namespace_and_uri = get_widely_used_namespace_and_uri_result(shaper_result, input_prefixes, widely_used_prefixes_dict, str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        print(widely_used_namespace_and_uri)
        self.assertEqual(widely_used_namespace_and_uri, ['Undefined\thttp://example.org/\tex:|ex2:\t\n'])


if __name__ == "__main__":
    unittest.main()