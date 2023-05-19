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

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i RDF-FILE, --input RDF-FILE
                        input RDF file(.ttl or .nt or gziped versions of them)
  -r FORMAT, --report FORMAT
                        set the output format/serializer of report to one of: shex (defalut) or md or markdown(same as md)
  -o FILE, --output FILE
                        write to file instead of stdout
  -c URL [URL ...], --classes URL [URL ...]
                        set the target classes to be inspected to one of: all (defalut) or URL1, URL2,...
```

## See Also
- [1] https://github.com/DaniFdezAlvarez/shexer
- [2] http://shex.io/shex-primer/#combined-constraints
- [3] https://openrefine.org/docs/technical-reference/clustering-in-depth#fingerprint

## Example
```
$ rdf-doctor -i example.nt
PREFIX : <http://weso.es/shapes/>

:Person  [<http://purl.obolibrary.org/obo/>~]  AND   # 5 instances
{
   <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>  [<http://xmlns.com/foaf/0.1/Person>]  ;          # 100.0 % (5 instances).
   <http://xmlns.com/foaf/0.1/name>  <http://www.w3.org/2001/XMLSchema#string>  ;          # 100.0 % (5 instances).
   <http://xmlns.com/foaf/0.1/age>  <http://www.w3.org/2001/XMLSchema#integer>  ?;
            # 80.0 % (4 instances). obj: <http://www.w3.org/2001/XMLSchema#integer>. Cardinality: {1}
   <http://xmlns.com/foaf/0.1/familyName>  <http://www.w3.org/2001/XMLSchema#string>  ?;
            # 80.0 % (4 instances). obj: <http://www.w3.org/2001/XMLSchema#string>. Cardinality: {1}
   <http://xmlns.com/foaf/0.1/knows>  IRI  ?
            # 40.0 % (2 instances). obj: IRI. Cardinality: {1}
}


:Document  [<http://purl.obolibrary.org/obo/>~]  AND   # 1 instance
{
   <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>  [<http://xmlns.com/foaf/0.1/Document>]  ;          # 100.0 % (1 instance).
   <http://xmlns.com/foaf/0.1/depiction>  <http://www.w3.org/2001/XMLSchema#string>  ;          # 100.0 % (1 instance).
   <http://xmlns.com/foaf/0.1/title>  <http://www.w3.org/2001/XMLSchema#string>            # 100.0 % (1 instance).
}


:Document  [<http://purl.obolibrary.org/obo/>~]  AND   # 1 instance
{
   <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>  [<http://xmlns.com/foaf/0.1#Document>]  ;          # 100.0 % (1 instance).
   <http://xmlns.com/foaf/0.1/title>  <http://www.w3.org/2001/XMLSchema#string>            # 100.0 % (1 instance).
}


# There may be a better QName.

# Input QName   Suggested QName URI
# Undefined     obo:    http://purl.obolibrary.org/obo/
# Undefined     uo:     http://purl.obolibrary.org/obo/
```

````
$ rdf-doctor -i example.ttl -r md
# Report on example.ttl

## Prefix reuse percentage ([?](https://github.com/dbcls/rdf-doctor#output-description))
Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor.
```
75.0%
```

## Refine prefixes ([?](https://github.com/dbcls/rdf-doctor#output-description))
Found prefixes that looks incorrect.
```
Prefix  Input URI       Suggested URI
chebi:  http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A http://purl.obolibrary.org/obo/CHEBI_
```

## Refine classes ([?](https://github.com/dbcls/rdf-doctor#output-description))
Found class names that looks incorrect.
```
Input class name        Suggested class name
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson   http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson
```

Found multiple strings that appear to represent the same class name.
```
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APERSON

http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADocument
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADOCUMENT
```
````

## Output Description
* **Prefix reuse percentage**: Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor.

* **Refine prefixes**: The URI entered as a prefix is checked against a list (errata) defined inside rdf-doctor, and if there is matching information, output as correction suggestions.

* **Refine classes**: The URI of the input class is checked against the list (errata) defined inside rdf-doctor, and if there is matching information, the correct URI is suggested. Also, if the URI of the input class is converted to a key string using the fingerprinting method and multiple different strings are found even though the key strings match, they may represent the same class. Output as correction suggestions.