from elasticsearch import Elasticsearch

es = Elasticsearch(["http://127.0.0.1:9200"])

doc = {'name': 'Kim', 'Job': 'IT'}
data = es.index(index="my_index", doc_type="doc1", id=1, body=doc)

print(data)
print("data.result: " + data['result'])
