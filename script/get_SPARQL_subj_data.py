from SPARQLWrapper import SPARQLWrapper, JSON
from operator import itemgetter
import re

#sparql = SPARQLWrapper("http://localhost:7200/repositories/Glyco_RDF")
#sparql = SPARQLWrapper("https://beta.sparql.swisslipids.org/")
#sparql = SPARQLWrapper("https://lsd.dbcls.jp/sparql")
#sparql = SPARQLWrapper("https://integbio.jp/rdf/sparql")

path = "dataset.tsv"
#path = "/data/yayamamo/git/tripledataprofiler/query-result.tsv"
bioportal_graphs = "/data/yayamamo/git/tripledataprofiler/bioportal_graphs.txt"
bioportal_ep = "https://integbio.jp/rdf/bioportal/sparql"

obo_pattern = re.compile(r'purl.obolibrary.org/obo/')
sio_pattern = re.compile(r'semanticscience.org/resource/')
identifier_pattern = re.compile(r'identifiers.org/')
prefix_pattern = re.compile(r'(?<=[^/][#/])[^#/]+[#/]?$')

subj_list_template = """
    select distinct ?subj
    from <___graph_name___>
    where {
        ?subj a <___class_uri___> .
        filter(! isBlank(?subj))
    }
    limit 10000
"""

obj_list_template = """
    select distinct ?obj
    from <___graph_name___>
    where {
        ?obj a <___class_uri___> .
        ?s ?p ?obj .
        filter(isURI(?obj) && ! isBlank(?obj))
    }
    limit 10000
"""

class_list_template = """
    select distinct ?class
    from <___graph_name___>
    where {
        [] a ?class .
        filter(! isBlank(?class))
    } limit 10000
"""

graph_ep_pair = []

def obtain_graph_and_endpoint():
    first = True
    with open(path) as f:
        for line in f:
            if first:
                first = False
                continue
            if re.match(r'#', line) != None:
                continue 

            (gname, ep) = itemgetter(2,5)(line.rstrip().split('\t'))

#            line = line.rstrip()
#            gname = ""
#            ep = ""
#            match = re.search(r'\t', line)
#            if match:
#                (ep, gname) = line.split('\t')
#            else:
#                ep = line

            graph_ep_pair.append({"gname":gname, "ep":ep})
#            print(ep + '\t' + gname)

def get_prefix_list(ep, class_uri, graph_name):
    prefix_list = []
    query = subj_list_template
    if graph_name == "":
        query = re.sub("^\s+from ", "# ", query, flags=re.MULTILINE).replace("___class_uri___", class_uri)
    else:
        query = query.replace("___class_uri___", class_uri).replace("___graph_name___", graph_name)
#    print(query)

    sparql = SPARQLWrapper(ep)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)

    value_list = []
    try:
        ret = sparql.queryAndConvert()
        for r in ret["results"]["bindings"]:
            value_list.append(r["subj"]["value"])
    except Exception as e:
        print(e)

    if len(value_list) == 0:
        return(prefix_list)

    dup_list = []
    last_len = -1

    do_more = True
    while do_more:
        n_value_list = []
        for v in value_list:
#            print(">" + v)
            if obo_pattern.search(v):
                v = re.sub("(?<=obo/)([^_#/]+_).+$", "\\1", v)
            elif sio_pattern.search(v):
                v = re.sub("(?<=resource/)([^_#/]+_).+$", "\\1", v)
            else:
                v = prefix_pattern.sub("", v)
            if v in dup_list:
                continue
            elif v in n_value_list:
                dup_list.append(v)
            else:
                n_value_list.append(v)
#            print("<" + v)
        list_len = len(set(n_value_list))
#        print(list_len)
        if last_len == -1:
            last_len = list_len
        elif list_len < 10 or n_value_list == value_list:
            do_more = False
        value_list = n_value_list

    derived_list = []
    for d in dup_list:
        derived = [var for var in dup_list if var.startswith(d)]
        if len(derived) > 1:
            derived.remove(d)
            derived_list = derived_list + derived

    derived_list = set(derived_list)
#   print(derived_list)

    for d in dup_list:
        if d in derived_list:
            continue
        prefix_list.append(d)

    return(prefix_list)

def get_bioportal_class_data():
    bioportal_graph_list = []
    with open(bioportal_graphs) as f:
        for line in f:
            if re.match(r'#', line) != None:
                continue
            gname = line.rstrip()
            class_list = get_class_list(bioportal_ep, line.rstrip())
            for c in class_list:
                for p in get_prefix_list(bioportal_ep, c, gname):
                    print('\t'.join((bioportal_ep, gname, c, p)))
    return

def get_class_list(ep, graph):
    query = class_list_template
    if graph == "":
        query = re.sub("^\s+from ", "# ", query, flags=re.MULTILINE)
    else:
        query = query.replace("___graph_name___", graph)
#    print(query)

    sparql = SPARQLWrapper(ep)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)

    class_list = []
    try:
        ret = sparql.queryAndConvert()
        for r in ret["results"]["bindings"]:
            class_list.append(r["class"]["value"])
    except Exception as e:
        print(e)

    return(class_list)

#### Main ####
if __name__ == "__main__":

    obtain_graph_and_endpoint()

    for ge in graph_ep_pair:
        if ge["ep"] == bioportal_ep:
            continue
            get_bioportal_class_data()
        else:
            class_list = get_class_list(ge["ep"], ge["gname"])
            for c in class_list:
                for p in get_prefix_list(ge["ep"], c, ge["gname"]):
                    print('\t'.join((ge["ep"], ge["gname"], c, p)))