import unittest
from flask import json
from app import app

class ArithRest(unittest.TestCase):

    test_app = None

    def setUp(self):
        self.app = app.test_client()
        self.test_app = app.test_client()

    def test_sum_remote(self):
        values = [10, 20, 5]
        response = self.test_app.post("/arith/sum",
                                        data = json.dumps(dict(numbers = values)),
                                        content_type = 'application/json')

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, 201)
        self.assertIn("application/json", response.content_type)
        self.assertIn("result", data)                                        
        self.assertEqual(data["result"], 35)

    def test_sum_remote_empty_list(self):
        response = self.test_app.post("/arith/sum",
                                        data = json.dumps(dict(numbers = [])),
                                        content_type = 'application/json')

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, 400)
        self.assertIn("application/json", response.content_type)
        self.assertIn("result", data)                                        
        self.assertEqual(data["result"], 'Empty list')

    def test_sum_remote_invalid_list(self):
        response = self.test_app.post("/arith/sum",
                                        data = json.dumps(dict(numbers = ['a'])),
                                        content_type = 'application/json')

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, 500)
        self.assertIn("application/json", response.content_type)
        self.assertIn("result", data)                                        
        self.assertEqual(data["result"], 'A list of valid numbers must be provided')

    def test_subtract_remote(self):
        values = [10, 20, 5]
        response = self.test_app.post("/arith/subtract",
                                        data = json.dumps(dict(numbers = values)),
                                        content_type = 'application/json')

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, 201)
        self.assertIn("application/json", response.content_type)
        self.assertIn("result", data)                                        
        self.assertEqual(data["result"], -15)

    def test_multiply_remote(self):
        values = [10, 20, 5]
        response = self.test_app.post("/arith/multiply",
                                        data = json.dumps(dict(numbers = values)),
                                        content_type = 'application/json')

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, 201)
        self.assertIn("application/json", response.content_type)
        self.assertIn("result", data)                                        
        self.assertEqual(data["result"], 1000)

    def test_divide_remote(self):
        values = [20, 10, 5]
        response = self.test_app.post("/arith/divide",
                                        data = json.dumps(dict(numbers = values)),
                                        content_type = 'application/json')

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, 201)
        self.assertIn("application/json", response.content_type)
        self.assertIn("result", data)                                        
        self.assertEqual(data["result"], 0.4)

    def test_divide_remote_division_by_zero(self):
        values = [20, 10, 0]
        response = self.test_app.post("/arith/divide",
                                        data = json.dumps(dict(numbers = values)),
                                        content_type = 'application/json')

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, 400)
        self.assertIn("application/json", response.content_type)
        self.assertIn("result", data)                                        
        self.assertEqual(data["result"], 'Division by ZERO is not allowed')

    def test_power_remote(self):
        response = self.test_app.post("/arith/power",
                                        data = json.dumps(dict(number = 2, power = 3)),
                                        content_type = 'application/json')

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, 201)
        self.assertIn("application/json", response.content_type)
        self.assertIn("result", data)                                        
        self.assertEqual(data["result"], 8)