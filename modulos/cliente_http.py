'''
Para instalar a dependencia deve-se seguir com os seguintes passos
1. Acessar o diretorio PYTHON_HOME\Scripts
2. Executar o seguinte comando: easy_install.py requests
2.1 easy_install.py simplejson
'''
import json
import requests

# Consulta a api para recuperar os repositorios do
# usuario especifico
def realizar_get(git_user_name):
    response = requests.get('https://api.github.com/users/' 
        + git_user_name + '/repos')

    #print(response.json())
        
    if response.status_code == 200 and len(response.json()) > 0:
        for repo in response.json():
            print('[{}] {}'.format(repo['language'], repo['name']))
    else:
        print('Nao foi possivel encontrar o repositorio para usuario {%s}. Http status %d'
            % (git_user_name, response.status_code))

def realizar_post(git_user_name, git_password, git_repo_name):
    response = requests.post('https://api.github.com/users/repos', data=json.dumps({'name': git_repo_name}), auth=(git_user_name, git_password))
        
    print(response.json())
     
    if response.status_code == 200:
       print('Repositorio {%s} criado com sucesso' % git_repo_name)
    else:
       print('Nao foi possivel criar o repositorio {%s}' % git_repo_name)

def realizar_delete(git_user_name, git_repo_name):
    response = requests.delete('https://api.github.com/users/repos/' 
        + git_user_name + '/' + git_repo_name)
        
    print(response.json())
     
    if response.status_code == 200:
       print('Repositorio {%s} removido com sucesso' % git_repo_name)
    else:
       print('Nao foi possivel remover o repositorio {%s}' % git_repo_name)
        
if __name__ == '__main__':
    git_user_name = input('Entre com o nome do seu usuario Git: ')
    if git_user_name != '':        
        realizar_get(git_user_name)
    else:
        print('Nenhum usuario definido!')