import sqlite3
import datetime

class Connect(object):

    tb_name = 'campanha'

    def __init__(self):
        try:
            base = 'campanha_db.db'
            self.conn = sqlite3.connect(base)
            self.cursor = self.conn.cursor()
            print("Banco:", base)
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQLite version: %s" % self.data)
            self.criar_schema()
        except sqlite3.Error as e:
            print("Erro ao abrir banco. %s" % e)
            
    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")

    def criar_schema(self, schema_name='sql/campanha_schema.sql'):
        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.cursor.executescript(schema)
        except sqlite3.Error:
            print("Aviso: A tabela %s já existe." % self.tb_name)
            return False

        print("Tabela %s criada com sucesso." % self.tb_name)