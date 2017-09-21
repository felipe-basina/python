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
    db.criar_schema()
    db.close_db()
    return jsonify("status:ok")

@app.route("/add", methods=["POST"])    
def inserir_db():
    json_dict_request = request.get_json()
    print("Preparando para inserir registro %s" % json_dict_request)

    db = Connect()
    db.criar_schema()
    
    if db.recuperar_por_email(json_dict_request['email']):
        return jsonify({"erro": "Email %s ja cadastrado!" % json_dict_request['email']})
    
    db.inserir_um_registro(json_dict_request)
    response = db.recuperar_registros()

    return jsonify({"msg": "Retorno", "persons": response})

@app.route("/all", methods=["GET"])
def all_db():
    db = Connect()
    db.criar_schema()
    response = db.recuperar_registros()
    
    return jsonify({"msg": "Retorno", "persons": response})
    
@app.route("/", methods=["DELETE"])
def remover_db():
    db = Connect()
    db.criar_schema()
    return jsonify({"msg": "Retorno", "persons": db.remover_registros()})

app.run(debug=True)