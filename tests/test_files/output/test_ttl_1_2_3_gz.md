# Report on
```
test_ttl_1.ttl.gz
test_ttl_2.ttl.gz
test_ttl_3.ttl.gz
```

## Prefix reuse percentage ([?](https://github.com/dbcls/rdf-doctor#output-description))
Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor.
```
70.0%
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
ex:	http://example.org/
ex:	http://example.org#
foaf:	http://xmlns.com/foaf/0.1/
foaf:	http://xmlns.com/foaf/0.1#
```

## Refine class URIs ([?](https://github.com/dbcls/rdf-doctor#output-description))
Found a more widely used one for the class URI inputed.
```
Input-class-URI	Suggested-class-URI
http://xmlns.com/foaf/0.1#Person	http://xmlns.com/foaf/0.1/Person
http://xmlns.com/foaf/0.1#Document	http://xmlns.com/foaf/0.1/Document
```

Found multiple strings that appear to represent the same class.
```
http://xmlns.com/foaf/0.1/Person
http://xmlns.com/foaf/0.1#Person

http://xmlns.com/foaf/0.1/Document
http://xmlns.com/foaf/0.1#Document

http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APerson
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APErson
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3APERSON

http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADocument
http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3ADOCUMENT
```

