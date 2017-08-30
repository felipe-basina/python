# Projeto: controle de cotas em disco
# https://wiki.python.org.br/ListaDeExerciciosProjetos
import functools
from collections import OrderedDict

def ler_arquivo(arquivo):
    if arquivo == '':
        raise Exception('Um arquivo deve ser definido')
    else:
    
        dict_usuario = {}
    
        try:
            
            with open(arquivo, 'r', encoding='utf-8') as origem:
                for linha in origem:
                    conteudo = linha.split()
                    dict_usuario[conteudo[0]] = conteudo[1]

        except:
            raise Exception('Nao foi possivel realizar a leitura do arquivo %s'
                % arquivo)
                
    return ordernar_dicionario(dict_usuario)
    
def escrever_conteudo(dict_usuario, arquivo):    
    try:
    
        with open(arquivo, 'w') as destino:
            destino.write('ACME Inc.           Uso do espaço em disco pelos usuários\n')
            destino.write('------------------------------------------------------------------------\n')
            destino.write('Nr.  Usuário        Espaço utilizado     % do uso\n\n')
    
            total_bytes = calcular_total_mb(dict_usuario)
    
            indice = 0

            for dados in ordernar_dicionario(dict_usuario).items():
                indice = indice + 1
                login = dados[0]
                espaco_utilizado = converter_para_mb(int(dados[1]))
                espaco_uso = calcular_total_uso(espaco_utilizado, total_bytes)
                
                destino.write("{0:<4} {1:9} {2:12} MB {3:15}%\n"
                    .format(indice, login, espaco_utilizado, espaco_uso))
                
            destino.write('\n')
            destino.write('Espaço total ocupado: %.2f MB\n' % total_bytes)
            destino.write('Espaço médio ocupado: %.2f MB\n' % calcular_espaco_medio_ocupado(dict_usuario))
    
    except Exception as ex:
        print('Erro ao criar arquivo [ %s ]' % str(ex))
    
def ordernar_dicionario(dict):
    return OrderedDict(sorted(dict.items()))
    
def converter_para_mb(total_bytes):
    return round(total_bytes / (1024 * 1024), 2)
    
def calcular_total_mb(dict_usuario):
    return functools.reduce(lambda x, y: x + y, 
        converter_dicionario_para_lista(dict_usuario))   
    
def converter_dicionario_para_lista(dict_usuario):
    return [converter_para_mb(int(tupla[1])) for tupla in list(dict_usuario.items())]
    
def calcular_espaco_medio_ocupado(dict_usuario):
    lista = converter_dicionario_para_lista(dict_usuario)
    return calcular_total_mb(dict_usuario) / len(lista)

def calcular_total_uso(total_uso, total_bytes):
    return round((total_uso / total_bytes) * 100, 2)
    
if __name__ == '__main__':
    diretorio = 'd:/instalados/python/dev/python/modulos/'
    arquivo_origem = diretorio + 'usuarios.txt'
    dict_usuario = ler_arquivo(arquivo_origem)
    
    arquivo_destino = diretorio + 'relatório.txt'
    escrever_conteudo(dict_usuario, arquivo_destino)
    
    print('Arquivo gerado com sucesso!')