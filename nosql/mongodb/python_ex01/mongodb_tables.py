from pymongo import MongoClient

def recuperar_conexao_mongo_db():
    client = MongoClient('mongodb://localhost:27017')
    # Escolher a base de dados
    return client.pymongo_test
    
def exibir_schemas():
    client = MongoClient('mongodb://localhost:27017')
    print('\nExibindo schemas existentes')
    for schema in client.database_names():
        print('{0}'.format(schema))
    
def exibir_tabelas():
    db = recuperar_conexao_mongo_db()
    print('\nExibindo nomes das tabelas')
    for table in db.collection_names():
        print('{0}'.format(table))
    
if __name__ == '__main__':
    exibir_schemas()
    exibir_tabelas()