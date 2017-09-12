'''
 Exercicio adaptado do site:
 http://www.mkyong.com/mongodb/java-mongodb-hello-world-example/
'''
from pymongo import MongoClient

def recuperar_conexao_mongo_db():
    client = MongoClient('mongodb://localhost:27017')
    # Escolher a base de dados
    return client.user_test
    
def inserir_registros():
    db = recuperar_conexao_mongo_db().users
    
    for indice in range(1, 11):
        user_data = {
            'id': int(indice),
            'profissao': 'PROFISSAO - ' + str(indice),
            'nome': 'NOME - ' + str(indice),
        }
        db.insert_one(user_data)
    
def exibir_registros():
    db = recuperar_conexao_mongo_db().users
    
    cursor = db.find({})
    for document in cursor:
        #print(document)
        print("{0} {1} {2}".format(document['id'], 
            document['profissao'], 
            document['nome']))
        
def remover_registros():
    db = recuperar_conexao_mongo_db().users
    db.remove({})
    
if __name__ == '__main__':
    remover_registros()
    inserir_registros()
    exibir_registros()
