import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from modulos.operacoes import *
    
if __name__ == '__main__':
    while(True):        
        try:      
            numero = int(input('Entre com um numero inteiro: '))
            print(soma_n_numeros_naturais(numero))
        except KeyboardInterrupt:
            print('\n\nPrograma finalizado com sucesso!')
            sys.exit(0)
        except:
            print('Voce nao digitou um numero valido. Vamos de novo!')