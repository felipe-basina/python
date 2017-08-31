'''
 Para rodar esse exemplo a partir do interpretador deve-se:
 1. Acessar o diretorio onde se encontra o arquivo, no caso, e:\instalados\python\dev\exercicios\classes
 2. Importar o modulo. Ex: from classe import Classe ou from classe import *
 3. Criar uma instancia da classe. Ex: c = Classe('Nome')
 4. Invocar os metodos. Ex: c.recuperar_nome(), c.cumprimentar(), c.alterar_nome()
'''
import datetime
import inspect

# Classe Pessoa
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.ano_nascimento = -1

    def recuperar_nome(self):
        return self.nome
        
    def cumprimentar(self):
        return 'Ola %s' % self.nome
        
    def alterar_nome(self):
        self.nome = input('Entre com o novo nome: ')
        
    def definir_ano_nascimento(self):
        self.ano_nascimento = int(input('Entre com o seu ano de nascimento: '))
        
    def exibir_idade_aproximada(self):
        if self.ano_nascimento > 0:
            hoje = datetime.datetime.now()
            return hoje.year - self.ano_nascimento
        else:
            print('Parece que o ano de nascimento nao foi definido :(')
            pass
            
    def exibir_metodos(self):
        # Por ser uma tupla, recupera somente o primeiro termo
        print([m[0] for m in inspect.getmembers(Pessoa, inspect.isfunction)])

# Classe Teste
class Teste:   
    def imprimir_mensagem(self):
        return 'Ola do Python'
       
    def imprimir_dados_modulo(self):
        print('Nome da classe: %s' % self.__class__)