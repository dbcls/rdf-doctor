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
EXTENSION_JSON_LD = ".jsonld"
EXTENSION_RDF = ".rdf"
EXTENSION_XML = ".xml"
EXTENSION_OWL = ".owl"
EXTENSION_GZ = ".gz"
EXTENSION_TAR_GZ = ".tar.gz"
EXTENSION_XZ = ".xz"
EXTENSION_TAR_XZ = ".tar.xz"
EXTENSION_ZIP = ".zip"

# Input file type
FILE_TYPE_TTL = "ttl"
FILE_TYPE_NT = "nt"
FILE_TYPE_JSON_LD = "json-ld"
FILE_TYPE_RDF_XML = "rdf_xml"
FILE_TYPE_TTL_GZ = "ttl_gz"
FILE_TYPE_JSON_LD_GZ = "json-ld_gz"
FILE_TYPE_NT_GZ = "nt_gz"
FILE_TYPE_RDF_XML_GZ = "rdf_xml_gz"
FILE_TYPE_TTL_XZ = "ttl_xz"
FILE_TYPE_JSON_LD_XZ = "json-ld_xz"
FILE_TYPE_NT_XZ = "nt_xz"
FILE_TYPE_RDF_XML_XZ = "rdf_xml_xz"
FILE_TYPE_TTL_ZIP = "ttl_zip"
FILE_TYPE_JSON_LD_ZIP = "json-ld_zip"
FILE_TYPE_NT_ZIP = "nt_zip"
FILE_TYPE_RDF_XML_ZIP = "rdf_xml_zip"

FILE_TYPE_ALL = "all"

# Dictionary of file type IDs and names
FILE_TYPE_DICT = {
    FILE_TYPE_TTL: "Turtle(.ttl)",
    FILE_TYPE_NT: "N-Triples(.nt)",
    FILE_TYPE_JSON_LD: "JSON-LD(.jsonld)",
    FILE_TYPE_RDF_XML: "RDF/XML(.rdf or .xml or .owl)",
    FILE_TYPE_TTL_GZ: "gz compressed Turtle(.ttl.gz)",
    FILE_TYPE_JSON_LD_GZ: "gz compressed JSON-LD(.jsonld.gz)",
    FILE_TYPE_NT_GZ: "gz compressed N-Triples(.nt.gz)",
    FILE_TYPE_RDF_XML_GZ: "gz compressed RDF/XML(.rdf.gz and .xml.gz and .owl.gz)",
    FILE_TYPE_TTL_XZ: "xz compressed Turtle(.ttl.xz)",
    FILE_TYPE_JSON_LD_XZ: "xz compressed JSON-LD(.jsonld.xz)",
    FILE_TYPE_NT_XZ: "xz compressed N-Triples(.nt.xz)",
    FILE_TYPE_RDF_XML_XZ: "xz compressed RDF/XML(.rdf.xz and .xml.xz and .owl.xz)",
    FILE_TYPE_TTL_ZIP: "zip compressed Turtle(.ttl.zip)",
    FILE_TYPE_JSON_LD_ZIP: "zip compressed JSON-LD(.jsonld.zip)",
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