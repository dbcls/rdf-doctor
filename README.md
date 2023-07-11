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
  -v, --version         show program's version number and exit
  -e, --verbose         show progress while processing
  -i RDF-FILE [RDF-FILE ...], --input RDF-FILE [RDF-FILE ...]
                        input RDF file(s)(.ttl or .nt or gzip-compressed versions of them). Use the same extension when specifying multiple.
  -r REPORT-FORMAT, --report REPORT-FORMAT
                        set the output format/serializer of report to one of: shex (defalut) or md or markdown(same as md)
  -o FILE, --output FILE
                        write to file instead of stdout
  -c URL [URL ...], --classes URL [URL ...]
                        set the target classes to be inspected to one of: all (defalut) or URL1, URL2,...
  -p FILE, --prefix-dict FILE
                        (only when "-r md"(same as "-r markdown") is specified) path to a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination for the prefix (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/refine-prefix-uris.tsv)
  -l FILE, --class-dict FILE
                        (only when "-r md"(same as "-r markdown") is specified) path to a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination for the class (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/refine-class-uris.tsv)
  -x FILE, --prefix-list FILE
                        list of prefixes (default: predefined file in rdf-doctor: https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/prefixes.tsv)
  -f INPUT-FORMAT, --force-format INPUT-FORMAT
                        This option should not normally be used. Because the input format is automatically determined by the file extension. Use it only when you want to force specification. If used, "turtle" or "nt" can be specified.
```

## See Also
- [1] https://github.com/DaniFdezAlvarez/shexer
- [2] http://shex.io/shex-primer/#combined-constraints
- [3] https://openrefine.org/docs/technical-reference/clustering-in-depth#fingerprint

## Example
```
$ rdf-doctor -i example_1.ttl
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX xmls: <http://www.w3.org/2001/XMLSchema#>
PREFIX ex: <http://example.org1/>
PREFIX ex: <http://example.org/>
PREFIX : <http://weso.es/shapes/>

:Person  [<http://example.org/>~]  AND   # 4 instances
{
   rdf:type  [foaf:Person]  ;                                  # 100.0 % (4 instances).
   foaf:name  xmls:string  ;                                   # 100.0 % (4 instances).
   foaf:age  xmls:integer  ?;
            # 75.0 % (3 instances). obj: xmls:integer. Cardinality: {1}
   foaf:familyName  xmls:string  ?;
            # 75.0 % (3 instances). obj: xmls:string. Cardinality: {1}
   foaf:knows  @:Person  ?
            # 25.0 % (1 instance). obj: @:Person. Cardinality: {1}
}


:Document  [<http://example.org/>~]  AND   # 2 instances
{
   rdf:type  [foaf:Document]  ;                                # 100.0 % (2 instances).
   foaf:title  xmls:string  ;                                  # 100.0 % (2 instances).
   foaf:depiction  xmls:string  ?
            # 50.0 % (1 instance). obj: xmls:string. Cardinality: {1}
}


# Duplicate prefixes found.

# Input-QName   Input-prefix-URI
# ex:   http://example.org1/
# ex:   http://example.org/


# There is a more widely used QName.

# Input-QName   Widely-used-QName       URI
# xmls: xsd:    http://www.w3.org/2001/XMLSchema#
```

````
$ rdf-doctor -i example_2.ttl -r md
# Report on
```
example_2.ttl
```

## Prefix reuse percentage ([?](https://github.com/dbcls/rdf-doctor#output-description))
Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor.
```
60.0%
```

## Refine prefix URIs ([?](https://github.com/dbcls/rdf-doctor#output-description))
Found a more widely used one for the prefix URI inputed.
```
Input-QName     Input-prefix-URI        Suggested-prefix-URI
foaf:   http://xmlns.com/foaf/0.1#      http://xmlns.com/foaf/0.1/
```

Duplicate prefixes found.
```
Input-QName     Input-prefix-URI
ex:     http://example.org/
ex:     https://example.org/
```

## Refine class URIs ([?](https://github.com/dbcls/rdf-doctor#output-description))
Found a more widely used one for the class URI inputed.
```
Input-class-URI Suggested-class-URI
http://xmlns.com/foaf/0.1#Person        http://xmlns.com/foaf/0.1/Person
http://xmlns.com/foaf/0.1#Document      http://xmlns.com/foaf/0.1/Document
```

Found multiple strings that appear to represent the same class.
```
http://xmlns.com/foaf/0.1#Person
http://xmlns.com/foaf/0.1#PErson

http://xmlns.com/foaf/0.1#Document
http://xmlns.com/foaf/0.1#DOcument
```
````


## Example of dictionary file
You can specify arbitrary dictionary files for prefixes and class URIs. It is a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination one per line like [this](https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/refine-prefix-uris.tsv).
This dictionary file is used only if -r or --report option is specified as md (same as markdown).
Specify -p, --prefix-dict for prefix, -l, --class-dict for class, followed by file.
See: https://github.com/dbcls/rdf-doctor#command-line-interface


## Example of prefix list
You can specify arbitrary files for prefix list. It is a tab delimited file listing QName and URI like [this](https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/prefixes.tsv).
This prefix list is used to calculate prefix reuse percentages(in "-r md") and to present widely used QName(in "-r shex").
Specify -x, --prefix-list, followed by file.
See: https://github.com/dbcls/rdf-doctor#command-line-interface


## Output Description
This is a description of the output when "-r md" (same as "-r markdown") is specified in the options.

* **Prefix reuse percentage**: Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor (or specified by -x option).

* **Refine prefix URIs**: The URI entered as a prefix is checked against a list defined inside rdf-doctor (or specified by -p option), and if there is matching information, output as correction suggestions. Also, if a prefix with the same QName but a different URI is found, it is output as a correction suggestion.

* **Refine class URIs**: The URI of the input class is checked against the list defined inside rdf-doctor (or specified by -l option), and if there is matching information, a candidate rewrite URI is suggested. Also, if the URI of the input class is converted to a key string using the fingerprinting method and multiple different strings are found even though the key strings match, they may represent the same class. Output as correction suggestions.