from pymongo import MongoClient

import datetime

# Conectando no servidor local e porta padrao
cliente = MongoClient('localhost', 27017)

# Definindo a base de dados
db = cliente.crud

musica = {"nome": "Nothing left to say",
            "banda": "Imagine Dragons",
            "categorias": ["indie", "rock"],
            "lancamento": datetime.datetime.now()}

# Inserir um registro
resultado = db.album.insert_one(musica)
print('Resultado insercao {0}'.format(resultado))

# Inserir em lote
musicas =  [
                  {
                    "_id": 1,
                    "nome": "Radioactive",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 2,
                    "nome": "Hear Me",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 3,
                    "nome": "Demons",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 4,
                    "nome": "Nothing Left To Say",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 5,
                    "nome": "Amsterdam",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  }
              ]
              
resultado = db.album.insert_many(musicas)
print('Resultado insercao em lote {0}'.format(resultado))

# Recuperar um registro
resultado = db.album.find_one()
print('Resultado recuperar registro:\n{0}'.format(resultado))

# Recuperar registro por filtro
resultado = db.album.find_one({'nome': 'Radioactive'})
print('Resultado recuperar registro por filtro:\n{0}'.format(resultado))

# Recuperar registro por ID
resultado = db.album.find_one({'_id': 3})
print('Resultado recuperar registro por ID:\n{0}'.format(resultado))

# Recuperar todos os registros por ID
for musica_id in range(db.album.count()):
    resultado = db.album.find_one({'_id': musica_id})
    print('Resultado recuperar registro por ID (looping) {0}:\n{1}'
            .format(musica_id, resultado))
            
# Atualizar um registro
resultado = db.album.update_one({'_id': 2}, {'$set': {'nome': 'Novo nome'}})
print('Resultado atualizar registro:\n{0}'.format(resultado))

# Atualizar todos os registros
resultado = db.album.update_many({'banda': 'Imagine Dragons'}, {'$set': {'nome': 'Novo Nome'}})
print('Resultado atualizar todos registros:\n{0}'.format(resultado))

# Remover um registro
resultado = db.album.delete_one({'_id': 2})
print('Resultado remover registro: {0}'.format(resultado))

# Remover todos os registros, por filtro
resultado = db.album.delete_many({'banda': 'Imagine Dragons'})
print('Resultado remover todos registros, por filtro: {0}'.format(resultado))

# Exibindo total de registros existentes
print('Total de registros existentes: {0}'.format(db.album.count()))