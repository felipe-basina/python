import unittest
from flask import json
from app import app

class FlaskAppCase(unittest.TestCase):

    test_app = None

    def setUp(self):
        self.app = app.test_client()
        self.test_app = app.test_client()

    def test_showMachineList(self):       
        response = self.test_app.get("/")
        self.assertEqual(200, response.status_code)
        self.assertIn("text/html", response.content_type)
    
    def test_getMachineList(self):
        response = self.test_app.post("/getMachineList")
        self.assertEqual(200, response.status_code)
        self.assertIn("text/html", response.content_type)
    
    def test_addMachine(self):
        dict_request = {}
        dict_request['device'] = 'device'
        dict_request['ip'] = 'localhost'
        dict_request['username'] = 'username'
        dict_request['password'] = 'password'
        dict_request['port'] = 110001
        
        response = self.test_app.post("/addMachine", 
                                        data = json.dumps(dict(info = dict_request)), 
                                        content_type = 'application/json')
        
        data = json.loads(response.get_data(as_text = True))
        
        self.assertEqual(200, response.status_code)
        self.assertIn("application/json", response.content_type)
        self.assertIn("message", data)
        self.assertIn("status", data)
        self.assertEqual(data["message"], "inserted successfully")
        self.assertEqual(data["status"], "OK")

if __name__ == '__main__':
    unittest.main()