import unittest
import json
from app import app, service_name

class ServiceNameTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_service_name(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('service_name', data)
        self.assertEqual(data['service_name'], service_name)

if __name__ == '__main__':
    unittest.main()
