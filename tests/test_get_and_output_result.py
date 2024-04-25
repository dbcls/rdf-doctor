import unittest
import argparse
import queue
import shutil
from doctor.doctor import get_and_output_result, get_widely_used_prefixes_dict, get_refine_prefix_uris, get_refine_class_uris
from doctor.consts import TARGET_CLASS_ALL
from tests.consts import NT_1, NT_1_GZ, NT_1_ZIP, NT_2, NT_2_GZ, NT_2_ZIP, NT_3, NT_3_GZ, TTL_1, TTL_1_GZ, TTL_1_ZIP, TTL_2, TTL_2_GZ, TTL_2_ZIP, TTL_3, TTL_3_GZ, TTL_3_ZIP, TTL_ERROR, OWL_1, OWL_1_GZ, OWL_1_ZIP, RDF_1, RDF_2, RDF_1_GZ, RDF_1_ZIP, XML_1, XML_1_GZ, XML_1_ZIP, REFINE_PREFIX_URIS_FILE_PATH, REFINE_CLASS_URIS_FILE_PATH, PREFIXES_FILE_PATH, REFINE_CLASS_URIS_ERROR_FILE_PATH, OUTPUT_DIR
from shexer.consts import NT, TURTLE, TURTLE_ITER, RDF_XML, GZ, ZIP
from pathlib import Path

