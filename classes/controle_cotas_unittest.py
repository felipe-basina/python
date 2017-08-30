# Testes: Controle de contas em disco
import sys
import os
import unittest

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from modulos.controle_cotas import *

class TestControleCotas(unittest.TestCase):

    def setUp(self):
        self.dict = {}
        self.dict['alexandre'] = '456123789'
        self.dict['anderson'] = '1245698456'
        self.dict['antonio'] = '123456456'
        self.dict['carlos'] = '91257581'
        self.dict['cesar'] = '987458'
        self.dict['rosemary'] = '789456125'

    '''
    def test_ler_arquivo_sem_arquivo(self):
        self.assertRaises(Exception, ler_arquivo(''))
    '''
        
    def test_ler_arquivo(self):
        arquivo = 'd:/instalados/python/dev/python/modulos/usuarios.txt'
        tupla = ler_arquivo(arquivo)
        
        self.assertTrue(len(tupla) > 0)
        self.assertEqual(len(tupla), 6)
        
    def test_ordenar_dicionario(self):
        dict = {}
        dict['marcelo'] = '1520'
        dict['amanda'] = '5855'
        dict['wesley'] = '9658'
        
        dict = ordernar_dicionario(dict)
        temp_list = list(dict.items()) # Converte para lista
        
        self.assertEqual(temp_list[0][0], 'amanda')
        self.assertEqual(temp_list[1][0], 'marcelo')
        self.assertEqual(temp_list[2][0], 'wesley')
        self.assertEqual(len(dict), 3)
        
    def test_converter_para_1_mb(self):
        self.assertEqual(converter_para_mb((1024 * 1024)), 1) # 1 MB

    def test_converter_para_2_mb(self):
        self.assertEqual(converter_para_mb((2 * 1024 * 1024)), 2) # 2 MB

    def test_converter_para_10_mb(self):
        self.assertEqual(converter_para_mb((10 * 1024 * 1024)), 10) # 10 MB
        
    def test_calcular_total_mb(self):
        self.assertEqual(round(calcular_total_mb(self.dict), 2), round(2581.57, 2))
        
    def test_calcular_espaco_medio_ocupado(self):
        self.assertEqual(round(calcular_espaco_medio_ocupado(self.dict), 2), round(430.26, 2))
        
    def test_converter_dicionario_para_lista(self):
        lista = converter_dicionario_para_lista(self.dict)
        
        self.assertEqual(len(lista), 6)
        self.assertTrue(isinstance(lista, list))
        
    def test_escrever_conteudo(self):
        arquivo = 'd:/instalados/python/dev/python/modulos/relatório.txt'
        self.assertIsNone(escrever_conteudo(self.dict, arquivo))
        
if __name__ == '__main__':
    unittest.main()