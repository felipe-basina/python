from flask import Flask, jsonify, request, Blueprint
from datetime import datetime
from connect_db import *
from aux_modulos import *

import traceback

cliente_rest = Blueprint('cliente_rest', __name__)

@cliente_rest.route("/", methods=["GET"])
def teste():
    return jsonify({"msg": "ok"})
    
@cliente_rest.route("/", methods=["POST"])
def insert_new():
    try:
        json_request = request.get_json()
        print("json request:", json_request)
        
        db = ClienteDb(False)
        
        cliente_cadastrado = db.recuperar_cliente_por_email(json_request["email"])
        if cliente_cadastrado:
            return jsonify({"erro": "E-mail %s ja cadastrado. O e-mail deve ser unico" % json_request["email"]})
        
        time_cadastrado = db.recuperar_time_por_id(json_request["id_time"])
        if not time_cadastrado:
            return jsonify({"erro": "ID time {%d} invalido. Por favor, tente novamente com um valor valido" % json_request["id_time"]})
        
        if not cliente_cadastrado is None and "erro" in cliente_cadastrado:
            return jsonify(cliente_cadastrado)
            
        cliente_cadastrado = db.inserir_cliente(json_request)
        if cliente_cadastrado != True:
            return jsonify({"msg": "Nao foi possivel realizar o cadastro do novo cliente. Por favor, tente novamente", 
                            "details": cliente_cadastrado})
            
        campanhas = recuperar_campanhas_por_id_time(json_request["id_time"])
            
        return jsonify({"status": "ok", "campanhas": campanhas})
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"erro": "Nao foi possivel realizar o cadastro", "msg": "%s" % ex})
        
@cliente_rest.route("/all", methods=["GET"])
def get_all():
    try:
        db = ClienteDb(False)
        clientes = db.recuperar_clientes()
        return jsonify(converter_clientes_para_json(clientes))
    except Exception as ex:
       traceback.print_exc()
       return jsonify({"erro": "Nao foi possivel recuperar clientes: %s" % ex})
       
@cliente_rest.route("/all/time", methods=["GET"])
def get_all_teams():
    try:
        db = ClienteDb(False)
        times = db.recuperar_times()
        return jsonify(converter_times_para_json(times))
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"erro": "Nao foi possivel recuperar os times cadastrados: %s" % ex})

@cliente_rest.route("/<int:cliente_id>", methods=["DELETE"])
def delete_one(cliente_id):
    try:
        db = ClienteDb(False)
        
        cliente_removido = db.remover_cliente_por_id(cliente_id)
        if cliente_removido == False:
            return jsonify({"erro": "Nao foi possivel remover o cliente com id %d" % cliente_id})
        
        return jsonify({"status": "ok", "msg": "Registro removido com sucesso"})
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"erro": "Nao foi possivel remover o cliente: " % ex})