# Since the order of the output of sheXer changes each time, only check that the result is list in the normal case.
class TestGetAndOutputResult(unittest.TestCase):

    def test_nt_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [NT_1, NT_2, NT_3]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[NT_1, NT_2, NT_3], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95),
                                        [input_file],
                                        NT,
                                        None,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(NT_1).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(NT_2).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(NT_3).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_nt_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[NT_1, NT_2, NT_3], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [NT_1, NT_2, NT_3],
                                    NT,
                                    None,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "n-triples.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_nt_gz_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [NT_1_GZ, NT_2_GZ, NT_3_GZ]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[NT_1_GZ, NT_2_GZ, NT_3_GZ], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95),
                                        [input_file],
                                        NT,
                                        GZ,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(NT_1_GZ).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(NT_2_GZ).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(NT_3_GZ).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_nt_gz_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[NT_1_GZ, NT_2_GZ, NT_3_GZ], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [NT_1_GZ, NT_2_GZ, NT_3_GZ],
                                    NT,
                                    GZ,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "n-triples.gz.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_nt_zip_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [NT_1_ZIP, NT_2_ZIP]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[NT_1_ZIP, NT_2_ZIP], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95),
                                        [input_file],
                                        NT,
                                        ZIP,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(NT_1_ZIP).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(NT_2_ZIP).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_nt_zip_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[NT_1_ZIP, NT_2_ZIP], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [NT_1_ZIP, NT_2_ZIP],
                                    NT,
                                    ZIP,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "n-triples.zip.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [TTL_1, TTL_2, TTL_3]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[TTL_1, TTL_2, TTL_3], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95),
                                        [input_file],
                                        TURTLE,
                                        None,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_1).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_2).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_3).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[TTL_1, TTL_2, TTL_3], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_1, TTL_2, TTL_3],
                                    TURTLE,
                                    None,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "turtle.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_gz_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [TTL_1_GZ, TTL_2_GZ, TTL_3_GZ]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95),
                                        [input_file],
                                        TURTLE,
                                        GZ,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_1_GZ).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_2_GZ).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_3_GZ).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_gz_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_1_GZ, TTL_2_GZ, TTL_3_GZ],
                                    TURTLE,
                                    GZ,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "turtle.gz.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_zip_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [TTL_1_ZIP, TTL_2_ZIP, TTL_3_ZIP]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[TTL_1_ZIP, TTL_2_ZIP, TTL_3_ZIP], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95),
                                        [input_file],
                                        TURTLE,
                                        ZIP,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_1_ZIP).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_2_ZIP).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_3_ZIP).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_zip_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[TTL_1_ZIP, TTL_2_ZIP, TTL_3_ZIP], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_1_ZIP, TTL_2_ZIP, TTL_3_ZIP],
                                    TURTLE,
                                    ZIP,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "turtle.zip.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_iter_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [TTL_1, TTL_2, TTL_3]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[TTL_1, TTL_2, TTL_3], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95, \
                                                force_format=TURTLE_ITER),
                                        [input_file],
                                        TURTLE,
                                        None,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_1).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_2).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_3).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_iter_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[TTL_1, TTL_2, TTL_3], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95, \
                                            force_format=TURTLE_ITER),
                                    [TTL_1, TTL_2, TTL_3],
                                    TURTLE,
                                    None,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "turtle.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_iter_gz_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [TTL_1_GZ, TTL_2_GZ, TTL_3_GZ]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95, \
                                                force_format=TURTLE_ITER),
                                        [input_file],
                                        TURTLE,
                                        GZ,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_1_GZ).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_2_GZ).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_3_GZ).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_iter_gz_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[TTL_1_GZ, TTL_2_GZ, TTL_3_GZ], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95, \
                                            force_format=TURTLE_ITER),
                                    [TTL_1_GZ, TTL_2_GZ, TTL_3_GZ],
                                    TURTLE,
                                    GZ,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "turtle.gz.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_iter_zip_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [TTL_1_ZIP, TTL_2_ZIP, TTL_3_ZIP]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[TTL_1_ZIP, TTL_2_ZIP, TTL_3_ZIP], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95, \
                                                force_format=TURTLE_ITER),
                                        [input_file],
                                        TURTLE,
                                        ZIP,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_1_ZIP).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_2_ZIP).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(TTL_3_ZIP).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_iter_zip_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[TTL_1_ZIP, TTL_2_ZIP, TTL_3_ZIP], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95, \
                                            force_format=TURTLE_ITER),
                                    [TTL_1_ZIP, TTL_2_ZIP, TTL_3_ZIP],
                                    TURTLE,
                                    ZIP,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "turtle.zip.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_rdf_xml_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [OWL_1, RDF_1, RDF_2, XML_1]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[OWL_1, RDF_1, RDF_2, XML_1], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95),
                                        [input_file],
                                        RDF_XML,
                                        None,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(OWL_1).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(RDF_1).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(RDF_2).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(XML_1).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_rdf_xml_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[OWL_1, RDF_1, RDF_2, XML_1], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [OWL_1, RDF_1, RDF_2, XML_1],
                                    RDF_XML,
                                    None,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "rdf_xml.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_rdf_xml_gz_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [OWL_1_GZ, RDF_1_GZ, XML_1_GZ]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[OWL_1_GZ, RDF_1_GZ, XML_1_GZ], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95),
                                        [input_file],
                                        RDF_XML,
                                        GZ,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(OWL_1_GZ).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(RDF_1_GZ).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(XML_1_GZ).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_gz_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[OWL_1_GZ, RDF_1_GZ, XML_1_GZ], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [OWL_1_GZ, RDF_1_GZ, XML_1_GZ],
                                    RDF_XML,
                                    GZ,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "rdf_xml.gz.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_zip_each(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        input_file_list = [OWL_1_ZIP, RDF_1_ZIP, XML_1_ZIP]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[OWL_1_ZIP, RDF_1_ZIP, XML_1_ZIP], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=True, \
                                                type=None, \
                                                merge=False, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95),
                                        [input_file],
                                        RDF_XML,
                                        ZIP,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR+str(Path(OWL_1_ZIP).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(RDF_1_ZIP).name)+".shex").exists())
        self.assertTrue(Path(OUTPUT_DIR+str(Path(XML_1_ZIP).name)+".shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_zip_merge(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[OWL_1_ZIP, RDF_1_ZIP, XML_1_ZIP], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [OWL_1_ZIP, RDF_1_ZIP, XML_1_ZIP],
                                    RDF_XML,
                                    ZIP,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "rdf_xml.zip.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_nt_report_false(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = None
        refine_class_uris = None
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[NT_1, NT_2, NT_3], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [NT_1, NT_2, NT_3],
                                    NT,
                                    None,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "n-triples.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_ttl_report_false(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = None
        refine_class_uris = None
        error_queue = queue.Queue()
        input_file_list = [TTL_1, TTL_2, TTL_3]
        for input_file in input_file_list:
            get_and_output_result(argparse.Namespace(input=[TTL_1, TTL_2, TTL_3], \
                                                output=OUTPUT_DIR, \
                                                classes=[TARGET_CLASS_ALL], \
                                                prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                                class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                                prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                                verbose=False, \
                                                report=False, \
                                                type=None, \
                                                merge=True, \
                                                tmp_dir=None, \
                                                tmp_dir_disk_usage_limit=95),
                                        [input_file],
                                        TURTLE,
                                        None,
                                        widely_used_prefixes_dict,
                                        refine_prefix_uris,
                                        refine_class_uris,
                                        error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "turtle.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_rdf_xml_report_false(self):
        shutil.rmtree(OUTPUT_DIR)
        Path(OUTPUT_DIR).mkdir(exist_ok=True)
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = None
        refine_class_uris = None
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[OWL_1, RDF_1, RDF_2, XML_1], \
                                            output=OUTPUT_DIR, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=False, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [OWL_1, RDF_1, RDF_2, XML_1],
                                    RDF_XML,
                                    None,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertTrue(Path(OUTPUT_DIR + "rdf_xml.shex").exists())
        self.assertTrue(error_queue.empty)

    def test_index_error(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_ERROR_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[TTL_2], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_ERROR_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            merge=True, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_2],
                                    TURTLE,
                                    None,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertEqual(str(error_queue.get()), str(IndexError("[ERROR] An index error occurred while processing [" + TTL_2 + "] Error message: list index out of range")))

    def test_value_error(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[TTL_3], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_3],
                                    "aaa",
                                    None,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertEqual(str(error_queue.get()), str(ValueError("[ERROR] A value error occurred while processing [" + TTL_3 + "] Error message: Invalid input format: aaa")))

    def test_exception_error(self):
        widely_used_prefixes_dict = get_widely_used_prefixes_dict(str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)))
        refine_prefix_uris = get_refine_prefix_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)))
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        error_queue = queue.Queue()
        get_and_output_result(argparse.Namespace(input=[TTL_ERROR], \
                                            output=None, \
                                            classes=[TARGET_CLASS_ALL], \
                                            prefix_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_PREFIX_URIS_FILE_PATH)), \
                                            class_uri_dict=str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)), \
                                            prefix_list=str(Path(__file__).resolve().parent.joinpath(PREFIXES_FILE_PATH)), \
                                            verbose=False, \
                                            report=True, \
                                            type=None, \
                                            tmp_dir=None, \
                                            tmp_dir_disk_usage_limit=95),
                                    [TTL_ERROR],
                                    TURTLE,
                                    None,
                                    widely_used_prefixes_dict,
                                    refine_prefix_uris,
                                    refine_class_uris,
                                    error_queue)

        self.assertEqual(str(error_queue.get()), str(Exception("[ERROR] An exception occurred while processing [" + TTL_ERROR + "] Error message: [Errno 2] No such file or directory: '/test_ttl_error.ttl'")))

if __name__ == "__main__":
    unittest.main()
