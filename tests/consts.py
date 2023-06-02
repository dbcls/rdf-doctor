import os.path as path

BASE_DIR = path.join(path.dirname(path.normpath(__file__)), "test_files" + path.sep)
OUTPUT_DIR = BASE_DIR + "output" + path.sep

TTL_1 = BASE_DIR + "test_ttl_1.ttl"
TTL_1_GZ = BASE_DIR + "test_ttl_1.ttl.gz"
TTL_2 = BASE_DIR + "test_ttl_2.ttl"
TTL_3 = BASE_DIR + "test_ttl_3.ttl"

NT_1 = BASE_DIR + "test_nt_1.nt"
NT_1_GZ = BASE_DIR + "test_nt_1.nt.gz"
NT_2 = BASE_DIR + "test_nt_2.nt"
NT_3 = BASE_DIR + "test_nt_3.nt"

OUTPUT_NT_1_GZ_MD = OUTPUT_DIR + "test_nt_1_gz.md"
OUTPUT_NT_3_MD = OUTPUT_DIR + "test_nt_3.md"
OUTPUT_TTL_1_GZ_MD = OUTPUT_DIR + "test_ttl_1_gz.md"
OUTPUT_TTL_3_MD = OUTPUT_DIR + "test_ttl_3.md"

CLASS_ERRATA_FILE_PATH = "reference/refine-classes.tsv"
PREFIX_ERRATA_FILE_PATH = "reference/refine-prefixes.tsv"