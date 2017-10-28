from flask import Flask, render_template, request, jsonify, json

import traceback

# Objeto Flask
app = Flask(__name__)

users = []
default_password = "pass123"

@app.route('/register', methods = ['POST'])
def register_user():
    try:
    
        json_data = request.get_json()["user"]
        print("json_data-> ", json_data)
        username = json_data['username']
        password = json_data['password']
        
        if username in users:
            return jsonify({"message": "User %s already registered!" % username, "user": username})
        else:
            users.append(username)
            return jsonify({"message": "User %s successfully registered!" % username, "user": username})
    
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"message": "It was not possible to register new User %s" % ex})

@app.route('/login', methods = ['POST'])
def login_user():
    try:
    
        json_data = request.get_json()["auth"]
        print("json_data-> ", json_data)
        username = json_data['username']
        password = json_data['password']
        
        if username in users:
            if password == default_password:
                return jsonify({"message": "Hello %s welcome back" % username, "user": username})
            else:
                return jsonify({"message": "Your password is not correct. Try again", "user": username})
        else:
            return jsonify({"message": "User %s not found!" % username, "user": username})
    
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"message": "It was not possible to login user - %s" % ex})
        
@app.route('/users', methods = ['GET'])
def list_users():
    return jsonify({"users:": users})

@app.route('/shutdown', methods=['GET'])
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