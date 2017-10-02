import sqlite3
import datetime
import os
import traceback

class Connect(object):

    tb_name = 'campanha'
    base = 'campanha_db.db'
    
    def __init__(self, remover_base=True):
        try:        
            if remover_base:
                base_removida = self.remover_base_atual()
                print("Base removida? %s" % base_removida)
            
            self.conn = sqlite3.connect(self.base, detect_types=sqlite3.PARSE_DECLTYPES)
            self.cursor = self.conn.cursor()
            
            self.criar_schema()
            self.set_fk_constraint()
            
            if remover_base:
                self.inserir_registros()
        except sqlite3.Error as e:
            traceback.print_exc()
            print("Erro ao abrir banco. %s" % e)
            
    def set_fk_constraint(self):
        try:
            if self.conn:
                self.cursor.execute('PRAGMA foreign_keys = ON')
            return True
        except Exception as ex:
            traceback.print_exc()
            return False
            
    def get_db_version(self):
        if self.conn:
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQLite version: %s" % self.data)
            return self.data
            
    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")

    def remover_base_atual(self):
        try:
            os.remove(self.base)
            print("Base removida com sucesso!")
            return True
        except:
            print("Nao foi possivel remover a base atual!")
            return False
            
    def criar_schema(self, schema_name='sql/campanha_schema.sql'):
        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.cursor.executescript(schema)
        except sqlite3.Error:
            print("Aviso: A tabela %s já existe." % self.tb_name)
            return False

        print("Tabela %s criada com sucesso." % self.tb_name)
        
    def inserir_registros(self):
        try:
            with open('sql/data.sql', 'rt') as f:
                dados = f.read()
                self.cursor.executescript(dados)
                self.commit_db()
                print("Dados inseridos do arquivo com sucesso.")
        except sqlite3.IntegrityError:
            traceback.print_exc()
            print("Aviso: Erro ao inserir registros")
            return False
        
class CampanhaDb(object):

    def __init__(self, remover_base=True):
        try:
            self.db = Connect(remover_base)
            print("Conectado na base dados!")
        except:
            print("Nao foi possivel se conectar com a base de dados!")
            
    def get_db_version(self):
        return self.db.get_db_version()
        
    def inserir_campanha(self, campanha):
        try:
            sql_insert = "INSERT INTO CAMPANHA (nome_campanha, id_time, dt_inicio_vigencia, dt_fim_vigencia) VALUES (?, ?, ?, ?)"
            
            self.db.cursor.execute(sql_insert, 
                (campanha["nome_campanha"], 
                    campanha["id_time"], 
                    campanha["dt_inicio_vigencia"],
                    campanha["dt_fim_vigencia"]))
                    
            self.db.commit_db()

            return True
        except Exception as ex:
            traceback.print_exc()
            return {"erro": "Nao foi possivel inserir novo registro", "motivo": "Erro %s" % ex}
            
    def atualizar_campanha(self, campanha):
        try:
            sql_update = "UPDATE CAMPANHA SET dt_fim_vigencia = ? WHERE ID = ?"
            
            self.db.cursor.execute(sql_update, 
                (campanha["dt_fim_vigencia"],
                    campanha["id"]))
                    
            self.db.commit_db()

            return True
        except Exception as ex:
            print("Excecao ao atualizar registro %s" % ex)
            return {"erro": "Nao foi possivel atualizar registro", "motivo": "Erro %s" % ex}

    def recuperar_campanhas_filtro(self, dt_inicio_vigencia, dt_fim_vigencia, cliente_id):
        try:
            sql = "SELECT * FROM CAMPANHA WHERE dt_inicio_vigencia >= ? AND dt_fim_vigencia <= ? AND cliente_id = ? ORDER BY dt_fim_vigencia DESC"
        
            return self.db.cursor.execute(sql, (dt_inicio_vigencia, dt_fim_vigencia, cliente_id)).fetchall()
        except:
            return {"campanhas": []}
            
    def recuperar_campanhas(self):
        try:
            sql = "SELECT * FROM CAMPANHA ORDER BY dt_fim_vigencia DESC"
        
            return self.db.cursor.execute(sql).fetchall()
        except Exception as ex:
            print("Excecao %s" % ex)
            return {"campanhas": []}
            
    def recuperar_campanhas_ativas(self, dt_vigencia=datetime.date.today()):
        try:
            sql = "SELECT * FROM CAMPANHA WHERE dt_fim_vigencia >= ? ORDER BY dt_fim_vigencia DESC"
            return self.db.cursor.execute(sql, (dt_vigencia,)).fetchall()
        except Exception as ex:
            print("Excecao %s" % ex)
            traceback.print_exc()
            return {"campanhas": []}
            
    def recuperar_campanhas_por_cliente_id(self, cliente_id):
        try:
            sql = "SELECT * FROM CAMPANHA WHERE cliente_id = ? ORDER BY dt_fim_vigencia DESC"
            return self.db.cursor.execute(sql, (cliente_id,)).fetchall()
        except Exception as ex:
            traceback.print_exc()
            return {"campanhas": []}

    def recuperar_campanha_por_id(self, id):
        try:
            sql = "SELECT * FROM CAMPANHA WHERE id = ?"
            return self.db.cursor.execute(sql, (id,)).fetchone()
        except Exception as ex:
            traceback.print_exc()
            return {"campanhas": []}
            
    def remover_campanha(self, campanha_id):
        try:
            sql_delete = "DELETE FROM CAMPANHA WHERE id = ?"
            self.db.cursor.execute(sql_delete, (campanha_id,))
            self.db.commit_db()
            return True
        except Exception as ex:
            traceback.print_exc()
            return {"erro": "Nao foi possivel remover registro", "motivo": "Erro %s" % ex}
            
    def recuperar_campanhas_por_id_time(self, id_time):
        try:
            sql = "SELECT * FROM CAMPANHA WHERE id_time = ?"
            return self.db.cursor.execute(sql, (id_time,)).fetchall()
        except Exception as ex:
            traceback.print_exc()
            return []
            
