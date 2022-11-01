# rdf-doctor

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
  -c, --class        Set the shexer target_classes to be inspected to one of:
    all (default）
    URL1, URL2,...
    * See also https://github.com/DaniFdezAlvarez/shexer#params-to-define-target-shapes
```

## Example

```
rdf-doctor -i knapsack_core_2021-08-28_exsample.ttl -r shex+
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.org/>
PREFIX weso-s: <http://weso.es/shapes/>
PREFIX xml: <http://www.w3.org/2001/XMLSchema#>
PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://mb-wiki.nig.ac.jp/resource/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX mb: <http://ddbj.nig.ac.jp/ontolofies/metabobank/>
PREFIX mb-wiki: <http://mb-wiki.nig.ac.jp/>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

weso-s:KNApSAcKCoreRecord
{
   rdf:type  [mb:KNApSAcKCoreRecord]  ;                        # 100.0 %
   sio:SIO_000008  IRI  {2};                                   # 100.0 %
            # 100.0 % obj: @weso-s:CHEMINF_000042. Cardinality: {1}
            # 100.0 % obj: @weso-s:CHEMINF_000043. Cardinality: {1}
   sio:CHEMINF_000200  IRI  {5};                               # 100.0 %
            # 100.0 % obj: @weso-s:CHEMINF_000113. Cardinality: {1}
            # 100.0 % obj: @weso-s:Start_substance. Cardinality: {1}
            # 100.0 % obj: @weso-s:CHEMINF_000018. Cardinality: {1}
            # 100.0 % obj: @weso-s:CHEMINF_000059. Cardinality: {1}
   rdfs:seeAlso  IRI  ;                                        # 100.0 %
   dcterms:hasPart  IRI  {3};                                  # 100.0 %
            # 100.0 % obj: @weso-s:SDfile. Cardinality: {1}
            # 100.0 % obj: @weso-s:CDXfile. Cardinality: {1}
            # 100.0 % obj: @weso-s:CHEMINF_000058. Cardinality: {1}
   mb:fid  xml:string  ;                                       # 100.0 %
   dc:identifier  xml:string  ;                                # 100.0 %
   foaf:homepage  IRI  ;                                       # 100.0 %
   rdfs:label  xml:string  ;                                   # 100.0 %
   sio:SIO_000255  @weso-s:KNApSAcKCoreAnnotations  +          # 100.0 %
            # 73.88767071254684 % obj: @weso-s:KNApSAcKCoreAnnotations. Cardinality: {1}
            # 12.210155562078075 % obj: @weso-s:KNApSAcKCoreAnnotations. Cardinality: {2}
}


weso-s:CHEMINF_000058
{
   rdf:type  [sio:CHEMINF_000058]  ;                           # 100.0 %
   rdfs:seeAlso  IRI  ;                                        # 100.0 %
   dcterms:format  IRI                                         # 100.0 %
}


weso-s:CDXfile
{
   rdf:type  [mb:CDXfile]  ;                                   # 100.0 %
   dcterms:format  IRI  ;                                      # 100.0 %
   rdfs:seeAlso  IRI                                           # 100.0 %
}


weso-s:SDfile
{
   rdf:type  [mb:SDfile]  ;                                    # 100.0 %
   dcterms:format  IRI  ;                                      # 100.0 %
   rdfs:seeAlso  IRI                                           # 100.0 %
}


weso-s:CHEMINF_000042
{
   rdf:type  [sio:CHEMINF_000042]  ;                           # 100.0 %
   sio:SIO_000300  xml:string                                  # 100.0 %
}


weso-s:CHEMINF_000043
{
   rdf:type  [sio:CHEMINF_000043]  ;                           # 100.0 %
   sio:SIO_000300  xml:string                                  # 100.0 %
}


weso-s:CHEMINF_000018
{
   rdf:type  [sio:CHEMINF_000018]  ;                           # 100.0 %
   sio:SIO_000300  rdf:langString  ?;
            # 74.57829037103542 % obj: rdf:langString. Cardinality: {1}
   sio:SIO_000300  xml:string  ?
            # 25.42170962896459 % obj: xml:string. Cardinality: {1}
}


weso-s:CHEMINF_000059
{
   rdf:type  [sio:CHEMINF_000059]  ;                           # 100.0 %
   sio:SIO_000300  xml:string  ;                               # 100.0 %
   rdfs:seeAlso  IRI                                           # 100.0 %
}


weso-s:CHEMINF_000113
{
   rdf:type  [sio:CHEMINF_000113]  ;                           # 100.0 %
   sio:SIO_000300  xml:string  ;                               # 100.0 %
   rdfs:seeAlso  IRI                                           # 100.0 %
}


weso-s:Start_substance
{
   rdf:type  [mb:Start_substance]  ;                           # 100.0 %
   sio:SIO_000300  xml:string                                  # 100.0 %
}


weso-s:KNApSAcKCoreAnnotations
{
   rdf:type  [mb:KNApSAcKCoreAnnotations]  ;                   # 100.0 %
   mb:kingdom  xml:string  ;                                   # 100.0 %
   mb:family  xml:string  ;                                    # 100.0 %
   mb:references  xml:string  +;                               # 100.0 %
            # 99.55414339158509 % obj: xml:string. Cardinality: {1}
   mb:organism  xml:string  ;                                  # 100.0 %
   mb:sp1  xml:string  ;                                       # 100.0 %
   rdfs:seeAlso  IRI  ?;
            # 69.92407991741769 % obj: IRI. Cardinality: {1}
   dcterms:references  IRI  *;
            # 63.87097246524295 % obj: IRI. Cardinality: +
            # 62.57074038553052 % obj: IRI. Cardinality: {1}
   mb:pmid  xml:string  *
            # 63.87097246524295 % obj: xml:string. Cardinality: +
            # 62.57074038553052 % obj: xml:string. Cardinality: {1}
}
```

