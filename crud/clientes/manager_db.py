import os
import sqlite3
import io
import datetime
import names
import csv
from gen_random_values import *


class Connect(object):

    def __init__(self, db_name):
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            print("Banco:", db_name)
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQLite version: %s" % self.data)
        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")


class ClientesDb(object):

    tb_name = 'clientes'

    def __init__(self):
        self.db = Connect('clientes.db')
        self.tb_name

    def fechar_conexao(self):
        self.db.close_db()
        
    def criar_schema(self, schema_name='sql/clientes_schema.sql'):
        print("Criando tabela %s ..." % self.tb_name)

        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print("Aviso: A tabela %s já existe." % self.tb_name)
            return False

        print("Tabela %s criada com sucesso." % self.tb_name)

    def inserir_um_registro(self):
        try:
            self.db.cursor.execute("""
            INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES ('Regis da Silva', 35, '12345678901', 'regis@email.com', '(11) 9876-5342',
            'São Paulo', 'SP', '2014-07-30 11:23:00.199000')
            """)
            # gravando no bd
            self.db.commit_db()
            print("Um registro inserido com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False
        
    def inserir_com_lista(self):
        # criando uma lista de dados
        lista = [('Agenor de Sousa', 23, '12345678901', 'agenor@email.com',
                  '(10) 8300-0000', 'Salvador', 'BA', '2014-07-29 11:23:01.199001'),
                 ('Bianca Antunes', 21, '12345678902', 'bianca@email.com',
                  '(10) 8350-0001', 'Fortaleza', 'CE', '2014-07-28 11:23:02.199002'),
                 ('Carla Ribeiro', 30, '12345678903', 'carla@email.com',
                  '(10) 8377-0002', 'Campinas', 'SP', '2014-07-28 11:23:03.199003'),
                 ('Fabiana de Almeida', 25, '12345678904', 'fabiana@email.com',
                  '(10) 8388-0003', 'São Paulo', 'SP', '2014-07-29 11:23:04.199004'),
                 ]
        try:
            self.db.cursor.executemany("""
            INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES (?,?,?,?,?,?,?,?)
            """, lista)
            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos da lista com sucesso: %s registros." %
                  len(lista))
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False
        
    def inserir_de_arquivo(self):
        try:
            with open('sql/clientes_dados.sql', 'rt') as f:
                dados = f.read()
                self.db.cursor.executescript(dados)
                # gravando no bd
                self.db.commit_db()
                print("Dados inseridos do arquivo com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False
            
    def inserir_de_csv(self, file_name='csv/clientes.csv'):
        try:
            reader = csv.reader(
                open(file_name, 'rt'), delimiter=',')
            linha = (reader,)
            for linha in reader:
                self.db.cursor.execute("""
                INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
                VALUES (?,?,?,?,?,?,?,?)
                """, linha)
            # gravando no bd
            self.db.commit_db()
            print("Dados importados do csv com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False
            
    def inserir_com_parametros(self):
        # solicitando os dados ao usuário
        self.nome = input('Nome: ')
        self.idade = input('Idade: ')
        self.cpf = input('CPF: ')
        self.email = input('Email: ')
        self.fone = input('Fone: ')
        self.cidade = input('Cidade: ')
        self.uf = input('UF: ') or 'SP'
        date = datetime.datetime.now().isoformat(" ")
        self.criado_em = input('Criado em (%s): ' % date) or date

        try:
            self.db.cursor.execute("""
            INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES (?,?,?,?,?,?,?,?)
            """, (self.nome, self.idade, self.cpf, self.email, self.fone,
                  self.cidade, self.uf, self.criado_em))
            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False

if __name__ == '__main__':
    c = ClientesDb()
    c.criar_schema()
    c.inserir_um_registro()
    c.inserir_com_lista()
    c.inserir_de_arquivo()
    c.inserir_de_csv()
    c.inserir_com_parametros()