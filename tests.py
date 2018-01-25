from app import *
import unittest
import requests

class FlaskTestCase(unittest.TestCase):

    def test_index_page(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_car_json(self):
        tester = app.test_client(self)
        response = tester.get('/car/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_car1_json_length(self):
        tester = app.test_client(self)
        response = tester.get('/car/1', content_type='application/json')
        self.assertEqual(response.content_length, 138)

if __name__ == '__main__':
    unittest.main()