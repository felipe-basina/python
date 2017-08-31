import sys
import os

# Utilizado para importar corretamente a classe em outro diretorio
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from classes.classe import Pessoa

def testar_metodos_pessoa(nome):
    p = Pessoa(nome)
    print(p.recuperar_nome())
    print(p.cumprimentar())

if __name__ == '__main__':
    nome = input('Entre com seu nome: ')
    testar_metodos_pessoa(nome)