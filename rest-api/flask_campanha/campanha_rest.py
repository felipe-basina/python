from flask import Flask, jsonify, request, g
from connect_db import *
from cliente_rest import *
from aux_modulos import *

import datetime
import traceback

app = Flask(__name__)

app.register_blueprint(cliente_rest, url_prefix='/cliente')

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

@app.route("/<int:campanha_id>", methods=["DELETE"])
def delete_one(campanha_id):
    try:
        db = CampanhaDb(False)
        
        campanha = db.recuperar_campanha_por_id(campanha_id)
        if not campanha:
            return jsonify({"code": "ERR-0003", "error": "Nenhuma campanha encontrada com ID { %s }" % (campanha_id)})
        
        campanha_removida = db.remover_campanha(campanha_id)
        if campanha_removida != True:
            return jsonify({"code": "ERR-0003", "error": "Nao foi possivel remover a campanha { %s }: %s" % (campanha_id, campanha_removida)})    
        
        return jsonify({"status": "ok", "msg": "Campanha removida com sucesso"})
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"code": "ERR-0003", "error": "Erro ao remover campanha com ID { %s }: %s" % (campanha_id, ex)})
        
@app.route("/", methods=["POST"])
def insert_new():
    try:    
        json_request = request.get_json()
        
        db = ClienteDb(False)
        time = db.recuperar_time_por_id(json_request["id_time"])
        if 'erro' in time:
            return jsonify({"code": "ERR-0002", "error": "Erro ao recuperar time: %s" % time})
        
        db = CampanhaDb(False)
        
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
        
app.run(debug=True)