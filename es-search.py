from elasticsearch import Elasticsearch

es = Elasticsearch(["http://127.0.0.1:9200"])
data = es.search(index="my_index", body={"query": {"match_all":{}}})
print(data)