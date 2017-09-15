from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
# Cria um dicionario para armazenagem de dados em memoria
todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        try:
            return {todo_id: todos[todo_id]}
        except:
            return {"erro": "Nenhum registro encontrado com id " + todo_id, 
                    "status": 500}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
        
    def post(self, todo_id):
        content = request.get_json(silent=True)
        todos[todo_id] = content
        return {todo_id: content}

    def delete(self, todo_id):
        try:
            del todos[todo_id]
            return todos
        except:
            return {"erro": "Nenhum registro encontrado para remocao com id " + todo_id, 
                    "status": 400}
        
api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)