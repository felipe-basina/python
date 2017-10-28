from flask import Flask, render_template, request, jsonify, json
from flask_cors import CORS, cross_origin

import traceback

# Objeto Flask
app = Flask(__name__)
CORS(app)

users = []
default_password = "pass123"

@app.route('/register', methods = ['POST'])
def register_user():
    try:
    
        json_data = request.get_json()["auth"]
        username = json_data['username']
        password = json_data['pass']
        
        if username in users:
            raise Exception("User %s already registered!" % username)
        else:
            users.append(username)
            return jsonify({"message": "User %s successfully registered!" % username, "user": username})
    
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"message": str(ex)}), 400

@app.route('/login', methods = ['POST'])
def login_user():
    try:
    
        json_data = request.get_json()["user"]
        username = json_data['username']
        password = json_data['pass']
        
        if username in users:
            if password == default_password:
                return jsonify({"message": "%s welcome back" % username, "user": username})
            else:
                raise Exception("Your password is not correct. Try again")
        else:
           raise Exception("User %s not found!" % username)
    
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"message": str(ex)}), 400
        
@app.route('/users', methods = ['GET'])
def list_users():
    return jsonify({"users": users})

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
    app.run(host='0.0.0.0')