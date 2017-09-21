import sqlite3
import datetime

class Connect(object):

    tb_name = 'person'

    def __init__(self):
        try:
            #base = ':memory:'
            base = 'dbase'
            # conectando...
            self.conn = sqlite3.connect(base)
            self.cursor = self.conn.cursor()
            print("Banco:", base)
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQLite version: %s" % self.data)
        except sqlite3.Error as e:
            print("Erro ao abrir banco. %s" % e)
            
    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")
            
    def criar_schema(self, schema_name='sql/person_schema.sql'):
        print("Criando tabela %s ..." % self.tb_name)

        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.cursor.executescript(schema)
        except sqlite3.Error:
            print("Aviso: A tabela %s já existe." % self.tb_name)
            return False

        print("Tabela %s criada com sucesso." % self.tb_name)
        
    def inserir_um_registro(self, person):
        try:
            self.cursor.execute("""
            INSERT INTO person (name, username, email, creation_date) values (?, ?, ?, ?)
            """, (person['name'], person['username'], person['email'], datetime.datetime.now()))

            # gravando no bd
            self.commit_db()
            print("Registro inserido com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False

    def recuperar_por_email(self, email):
        try:
            sql = "SELECT * FROM PERSON WHERE EMAIL = " + email
            return self.cursor.execute(sql).fetchone()
        except:
            return {"erro": "Nao foi possivel recuperar registro por email %s" % email}
            
    def recuperar_registros(self):
        try:
            sql = "SELECT * FROM PERSON ORDER BY NAME DESC"
            return self.cursor.execute(sql).fetchall()
        except:
            print("Erro ao recuperar registros")
            return {"erro": "Nao foi possivel recuperar registros"}
            
    def remover_registros(self):
        sql = "DELETE FROM PERSON"
        try:
            self.cursor.execute(sql)
            self.commit_db()
            return("Registros removidos com sucesso")
        except:
            print("Erro ao remover registros")
            return {"erro": "Nao foi possivel remover registros"}