import sys
import os
import unittest

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from modulos.operacoes import *

class TestOperacoes(unittest.TestCase):

    def setUp(self):
        pass

    def test_soma_1_9(self):
        self.assertEqual(soma_n_numeros_naturais(9), 45)

    def test_soma_1_10(self):
        self.assertEqual(soma_n_numeros_naturais(10), 55)
        
    def test_ler_arquivo_sucesso(self):
        arquivo = 'operacoes_unittest.py'
        self.assertIsNone(ler_arquivo(arquivo))

    def test_ler_arquivo_falha(self):
        arquivo = 'operacoes.py'
        self.assertIsNotNone(FileNotFoundError, ler_arquivo(arquivo))
        
if __name__ == '__main__':
    unittest.main()