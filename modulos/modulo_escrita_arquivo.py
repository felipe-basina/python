'''
 Exemplo de execução do script:
from modulo_escrita_arquivo import *
arquivo = 'teste1.txt'
conteudo = 'Conteúdo de exemplo para escrita em arquivo!'
escrever_conteudo(conteudo, arquivo)
'''
import os
import codecs

def escrever_conteudo(conteudo, nome_arquivo):
    if not (conteudo or nome_arquivo):
        print('Necessario definir conteudo e arquivo para escrita')
    else:
        try:
        
            nome_arquivo = os.getcwd() + "\\" + nome_arquivo
            
            # w - modulo para escrita em arquivo
            # a - modulo para realizar append
            file_obj = codecs.open(nome_arquivo, 'a', 'utf-8')
            file_obj.write(conteudo + '\n')
            file_obj.close()
        
        except OSError as e:
            print('Erro ao criar arquivo %s: %s' % (nome_arquivo, e))