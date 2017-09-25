from flask import Flask, jsonify, request, g
from connect_db import *

import datetime
import traceback

app = Flask(__name__)

# https://stackoverflow.com/questions/6871016/adding-5-days-to-a-date-in-python

@app.route("/all")
def get_all():
    try:
        db = CampanhaDb()
        campanhas = db.recuperar_campanhas()
        
        campanha_lista = []
        
        if campanhas:
            campanha_lista = converter_campanhas_para_json(campanhas)
        else:
            raise Exception("Nenhuma campanhada cadastrada")
        
        return jsonify({"status": "ok", "campanhas": campanha_lista, "total": len(campanha_lista)})
    except Exception as ex:
        return jsonify({"code": "ERR-0001", "error": "Erro ao recuperar campanhas: %s" % ex})

@app.route("/<int:cliente_id>")
def get_by_cliente_id(cliente_id):
    try:
        db = CampanhaDb(False)
        campanha_lista = converter_campanhas_para_json(db.recuperar_campanhas_por_cliente_id(cliente_id))
        
        return jsonify({"status": "ok", "campanhas": campanha_lista, "total": len(campanha_lista)})
    except Exception as ex:
        return jsonify({"code": "ERR-0011", "error": "Erro ao recuperar campanhas para ID { %s }: %s" % (cliente_id, ex)})
        
@app.route("/", methods=["POST"])
def insert_new():
    try:
        db = CampanhaDb(False)
    
        json_request = request.get_json()
        
        # 1. Verificar se existe alguma campanha com data fim de vigencia
        # igual ao valor enviado como parametro
        campanhas_ativas = db.recuperar_campanhas_ativas(json_request['dt_fim_vigencia'])
        
        if campanhas_ativas:
            # 2. Para cada campanha recuperada deve-se atualizar a data fim de vigencia
            # adicionando 1 dia a data
            for campanha_atual in campanhas_ativas:
                data_fim_atual = campanha_atual[4]
               
                campanha = {}
                campanha["nome_campanha"] = campanha_atual[1]
                campanha["dt_fim_vigencia"] = campanha_atual[4] + datetime.timedelta(days=1)
                campanha["id"] = campanha_atual[0]
               
                db.atualizar_campanha(campanha)
                
                # 2.1 Notificar sistemas sobre alteracao da campanha
                notificar_sistemas_alteracao_campanha(campanha, data_fim_atual)

        # 3. Insere a nova campanha
        registro_inserido = db.inserir_campanha(json_request)
        if registro_inserido != True:
            return jsonify(registro_inserido)
        
        registros_ativos = db.recuperar_campanhas_ativas()
        campanha_lista = converter_campanhas_para_json(registros_ativos)
        
        return jsonify({"status": "ok", "campanhas": campanha_lista, "total": len(campanha_lista)})
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"code": "ERR-0002", "error": "Erro ao inserir nova campanha: %s" % ex})
        
def converter_campanhas_para_json(campanhas):
    campanha_lista = []

    if campanhas:
        for _, nome, id_time, dt_inicio, dt_fim, _ in campanhas:
            dict = {}
            dict['nome_campanha'] = nome
            dict['id_time'] = id_time
            dict['dt_inicio_vigencia'] = dt_inicio.strftime('%d/%m/%Y')
            dict['dt_fim_vigencia'] = dt_fim.strftime('%d/%m/%Y')
            
            campanha_lista.append(dict)
                
    return campanha_lista
        
def notificar_sistemas_alteracao_campanha(campanha, dt_fim_original):
    print("A campanha ID { %s } - NOME { %s } teve a sua data fim de vigencia alterada de { %s } para { %s }" %
        (campanha["id"], campanha["nome_campanha"], 
        dt_fim_original.strftime('%d/%m/%Y'),
        campanha["dt_fim_vigencia"].strftime('%d/%m/%Y')))
        
app.run(debug=True)