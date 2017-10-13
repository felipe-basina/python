import unittest
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
    
if __name__ == '__main__':
    unittest.main()