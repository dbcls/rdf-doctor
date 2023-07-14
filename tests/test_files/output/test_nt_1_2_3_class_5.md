# Report on
```
test_nt_1.nt
test_nt_2.nt
test_nt_3.nt
```

## Prefix reuse percentage ([?](https://github.com/dbcls/rdf-doctor#output-description))
Percentage of prefixes used in the input file that are included in the predefined prefix list inside rdf-doctor.
```
Not calculated because there is no prefix defined.
```

## Refine class URIs ([?](https://github.com/dbcls/rdf-doctor#output-description))
Found a more widely used one for the class URI inputed.
```
Input-class-URI	Suggested-class-URI
http://xmlns.com/foaf/0.1/PErson	http://xmlns.com/foaf/0.1/Person
http://xmlns.com/foaf/0.1#Person	http://xmlns.com/foaf/0.1/Person
http://xmlns.com/foaf/0.1#Document	http://xmlns.com/foaf/0.1/Document
```

Found multiple strings that appear to represent the same class.
```
http://xmlns.com/foaf/0.1/Person
http://xmlns.com/foaf/0.1/PErson
http://xmlns.com/foaf/0.1#Person

http://xmlns.com/foaf/0.1/Document
http://xmlns.com/foaf/0.1#Document
```

