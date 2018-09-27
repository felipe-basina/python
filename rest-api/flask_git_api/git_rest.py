from flask import Flask, jsonify, request, g

import requests
import traceback

app = Flask(__name__)

@app.route("/user/<string:username>")
def get_user_info_by_username(username):
	try:
		git_url = 'https://api.github.com/users/' + username
		response = requests.get(git_url)
		return jsonify({"user-info": response.json(), "user": username, "status": 200})
	except:
		return jsonify({"message": "Internal error", "status": 400})

if __name__ == '__main__':
    app.run(debug=False)
