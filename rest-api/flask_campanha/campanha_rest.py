from flask import Flask, jsonify, request
from connect_db import *

app = Flask(__name__)

# https://stackoverflow.com/questions/6871016/adding-5-days-to-a-date-in-python

@app.route("/")
def get_all():
    try:
        db = CampanhaDb()
        campanhas = db.recuperar_campanhas()
        
        campanha_lista = []
        
        if campanhas:
            for _, nome, id_time, dt_inicio, dt_fim, _ in campanhas:
                dict = {}
                dict['nome_campanha'] = nome
                dict['id_time'] = id_time
                dict['dt_inicio_vigencia'] = dt_inicio.strftime('%d/%m/%Y')
                dict['dt_fim_vigencia'] = dt_fim.strftime('%d/%m/%Y')
                
                campanha_lista.append(dict)
        else:
            raise Exception("Nenhuma campanhada cadastrada")
        
        return jsonify({"status": "ok", "campanhas": campanha_lista, "total": len(campanha_lista)})
    except Exception as ex:
        return jsonify({"code": "ERR-0001", "error": "Erro ao recuperar campanhas %s" % ex})

app.run(debug=True)