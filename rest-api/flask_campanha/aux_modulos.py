from connect_db import *

import datetime
import traceback

def converter_campanhas_para_json(campanhas):
    campanha_lista = []

    if campanhas:
        for id, nome, id_time, dt_inicio, dt_fim in campanhas:
            dict = {}
            dict['id'] = id
            dict['nome_campanha'] = nome
            dict['id_time'] = id_time
            dict['dt_inicio_vigencia'] = dt_inicio.strftime('%d/%m/%Y')
            dict['dt_fim_vigencia'] = dt_fim.strftime('%d/%m/%Y')
            
            campanha_lista.append(dict)
                
    return campanha_lista
    
def converter_clientes_para_json(clientes):
    cliente_lista = []

    if clientes:
        for id, nome, email, dt_nascimento, id_time, dt_cadastro in clientes:
            dict = {}
            dict['id'] = id
            dict['nome_cliente'] = nome
            dict['email'] = email
            dict['dt_nascimento'] = dt_nascimento.strftime('%d/%m/%Y')
            dict['id_time'] = id_time
            
            dt_cadastro_ts = datetime.datetime.strptime(dt_cadastro, '%Y-%m-%d %H:%M:%S')
            dict['dt_cadastro'] = dt_cadastro_ts.strftime('%d/%m/%Y %H:%M:%S')
            
            cliente_lista.append(dict)
                
    return cliente_lista

def converter_times_para_json(times):
    time_lista = []

    if times:
        for id, nome in times:
            dict = {}
            dict['id'] = id
            dict['nome_time'] = nome
            
            time_lista.append(dict)
                
    return time_lista
    
def recuperar_campanhas_por_id_time(id_time):
    try:
        db = CampanhaDb(False)
        campanhas = db.recuperar_campanhas_por_id_time(id_time)
        return converter_campanhas_para_json(campanhas)
    except Exception as ex:
        traceback.print_exc()
        return []