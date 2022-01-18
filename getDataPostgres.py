#!/usr/bin/env python3
"""
Classe criada para conectar-se ao postgre e extrair dados da tabela tb_dados_extraidos,
em seguida os dados são inserido no cluster do elasticSearch, onde seram manipulados
quando o usuario realizar consultas via tela
"""

import simplejson as json
import psycopg2
from psycopg2.extras import RealDictCursor
import postElasticSearch


class PostgresWrapper:

    def __init__(self, **args):
        self.user = args.get('user', 'postgres')
        self.password = args.get('password', 'admin')
        self.port = args.get('port', 5432)
        self.dbname = args.get('dbname', 'postgres')
        self.host = args.get('host', 'localhost')
        self.connection = None

    def connect(self):
        pg_conn = psycopg2.connect(
            user=self.user,
            password=self.password,
            port=self.port,
            dbname=self.dbname,
            host=self.host
        )
        self.connection = pg_conn

    def get_json_cursor(self):
        return self.connection.cursor(cursor_factory=RealDictCursor)

    @staticmethod
    def execute_and_fetch(cursor, query):
        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        return res

    def get_json_response(self, query):
        cursor = self.get_json_cursor()
        response = self.execute_and_fetch(cursor, query)
        return json.dumps(response, default=str)

    def get_countries(self, ):
        query = "SELECT * FROM tb_dados_extraidos;"
        output_json = self.get_json_response(query).replace('[', '{"Dados":[').replace(']', ']}')
        novo_json = json.loads(output_json)
        valor = str(novo_json)
        vl= eval(valor)
        postElasticSearch.sendElasticSearch(vl)


dbconn = PostgresWrapper()
dbconn.connect()
dbconn.get_countries()
