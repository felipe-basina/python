# Mongodb
from pymongo import MongoClient
import datetime

# Padrao para conectar na base em localhost
# client = MongoClient() 
# client = MongoClient('localhost', 27017)

def recuperar_conexao_mongo_db():
    client = MongoClient('mongodb://localhost:27017')
    # Escolher a base de dados
    return client.pymongo_test
    
    
def inserir_registro():
    posts = recuperar_conexao_mongo_db().posts

    post_data = {
        'title': 'Python and MongoDB',
        'content': 'PyMongo is fun, you guys',
        'author': 'Scott',
        'creation-date': datetime.datetime.now()
    }
    
    result = posts.insert_one(post_data)
    print('One post: {0}'.format(result.inserted_id))

def listar_registros():
    posts = recuperar_conexao_mongo_db().posts
    
    cursor = posts.find({})
    for document in cursor:
        #print(document)
        print("{0} - {1}".format(document['title'], document['author']))
        
def remover_registros():
    posts = recuperar_conexao_mongo_db().posts
    posts.remove({})
    
if __name__ == '__main__':
    remover_registros()
    inserir_registro()
    listar_registros()