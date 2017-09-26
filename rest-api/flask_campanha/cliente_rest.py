from flask import Flask, jsonify, request, Blueprint
from connect_db import *

import datetime
import traceback

cliente_rest = Blueprint('cliente_rest', __name__)

@cliente_rest.route("/", methods=["GET"])
def teste():
    return jsonify({"msg": "ok"})