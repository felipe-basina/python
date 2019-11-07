from flask import Flask, jsonify

from api.arith_rest import *

app = Flask(__name__)
app.register_blueprint(arith_rest, url_prefix = '/arith')

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})

app.run(debug = True)