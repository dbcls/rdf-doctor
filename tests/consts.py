import os.path as path

# Directories for testing
BASE_DIR = path.join(path.dirname(path.normpath(__file__)), "test_files" + path.sep)
OUTPUT_DIR = BASE_DIR + "output" + path.sep
DIR_INPUT_TEST_DIR_TTL = BASE_DIR + "dir_input_test_turtle"
DIR_INPUT_TEST_DIR_NT = BASE_DIR + "dir_input_test_nt"
DIR_INPUT_TEST_DIR_RDF_XML = BASE_DIR + "dir_input_test_rdf_xml"

# Turtle test files
TTL_1 = BASE_DIR + "test_ttl_1.ttl"
TTL_2 = BASE_DIR + "test_ttl_2.ttl"
TTL_3 = BASE_DIR + "test_ttl_3.ttl"
TTL_1_GZ = BASE_DIR + "test_ttl_1.ttl.gz"
TTL_2_GZ = BASE_DIR + "test_ttl_2.ttl.gz"
TTL_3_GZ = BASE_DIR + "test_ttl_3.ttl.gz"
TTL_1_ZIP = BASE_DIR + "test_ttl_1.ttl.zip"
TTL_2_ZIP = BASE_DIR + "test_ttl_2.ttl.zip"
TTL_3_ZIP = BASE_DIR + "test_ttl_3.ttl.zip"
TTL_ERROR = "/test_ttl_error.ttl"

# N-Triples test files
NT_1 = BASE_DIR + "test_nt_1.nt"
NT_2 = BASE_DIR + "test_nt_2.nt"
NT_3 = BASE_DIR + "test_nt_3.nt"
NT_1_GZ = BASE_DIR + "test_nt_1.nt.gz"
NT_2_GZ = BASE_DIR + "test_nt_2.nt.gz"
NT_3_GZ = BASE_DIR + "test_nt_3.nt.gz"
NT_1_ZIP = BASE_DIR + "test_nt_1.nt.zip"
NT_2_ZIP = BASE_DIR + "test_nt_2.nt.zip"

# RDF/XML test files
OWL_1 = BASE_DIR + "test_owl_1.owl"
RDF_1 = BASE_DIR + "test_rdf_1.rdf"
RDF_2 = BASE_DIR + "test_rdf_2.rdf"
XML_1 = BASE_DIR + "test_xml_1.xml"
OWL_1_GZ = BASE_DIR + "test_owl_1.owl.gz"
RDF_1_GZ = BASE_DIR + "test_rdf_1.rdf.gz"
XML_1_GZ = BASE_DIR + "test_xml_1.xml.gz"
OWL_1_ZIP = BASE_DIR + "test_owl_1.owl.zip"
RDF_1_ZIP = BASE_DIR + "test_rdf_1.rdf.zip"
XML_1_ZIP = BASE_DIR + "test_xml_1.xml.zip"

# compressed dirctory
COMPRESSED_DIR_TAR_GZ = BASE_DIR + "test_compressed_dir.tar.gz"
COMPRESSED_DIR_ZIP = BASE_DIR + "test_compressed_dir.zip"

# Reference files
PREFIXES_FILE_PATH = "reference/prefixes.tsv"
PREFIXES_ERROR_FILE_PATH = "reference/prefixes-error.tsv"
REFINE_CLASS_URIS_FILE_PATH = "reference/refine-class-uris.tsv"
REFINE_CLASS_URIS_ERROR_FILE_PATH = "reference/refine-class-uris-error.tsv"
REFINE_PREFIX_URIS_FILE_PATH = "reference/refine-prefix-uris.tsv"
REFINE_PREFIX_URIS_ERROR_FILE_PATH = "reference/refine-prefix-uris-error.tsv"
