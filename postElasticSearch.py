from elasticsearch import Elasticsearch
from datetime import datetime


def sendElasticSearch(json):
    create_json = "Dados inseridos com sucesso no cluster/Elasticsearch"
    update_json = "Dados atualizados com sucesso no cluster/Elasticsearch"

    es = Elasticsearch(
        ['localhost:9200'],
        port=8000,)

    res = es.index(index="index_thomson", id=30,body=json)
    print(res)
    print(create_json) if str(res["result"]) != "updated" else print(update_json)
