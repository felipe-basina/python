from flask import Flask, jsonify, request
from conexao_db import *

app = Flask(__name__)

@app.route("/")
def hello():  
    return jsonify("Hello World!")

@app.route("/db")
def conexao_db():
    print("Preparando para se conectar na base de dados...")
    db = Connect()
    db.close_db()
    return jsonify("status:ok")

@app.route("/", methods=["POST"])    
def inserir_db():
    json_dict_request = request.get_json()
    
    retorno = validar_parametros(json_dict_request)
    if retorno != "ok":
        return jsonify(retorno)

    db = Connect()
    
    retorno = db.recuperar_por_email(json_dict_request['email'])
    if retorno is not None:
        return jsonify({"erro": "Email %s ja cadastrado!" % json_dict_request['email']})
    
    db.inserir_um_registro(json_dict_request)

    return jsonify({"msg": "Retorno", "result": db.recuperar_registros()})

@app.route("/", methods=["PUT"])
def atualizar_db():
    json_dict_request = request.get_json()
    
    retorno = validar_parametros(json_dict_request)
    if retorno != "ok":
        return jsonify(retorno)

    db = Connect()
    
    retorno = db.recuperar_por_email(json_dict_request['email'])
    if retorno is None:
        return jsonify({"erro": "Email %s nao cadastrado!" % json_dict_request['email']})

    retorno = db.atualizar_um_registro(json_dict_request, retorno[0])
    if retorno != "ok":
        return jsonify({"erro": retorno})
    
    return jsonify({"msg": "Retorno", 
        "result": "Registro atualizado com sucesso", 
        "update": db.recuperar_por_email(json_dict_request['email'])})
    
@app.route("/all", methods=["GET"])
def all_db():
    db = Connect()
    return jsonify({"msg": "Retorno", "result": db.recuperar_registros()})
    
@app.route("/", methods=["DELETE"])
def remover_db():
    db = Connect()
    return jsonify({"msg": "Retorno", "result": db.remover_registros()})
    
@app.route("/count", methods=["GET"])
def contar_registros_db():
    db = Connect()
    return jsonify({"msg": "Retorno", "total": db.contar_registros()})
    
def validar_parametros(person):
    if not person:
        return {"erro": "Parametro nulo ou vazio"}
    
    if 'name' not in person or person['name'] == '' or len(person['name']) <= 0:
        return {"erro": "Atributo '%s' preenchimento obrigatorio" % "name"}

    if 'username' not in person or person['username'] == '' or len(person['username']) <= 0:
        return {"erro": "Atributo '%s' preenchimento obrigatorio" % "username"}

    if 'email' not in person or person['email'] == '' or len(person['email']) <= 0:
        return {"erro": "Atributo '%s' preenchimento obrigatorio" % "email"}
        
    return "ok"
        
app.run(debug=True)