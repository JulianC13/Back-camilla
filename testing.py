import os
import unittest
from flask import Flask
from camilla import app  

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_search(self):
        response = self.app.get('/search')
        self.assertEqual(response.status_code, 200)

    def test_not_found(self):
        response = self.app.get('/app')
        self.assertEqual(response.status_code, 404)
    
    def test_post(self):
        response = self.app.post('/search')
        self.assertEqual(response.status_code, 405)

    def test_put(self):
        response = self.app.put('/search')
        self.assertEqual(response.status_code, 405)

    def test_delete(self):
        response = self.app.put('/search')
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()
