import unittest
from flask import json
from cpf_blacklist import app

class CpfBlacklistCase(unittest.TestCase):

    test_app = None

    def setUp(self):
        self.test_app = app.test_client()
        
    def test_verificar_cpf_blacklist_sem_cpf(self):       
        response = self.test_app.get("/")

        data = json.loads(response.get_data(as_text = True))
        
        self.assertEqual(200, response.status_code)
        self.assertIn("application/json", response.content_type)
        self.assertEqual("RUNNING", data)
        
    def test_verificar_cpf_blacklist_cpf_em_blacklist_sem_caracteres_especiais(self):       
        response = self.test_app.get("/00000000000")

        data = json.loads(response.get_data(as_text = True))
        
        self.assertEqual(200, response.status_code)
        self.assertIn("application/json", response.content_type)
        self.assertEqual("BLOCK", data)
        
    def test_verificar_cpf_blacklist_cpf_em_blacklist_com_caracteres_especiais(self):       
        response = self.test_app.get("/000.000.000-00")

        data = json.loads(response.get_data(as_text = True))
        
        self.assertEqual(200, response.status_code)
        self.assertIn("application/json", response.content_type)
        self.assertEqual("BLOCK", data)

    def test_verificar_cpf_blacklist_cpf_nao_blacklist_sem_caracteres_especiais(self):       
        response = self.test_app.get("/26347271940")

        data = json.loads(response.get_data(as_text = True))
        
        self.assertEqual(200, response.status_code)
        self.assertIn("application/json", response.content_type)
        self.assertEqual("FREE", data)
        
    def test_verificar_cpf_blacklist_cpf_nao_blacklist_com_caracteres_especiais(self):       
        response = self.test_app.get("/263.472.719-40")

        data = json.loads(response.get_data(as_text = True))
        
        self.assertEqual(200, response.status_code)
        self.assertIn("application/json", response.content_type)
        self.assertEqual("FREE", data)
        
    def test_verificar_cpf_blacklist_parametro_invalido(self):       
        response = self.test_app.get("/parametro")

        data = json.loads(response.get_data(as_text = True))
        
        self.assertEqual(200, response.status_code)
        self.assertIn("application/json", response.content_type)
        self.assertEqual("RUNNING", data)
        
if __name__ == '__main__':
    unittest.main()