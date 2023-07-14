import os.path as path

BASE_DIR = path.join(path.dirname(path.normpath(__file__)), "test_files" + path.sep)
OUTPUT_DIR = BASE_DIR + "output" + path.sep

# Turtle test files
TTL_1 = BASE_DIR + "test_ttl_1.ttl"
TTL_2 = BASE_DIR + "test_ttl_2.ttl"
TTL_3 = BASE_DIR + "test_ttl_3.ttl"
TTL_1_GZ = BASE_DIR + "test_ttl_1.ttl.gz"
TTL_2_GZ = BASE_DIR + "test_ttl_2.ttl.gz"
TTL_3_GZ = BASE_DIR + "test_ttl_3.ttl.gz"
TTL_ERROR = BASE_DIR + "test_ttl_error.ttl"

# N-Triples test files
NT_1 = BASE_DIR + "test_nt_1.nt"
NT_2 = BASE_DIR + "test_nt_2.nt"
NT_3 = BASE_DIR + "test_nt_3.nt"
NT_1_GZ = BASE_DIR + "test_nt_1.nt.gz"
NT_2_GZ = BASE_DIR + "test_nt_2.nt.gz"
NT_3_GZ = BASE_DIR + "test_nt_3.nt.gz"

OUTPUT_NT_3_MD = OUTPUT_DIR + "test_nt_3.md"
OUTPUT_NT_1_2_3_MD = OUTPUT_DIR + "test_nt_1_2_3.md"
OUTPUT_NT_1_2_3_CLASS_1_MD = OUTPUT_DIR + "test_nt_1_2_3_class_1.md"
OUTPUT_NT_1_2_3_CLASS_2_MD = OUTPUT_DIR + "test_nt_1_2_3_class_2.md"
OUTPUT_NT_1_2_3_CLASS_3_MD = OUTPUT_DIR + "test_nt_1_2_3_class_3.md"
OUTPUT_NT_1_2_3_CLASS_4_MD = OUTPUT_DIR + "test_nt_1_2_3_class_4.md"
OUTPUT_NT_1_2_3_CLASS_5_MD = OUTPUT_DIR + "test_nt_1_2_3_class_5.md"
OUTPUT_NT_1_GZ_MD = OUTPUT_DIR + "test_nt_1_gz.md"
OUTPUT_NT_1_2_3_GZ_MD = OUTPUT_DIR + "test_nt_1_2_3_gz.md"

OUTPUT_TTL_3_MD = OUTPUT_DIR + "test_ttl_3.md"
OUTPUT_TTL_3_CLASS_1_MD = OUTPUT_DIR + "test_ttl_3_class_1.md"
OUTPUT_TTL_3_CLASS_2_MD = OUTPUT_DIR + "test_ttl_3_class_2.md"
OUTPUT_TTL_3_CLASS_3_MD = OUTPUT_DIR + "test_ttl_3_class_3.md"
OUTPUT_TTL_3_CLASS_4_MD = OUTPUT_DIR + "test_ttl_3_class_4.md"
OUTPUT_TTL_3_CLASS_5_MD = OUTPUT_DIR + "test_ttl_3_class_5.md"
OUTPUT_TTL_1_GZ_MD = OUTPUT_DIR + "test_ttl_1_gz.md"
OUTPUT_TTL_1_2_3_MD = OUTPUT_DIR + "test_ttl_1_2_3.md"
OUTPUT_TTL_1_2_3_GZ_MD = OUTPUT_DIR + "test_ttl_1_2_3_gz.md"

PREFIXES_FILE_PATH = "reference/prefixes.tsv"
PREFIXES_ERROR_FILE_PATH = "reference/prefixes-error.tsv"
REFINE_CLASS_URIS_FILE_PATH = "reference/refine-class-uris.tsv"
REFINE_CLASS_URIS_ERROR_FILE_PATH = "reference/refine-class-uris-error.tsv"
REFINE_PREFIX_URIS_FILE_PATH = "reference/refine-prefix-uris.tsv"
REFINE_PREFIX_URIS_ERROR_FILE_PATH = "reference/refine-prefix-uris-error.tsv"
