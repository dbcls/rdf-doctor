# rdf-doctor
[![Pyversions](https://img.shields.io/pypi/pyversions/rdf-doctor.svg)](https://pypi.python.org/pypi/rdf-doctor)

## Motivation
DBCLS has conducted to convert various life science databases to RDF and support it. This development will enable us to provide a high-quality dataset that better links existing RDF datasets stored in the RDF portal site and newly developed RDF.

## Requirements
```
(1) Operating system
Linux (CentOS 7 or later or Ubuntu 20.04 or later), macOS 12 Monterey or later

(2) Software development language
Python

(3) Operating system environment
Main memory: 32 GB or less
Hard disk: 2TB or less
```

## Install
```
pip install rdf-doctor
```

## Command Line Interface
```
$ rdf-doctor --help
usage: rdf-doctor -i RDF-FILE [Options]

Home page: https://github.com/dbcls/rdf-doctor

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -v, --verbose         show progress while processing
  -i RDF-FILE or DIRECTORY [RDF-FILE or DIRECTORY ...], --input RDF-FILE or DIRECTORY [RDF-FILE or DIRECTORY ...]
                        input RDF file or directory (Turtle(.ttl), N-Triples(.nt), RDF/XML(.rdf, .xml, .owl) and their compressed versions are supported)
  -t TYPE, --type TYPE  specifies the type of the input file ("all" or individually from the following Multiple types can be specified by separating them with a comma. ttl, nt, rdf_xml, ttl_gz, nt_gz, rdf_xml_gz, ttl_zip, nt_zip, rdf_xml_zip)
  -r, --report          add report to results
  -o DIRECTORY, --output DIRECTORY
                        directory to output results (standard output if not specified)
  -c URL [URL ...], --classes URL [URL ...]
                        set the target classes to be inspected to one of: all (defalut) or URL1 URL2...
  -e, --each            separate results by file when multiple files are specified
  --tmp-dir DIRECTORY   Temporary directory where the unzipped contents are placed when processing tar.gz or zipped directory
  --tmp-dir-disk-usage-limit PERCENTAGE
                        Percentage of disk usage that contains the temporary directory where unzipped contents are placed when processing tar.gz or zipped directory. Interrupt processing when the specified usage percentage is exceeded (1-100 default: 95)
  --prefix-uri-dict FILE
                        path to a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination for the prefix (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-
                        doctor/blob/main/doctor/reference/refine-prefix-uris.tsv)
  --class-uri-dict FILE
                        path to a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination for the class (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-
                        doctor/blob/main/doctor/reference/refine-class-uris.tsv)
  --prefix-list FILE    list of prefixes (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/prefixes.tsv)
  --force-format INPUT-FORMAT
                        This option should not normally be used. Because the input format is automatically determined by the file extension. Use it only when you want to force specification. If used, "turtle", "nt" and
                        "xml"(=RDF/XML) can be specified.
```

## See Also
- [1] https://github.com/DaniFdezAlvarez/shexer
- [2] http://shex.io/shex-primer/#combined-constraints
- [3] https://openrefine.org/docs/technical-reference/clustering-in-depth#fingerprint

## Example
```
$ rdf-doctor -i example_1.ttl
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX oboc: <http://www.ebi.ac.uk/oboc/searchId.do?obocId=CHEBI%3A>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX ns1: <http://example.org#>
PREFIX ns2: <https://example.org#>
PREFIX foaf: <http://xmlns.com/foaf/0.1#>
PREFIX : <http://weso.es/shapes/>

:Document  [<http://www.ebi.ac.uk/oboc/>~]  AND   # 1 instance
{
   rdf:type  [foaf:Document]  ;                                # 100.0 % (1 instance).
   oboc:depiction  xsd:string  ;                               # 100.0 % (1 instance).
   oboc:title  xsd:string                                      # 100.0 % (1 instance).
}


:Parson  [<http://www.ebi.ac.uk/oboc/>~]  AND   # 1 instance
{
   rdf:type  [foaf:Parson]  ;                                  # 100.0 % (1 instance).
   oboc:familyName  xsd:string  ;                              # 100.0 % (1 instance).
   oboc:knows  IRI  ;                                          # 100.0 % (1 instance).
   oboc:name  xsd:string                                       # 100.0 % (1 instance).
}


:PERSON  [<http://www.ebi.ac.uk/oboc/>~]  AND   # 1 instance
{
   rdf:type  [foaf:PERSON]  ;                                  # 100.0 % (1 instance).
   oboc:name  xsd:string  ;                                    # 100.0 % (1 instance).
   oboc:age  xsd:integer                                       # 100.0 % (1 instance).
}


:DOCUMENT  [<http://www.ebi.ac.uk/oboc/>~]  AND   # 1 instance
{
   oboc:title  xsd:string  ;                                   # 100.0 % (1 instance).
   rdf:type  [foaf:DOCUMENT]                                   # 100.0 % (1 instance).
}


:PErson  [<http://www.ebi.ac.uk/oboc/>~]  AND   # 1 instance
{
   oboc:name  xsd:string  ;                                    # 100.0 % (1 instance).
   rdf:type  [foaf:PErson]  ;                                  # 100.0 % (1 instance).
   oboc:familyName  xsd:string  ;                              # 100.0 % (1 instance).
   oboc:age  xsd:integer                                       # 100.0 % (1 instance).
}


:Person  [<http://www.ebi.ac.uk/oboc/>~]  AND   # 1 instance
{
   oboc:name  xsd:string  ;                                    # 100.0 % (1 instance).
   oboc:age  xsd:integer  ;                                    # 100.0 % (1 instance).
   rdf:type  [foaf:Person]  ;                                  # 100.0 % (1 instance).
   oboc:familyName  xsd:string                                 # 100.0 % (1 instance).
}


# # Report on
# ```
# test_ttl_5.ttl
# ```
# 
# ## Prefix reuse percentage ([?](https://github.com/dbcls/rdf-doctor#output-description))
# 
# Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor.
# ```
# 33.33%
# ```
# 
# 
# ## Refine namespace and URIs ([?](https://github.com/dbcls/rdf-doctor#output-description))
# 
# Duplicate prefixes found.
# ```
# Input-Namespace       Input-prefix-URI
# ex2:  http://example.org#
# ex2:  https://example.org#
# ```
# 
# 
# There is a more widely used Namespace and URI.
# (For each of Namespace and URI, output only if the input value differs from the widely used value.)
# Using a customized prefix list. (tests/reference/prefixes.tsv)
# Using a customized prefix URI dictionary. (tests/reference/refine-prefix-uris.tsv)
# ```
# Input-Namespace       Input-URI       Widely-used-Namespace   Widely-used-URI
# ex2:  http://example.org#     alice:|egdo:|ex:  http://example.org/
# ex2:  https://example.org#    alice:|egdo:|ex:  http://example.org/
# foaf: http://xmlns.com/foaf/0.1#              http://xmlns.com/foaf/0.1/
# ```
# 
# 
# ## Refine class URIs ([?](https://github.com/dbcls/rdf-doctor#output-description))
# 
# Found a more widely used one for the class URI inputed.
# Using a customized class URI dictionary. (tests/reference/refine-class-uris.tsv)
# ```
# Input-class-URI       Suggested-class-URI
# http://xmlns.com/foaf/0.1#Person      http://xmlns.com/foaf/0.1/Person
# http://xmlns.com/foaf/0.1#Document    http://xmlns.com/foaf/0.1/Document
# ```
# 
# 
# Found multiple strings that appear to represent the same class.
# ```
# http://xmlns.com/foaf/0.1#Person
# http://xmlns.com/foaf/0.1#PErson
# http://xmlns.com/foaf/0.1#PERSON
# 
# http://xmlns.com/foaf/0.1#Document
# http://xmlns.com/foaf/0.1#DOCUMENT
# ```
# 
#
```

## Example of dictionary file
You can specify arbitrary dictionary files for prefixes and class URIs. It is a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination one per line like [this](https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/refine-prefix-uris.tsv).
Specify --prefix-uri-dict for prefix, --class-uri-dict for class, followed by file.
See: https://github.com/dbcls/rdf-doctor#command-line-interface


## Example of prefix list
You can specify arbitrary files for prefix list. It is a tab delimited file listing QName and URI like [this](https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/prefixes.tsv).
Specify --prefix-list, followed by file.
See: https://github.com/dbcls/rdf-doctor#command-line-interface


## Output Description
This is an explanation of the output contents when the -r (--report) option is specified.

* **Prefix reuse percentage**: Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor (or specified by --prefix-list option).

* **Refine namespace and URIs**: The namespaces and URIs entered as a prefix is checked against a list defined inside rdf-doctor (or specified by --prefix-uri-dict and --prefix-list option), and if there is matching information, output as correction suggestions. Also, if a prefix with the same namespace but a different URI is found, it is output as a correction suggestion.

* **Refine class URIs**: The URI of the input class is checked against the list defined inside rdf-doctor (or specified by --class-uri-dict option), and if there is matching information, a candidate rewrite URI is suggested. Also, if the URI of the input class is converted to a key string using the fingerprinting method and multiple different strings are found even though the key strings match, they may represent the same class. Output as correction suggestions.
