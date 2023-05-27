#pip install elasticsearch
from elasticsearch import Elasticsearch

# Establish a connection to the Elasticsearch server
es = Elasticsearch(
    hosts=[{"host": "https://127.0.0.1", "port": 9200}],  # Replace with the appropriate host and port
    http_auth=("elastic", "gy1Vyc-N1dIuYM9a8LLZ"),  # If authentication is required
    scheme="https"
)

# Perform a search query
query = {
    "query": {
        "match": {
            "field_name": "search_term"
        }
    }
}

response = es.search(index="your_index_name", body=query)

# Process the search results
for hit in response["hits"]["hits"]:
    source = hit["_source"]
    print(source)
