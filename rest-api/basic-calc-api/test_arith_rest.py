import unittest
from flask import json
from app import app
from api.arith_rest import EMPTY_LIST, DIVISION_BY_ZERO_NOT_ALLOWED, VALID_NUMBER_LIST

class ArithRest(unittest.TestCase):

    APPLICATION_JSON = "application/json"
    RESULT = "result"
    SUCCESS_STATUS_CODE = 201
    BAD_REQUEST_STATUS_CODE = 400

    test_app = None

    def setUp(self):
        self.app = app.test_client()
        self.test_app = app.test_client()

    def test_sum_remote(self):
        values = [10, 20, 5]
        response = self.test_app.post("/arith/sum",
                                        data = json.dumps(dict(numbers = values)),
                                        content_type = self.APPLICATION_JSON)

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, self.SUCCESS_STATUS_CODE)
        self.assertIn(self.APPLICATION_JSON, response.content_type)
        self.assertIn(self.RESULT, data)                                        
        self.assertEqual(data[self.RESULT], 35)

    def test_sum_remote_empty_list(self):
        response = self.test_app.post("/arith/sum",
                                        data = json.dumps(dict(numbers = [])),
                                        content_type = self.APPLICATION_JSON)

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, self.BAD_REQUEST_STATUS_CODE)
        self.assertIn(self.APPLICATION_JSON, response.content_type)
        self.assertIn(self.RESULT, data)                                        
        self.assertEqual(data[self.RESULT], EMPTY_LIST)

    def test_sum_remote_invalid_list(self):
        response = self.test_app.post("/arith/sum",
                                        data = json.dumps(dict(numbers = ['a'])),
                                        content_type = self.APPLICATION_JSON)

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, 500)
        self.assertIn(self.APPLICATION_JSON, response.content_type)
        self.assertIn(self.RESULT, data)                                        
        self.assertEqual(data[self.RESULT], VALID_NUMBER_LIST)

    def test_subtract_remote(self):
        values = [10, 20, 5]
        response = self.test_app.post("/arith/subtract",
                                        data = json.dumps(dict(numbers = values)),
                                        content_type = self.APPLICATION_JSON)

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, self.SUCCESS_STATUS_CODE)
        self.assertIn(self.APPLICATION_JSON, response.content_type)
        self.assertIn(self.RESULT, data)                                        
        self.assertEqual(data[self.RESULT], -15)

    def test_multiply_remote(self):
        values = [10, 20, 5]
        response = self.test_app.post("/arith/multiply",
                                        data = json.dumps(dict(numbers = values)),
                                        content_type = self.APPLICATION_JSON)

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, self.SUCCESS_STATUS_CODE)
        self.assertIn(self.APPLICATION_JSON, response.content_type)
        self.assertIn(self.RESULT, data)                                        
        self.assertEqual(data[self.RESULT], 1000)

    def test_divide_remote(self):
        values = [20, 10, 5]
        response = self.test_app.post("/arith/divide",
                                        data = json.dumps(dict(numbers = values)),
                                        content_type = self.APPLICATION_JSON)

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, self.SUCCESS_STATUS_CODE)
        self.assertIn(self.APPLICATION_JSON, response.content_type)
        self.assertIn(self.RESULT, data)                                        
        self.assertEqual(data[self.RESULT], 0.4)

    def test_divide_remote_division_by_zero(self):
        values = [20, 10, 0]
        response = self.test_app.post("/arith/divide",
                                        data = json.dumps(dict(numbers = values)),
                                        content_type = self.APPLICATION_JSON)

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, self.BAD_REQUEST_STATUS_CODE)
        self.assertIn(self.APPLICATION_JSON, response.content_type)
        self.assertIn(self.RESULT, data)                                        
        self.assertEqual(data[self.RESULT], DIVISION_BY_ZERO_NOT_ALLOWED)

    def test_power_remote(self):
        response = self.test_app.post("/arith/power",
                                        data = json.dumps(dict(number = 2, power = 3)),
                                        content_type = self.APPLICATION_JSON)

        data = json.loads(response.get_data(as_text = True))
        self.assertEqual(response.status_code, self.SUCCESS_STATUS_CODE)
        self.assertIn(self.APPLICATION_JSON, response.content_type)
        self.assertIn(self.RESULT, data)                                        
        self.assertEqual(data[self.RESULT], 8)