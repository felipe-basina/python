from app import app, db
from app.models import User, Post

'''
 Utilizado para que se possa iniciar
 o flask shell e nao ter a necessidade
 de sempre importar os pacotes para realizacao
 de testes. Comando: flask shell
'''
@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}
