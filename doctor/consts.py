VERSION_FILE = "__init__.py"

# Report export format
# REPORT_FORMAT_SHEX = "shex"
# REPORT_FORMAT_MD = "md"               # same as markdown
# REPORT_FORMAT_MARKDOWN = "markdown"   # same as md

# Target classes
TARGET_CLASS_ALL = "all"

# Input file extensions
EXTENSION_NT = ".nt"
EXTENSION_TTL = ".ttl"
EXTENSION_RDF = ".rdf"
EXTENSION_XML = ".xml"
EXTENSION_OWL = ".owl"
EXTENSION_GZ = ".gz"
EXTENSION_TAR_GZ = ".tar.gz"
EXTENSION_ZIP = ".zip"

# Input file type
FILE_TYPE_TTL = "ttl"
FILE_TYPE_NT = "nt"
FILE_TYPE_RDF_XML = "rdf_xml"
FILE_TYPE_TTL_GZ = "ttl_gz"
FILE_TYPE_NT_GZ = "nt_gz"
FILE_TYPE_RDF_XML_GZ = "rdf_xml_gz"
FILE_TYPE_TTL_ZIP = "ttl_zip"
FILE_TYPE_NT_ZIP = "nt_zip"
FILE_TYPE_RDF_XML_ZIP = "rdf_xml_zip"

FILE_TYPE_ALL = "all"

# Dictionary of file type IDs and names
FILE_TYPE_DICT = {
    FILE_TYPE_TTL: "Turtle(.ttl)",
    FILE_TYPE_NT: "N-Triples(.nt)",
    FILE_TYPE_RDF_XML: "RDF/XML(.rdf or .xml or .owl)",
    FILE_TYPE_TTL_GZ: "tar compressed Turtle(.ttl.gz)",
    FILE_TYPE_NT_GZ: "tar compressed N-Triples(.nt.gz)",
    FILE_TYPE_RDF_XML_GZ: "tar compressed RDF/XML(.rdf.gz and .xml.gz and .owl.gz)",
    FILE_TYPE_TTL_ZIP: "zip compressed Turtle(.ttl.zip)",
    FILE_TYPE_NT_ZIP: "zip compressed N-Triples(.nt.zip)",
    FILE_TYPE_RDF_XML_ZIP: "zip compressed RDF/XML(.rdf.zip and .xml.zip and .owl.zip)"
}

# Correct prefix list file path
PREFIXES_FILE_PATH = "reference/prefixes.tsv"

# Errata
REFINE_CLASS_URIS_FILE_PATH = "reference/refine-class-uris.tsv"
REFINE_PREFIX_URIS_FILE_PATH = "reference/refine-prefix-uris.tsv"

# Help link URL
HELP_LINK_URL = "https://github.com/dbcls/rdf-doctor#output-description"

# Default value for disk usage limit, including temporary directories
TMP_DISK_USAGE_LIMIT_DEFAULT = 95