class ClienteDb(object):

    def __init__(self, remover_base=True):
        try:
            self.db = Connect(remover_base)
            print("Conectado na base dados!")
        except:
            print("Nao foi possivel se conectar com a base de dados!")
            
    def inserir_cliente(self, cliente):
        try:
            sql_insert = "INSERT INTO CLIENTE (nome_cliente, email, dt_nascimento, id_time) VALUES (?, ?, ?, ?)"
            self.db.cursor.execute(sql_insert, 
                                    (cliente["nome_cliente"],
                                    cliente["email"],
                                    cliente["dt_nascimento"],
                                    cliente["id_time"]))
            self.db.commit_db()
            return True
        except Exception as ex:
            traceback.print_exc()
            return {"erro": "Nao foi possivel cadastrar um novo cliente", "motivo": "Erro %s" % ex}
            
    def recuperar_cliente_por_email(self, email):
        try:
            sql = "SELECT * FROM CLIENTE WHERE email = ?"
            return self.db.cursor.execute(sql, (email,)).fetchone()
        except Exception as ex:
            traceback.print_exc()
            return {"erro": "Nao foi possivel recuperar cliente com email %s" % email, "motivo": "Erro %s" % ex}
            
    def recuperar_clientes(self):
        try:
            sql = "SELECT * FROM CLIENTE ORDER BY dt_cadastro DESC"
            return self.db.cursor.execute(sql,).fetchall()
        except Exception as ex:
            traceback.print_exc()
            return {"erro": "Nao foi possivel recuperar clientes cadastrados", "motivo": "Erro %s" % ex}
            
    def recuperar_times(self):
        try:
            sql = "SELECT * FROM TIIME ORDER BY id"
            return self.db.cursor.execute(sql,).fetchall()
        except Exception as ex:
            traceback.print_exc()
            return {"erro": "Nao foi possivel recuperar times cadastrados", "motivo": "Erro %s" % ex}
            
    def recuperar_time_por_id(self, time_id):
        try:
            sql = "SELECT * FROM TIIME WHERE id = ?"
            return self.db.cursor.execute(sql, (time_id,)).fetchone()
        except Exception as ex:
            traceback.print_exc()
            return {"erro": "Nao foi possivel recuperar time com id %s" % id, "motivo": "Erro %s" % ex}
            
    def remover_cliente_por_id(self, cliente_id):
        try:
            sql_delete = "DELETE FROM CLIENTE WHERE id = ?"
            self.db.cursor.execute(sql_delete, (cliente_id,))
            self.db.commit_db()
            return True
        except Exception as ex:
            traceback.print_exc()
            return {"erro": "Nao foi possivel remover cliente com id %d : %s" % (cliente_id, ex)}