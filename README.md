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
                        (only when md(same as "markdown") is specified with -r, --report option) path to a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination for
                        the prefix (default: predefined file in rdf-doctor)
  -l FILE, --class-dict FILE
                        (only when md(same as "markdown") is specified with -r, --report option) path to a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination for
                        the class (default: predefined file in rdf-doctor)
  -x FILE, --prefix-list FILE
                        list of prefixes (default: predefined file in rdf-doctor)
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
PREFIX oboc: <http://purl.obolibrary.org/obo/CHEBI_>
PREFIX chebi: <http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX pobo: <http://purl.obolibrary.org/obo/>
PREFIX ex: <http://example.org1/>
PREFIX ex: <http://example.org2/>
PREFIX : <http://weso.es/shapes/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xml: <http://www.w3.org/XML/1998/namespace/>

:searchId.do?chebiId=CHEBI%3ADocument  [<http://purl.obolibrary.org/obo/>~]  AND   # 1 instance
{
   rdf:type  [chebi:Document]  ;                               # 100.0 % (1 instance).
   chebi:depiction  xsd:string  ;                              # 100.0 % (1 instance).
   chebi:title  xsd:string                                     # 100.0 % (1 instance).
}


:searchId.do?chebiId=CHEBI%3APErson  [<http://purl.obolibrary.org/obo/>~]  AND   # 1 instance
{
   chebi:name  xsd:string  ;                                   # 100.0 % (1 instance).
   rdf:type  [chebi:PErson]  ;                                 # 100.0 % (1 instance).
   chebi:familyName  xsd:string  ;                             # 100.0 % (1 instance).
   chebi:age  xsd:integer                                      # 100.0 % (1 instance).
}


:searchId.do?chebiId=CHEBI%3ADOCUMENT  [<http://purl.obolibrary.org/obo/>~]  AND   # 1 instance
{
   chebi:title  xsd:string  ;                                  # 100.0 % (1 instance).
   rdf:type  [chebi:DOCUMENT]                                  # 100.0 % (1 instance).
}


:searchId.do?chebiId=CHEBI%3APerson  [<http://purl.obolibrary.org/obo/>~]  AND   # 1 instance
{
   chebi:age  xsd:integer  ;                                   # 100.0 % (1 instance).
   chebi:name  xsd:string  ;                                   # 100.0 % (1 instance).
   rdf:type  [chebi:Person]  ;                                 # 100.0 % (1 instance).
   chebi:familyName  xsd:string                                # 100.0 % (1 instance).
}


:searchId.do?chebiId=CHEBI%3AParson  [<http://purl.obolibrary.org/obo/>~]  AND   # 1 instance
{
   chebi:familyName  xsd:string  ;                             # 100.0 % (1 instance).
   rdf:type  [chebi:Parson]  ;                                 # 100.0 % (1 instance).
   chebi:knows  @:searchId.do?chebiId=CHEBI%3APErson  ;          # 100.0 % (1 instance).
   chebi:name  xsd:string                                      # 100.0 % (1 instance).
}


:searchId.do?chebiId=CHEBI%3APERSON  [<http://purl.obolibrary.org/obo/>~]  AND   # 1 instance
{
   chebi:age  xsd:integer  ;                                   # 100.0 % (1 instance).
   chebi:name  xsd:string  ;                                   # 100.0 % (1 instance).
   rdf:type  [chebi:PERSON]                                    # 100.0 % (1 instance).
}


# Duplicate prefixes found.

# Input-QName	Input-prefix-URI
# ex:	http://example.org1/
# ex:	http://example.org2/


# There is a more widely used QName.

# Input-QName	Widely-used-QName	URI
# pobo:	obo:	http://purl.obolibrary.org/obo/
# pobo:	uo:	http://purl.obolibrary.org/obo/
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
57.14%
```

## Refine prefix URIs ([?](https://github.com/dbcls/rdf-doctor#output-description))
Found a more widely used one for the prefix URI inputed.
```
Input-QName	Input-prefix-URI	Suggested-prefix-URI
chebi:	http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A	http://purl.obolibrary.org/obo/CHEBI_
```

Duplicate prefixes found.
```
Input-QName	Input-prefix-URI
ex:	http://example.org1/
ex:	http://example.org2/
```

## Refine class URIs ([?](https://github.com/dbcls/rdf-doctor#output-description))
Found a more widely used one for the class URI inputed.
```
Input-class-URI	Suggested-class-URI
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson	http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson
```

Found multiple strings that appear to represent the same class.
```
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APERSON

http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADocument
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADOCUMENT
```
````


## Example of dictionary file
You can specify arbitrary dictionary files for prefixes and class URIs. It is a tab delimited file listing candidate pairs of URI rewrite source and rewrite destination, one per line, as like [this](https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/refine-prefix-uris.tsv).
This dictionary file is used only if -r or --report option is specified as md (same as markdown).
Specify -p, --prefix-dict for prefix, -l, --class-dict for class, followed by file.
See: https://github.com/dbcls/rdf-doctor#command-line-interface


## Example of prefix list
You can specify arbitrary  files for prefix list. It is a tab delimited file listing QName and URI, one per line, as like [this](https://github.com/dbcls/rdf-doctor/blob/main/doctor/reference/refine-prefix-uris.tsv).
This prefix list is used to calculate prefix reuse percentages(in "-r md") and to present widely used QName(in "-r shex").
Specify -x, --prefix-list, followed by file.
See: https://github.com/dbcls/rdf-doctor#command-line-interface


## Output Description
* **Prefix reuse percentage**: Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor (or specified by -x option).

* **Refine prefix URIs**: The URI entered as a prefix is checked against a list defined inside rdf-doctor (or specified by -p option), and if there is matching information, output as correction suggestions. Also, if a prefix with the same QName but a different URI is found, it is output as a correction suggestion.

* **Refine class URIs**: The URI of the input class is checked against the list defined inside rdf-doctor (or specified by -l option), and if there is matching information, a candidate rewrite URI is suggested. Also, if the URI of the input class is converted to a key string using the fingerprinting method and multiple different strings are found even though the key strings match, they may represent the same class. Output as correction suggestions.