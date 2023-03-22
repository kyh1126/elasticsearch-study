from elasticsearch import Elasticsearch

es = Elasticsearch(["http://127.0.0.1:9200"])
data = es.get(index="my_index", doc_type="doc1", id=1)
print(data)