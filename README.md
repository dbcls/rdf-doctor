# rdf-doctor

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

Home page: https://github.com/dbcls/rdf-doctor

Usage:
  rdf-doctor -i RDF-FILE [Options]

Argument:
  -i, --input        Input RDF-FILE

Options:
  -h, --help         Show this help message
  -v, --version      Show version number
  -r, --report       Set the output format/serializer of report to one of:
    shex (defalut)
    shex+
    md    markdown
  -o, --output FILE  Write to file instead of stdout
  -c, --classes      Set the shexer target_classes to be inspected to one of:
    all (default）
    URL1, URL2,...
    * See also https://github.com/DaniFdezAlvarez/shexer#params-to-define-target-shapes
```

## TODO

Implementation

```
a) クラスごとのインスタンスについてプレフィックスを取得し、バリデーション表現にしたうえでShExに含める
b) 所与の辞書を参照し、プレフィックス及びクラス名について書き換え候補をレポートに含める
```


## See Also
- [1] https://github.com/DaniFdezAlvarez/shexer
- [2] http://shex.io/shex-primer/#combined-constraints
- [3] https://docs.openrefine.org/next/manual/cellediting#fingerprinting

## Example

```
$ rdf-doctor -i test_turtle_1.ttl
PREFIX : <http://weso.es/shapes/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
PREFIX ex: <http://example.org/>

:Address   # 4 instances
{
   rdf:type  [ex:Address]  ;                                   # 100.0 % (4 instances).
   ex:city  xsd:string  ;                                      # 100.0 % (4 instances).
   ex:state  xsd:string  ;                                     # 100.0 % (4 instances).
   ex:zip  xsd:string  ?;
            # 75.0 % (3 instances). obj: xsd:string. Cardinality: {1}
   ex:street  xsd:string  ?
            # 75.0 % (3 instances). obj: xsd:string. Cardinality: {1}
}


:Person   # 5 instances
{
   rdf:type  [ex:Person]  ;                                    # 100.0 % (5 instances).
   ex:name  xsd:string  ;                                      # 100.0 % (5 instances).
   ex:hasAddress  @:Address  ?;
            # 80.0 % (4 instances). obj: @:Address. Cardinality: {1}
   ex:age  xsd:integer  ?
            # 40.0 % (2 instances). obj: xsd:integer. Cardinality: {1}
}
```

```
$ rdf-doctor -i test_turtle_2.ttl -r md
Prefix reuse percentage: 75.0 %

[INFO] Multiple strings were found that appear to represent the same class name. They are listed below.

http://xmlns.com/foaf/0.1/Person
http://xmlns.com/foaf/0.1/PErson
http://xmlns.com/foaf/0.1/PERSON

http://xmlns.com/foaf/0.1/Document
http://xmlns.com/foaf/0.1/DOCUMENT
http://xmlns.com/foaf/0.1#Document
http://xmlns.com/foaf/0.1/DOcument
```