# Report on test_ttl_3.ttl

## Prefix reuse percentage ([?](https://github.com/dbcls/rdf-doctor#output-description))
Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor.
```
80.0%
```

## Refine prefixes ([?](https://github.com/dbcls/rdf-doctor#output-description))
Found prefixes that looks incorrect.
```
Prefix	Input URI	Suggested URI
chebi:	http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A	http://purl.obolibrary.org/obo/CHEBI_
```

## Refine classes ([?](https://github.com/dbcls/rdf-doctor#output-description))
Found multiple strings that appear to represent the same class name.
```
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APERSON

http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADocument
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADOCUMENT
```
