from flask import Flask, jsonify

import re
import traceback

app = Flask(__name__)

@app.route("/<string:cpf>", methods = ["GET"])
@app.route("/", methods = ["GET"])
def verificar_cpf_blacklist(cpf = ""):
    if not (cpf and cpf_valido(cpf)):
        return jsonify("RUNNING")
    else:
        cpf_bloqueado = cpf_em_blacklist(remover_caracteres_especiais(cpf))
        if cpf_bloqueado:
            return jsonify("BLOCK")
        else:
            return jsonify("FREE")

def cpf_em_blacklist(cpf):
    lista_cpf_temp = []
    try:
    
        with open("blacklist.txt", encoding='utf-8') as f:
            for line in f:
                lista_cpf_temp.append(remover_caracteres_especiais(line))
                
        if cpf in lista_cpf_temp:
            return True
        else:
            return False

    except Exception as ex:
        traceback.print_exc()
        return False
        
def remover_caracteres_especiais(cpf):
    return cpf.replace(".", "").replace("-", "").replace("\n", "")
    
def cpf_valido(cpf):
    verificacao = re.match("((\d){3,}(\.)*){2,3}(\d){3,}(\-)*(\d){2,}", cpf)
    if verificacao:
        return True
    else:
        return False
        
if __name__ == "__main__":
    app.run(debug=True)
