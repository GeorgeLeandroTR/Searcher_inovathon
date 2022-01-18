from flask import Flask, render_template, request, redirect, url_for
from elasticsearch import Elasticsearch

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        search = request.form.get('search')
        return redirect(url_for('results', search=search))
    return render_template("home.html")


@app.route('/results', methods=['GET', 'POST'])
def results():
    search = request.args.get('search', None)
    if request.method == 'POST':
        search = request.form['search'].upper()
    else:
        search = 'nada'

    #print("name ---> " +str(search))

    #search = "TRAVA"
    es = Elasticsearch(
        ['localhost:9200'],
        port=8000, )
    res = es.search(index="index_thomson", body={"query": {"match": {"Dados.DESCRICAO_DETALHADA": ""+search+""}}})
    #print("res -->> "+ str(res))


    return render_template("results.html", value=res, pes= search)



app.run(host='127.0.0.1', port=80)
