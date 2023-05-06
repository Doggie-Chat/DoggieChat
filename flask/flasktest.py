from flask import url_for
from werkzeug.security import generate_password_hash
import unittest
from app import app
from models import User
from config import Config

class Testunits(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config.from_object(Config)
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def test_successful_login(self):
        with app.test_client() as client:
            response = client.post('/login', data=dict(
                username='test1',
                pwd='aaaaaaaa'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'DOGGIE CHAT', response.data)

    def test_incorrect_password(self):
        with app.test_client() as client:
            response = client.post('/login', data=dict(
                username='test1',
                pwd='wrongpassword'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Incorrect password, please try again', response.data)

    def test_username_not_found(self):
        with app.test_client() as client:
            response = client.post('/login', data=dict(
                username='nonexistentuser',
                pwd='password'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'REGISTER', response.data)
    
    def test_email_verify_new(self):
        with app.test_client() as client:
            response = client.get('/send?email=1044739111@qq.com')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["code"], 200)

    def test_email_verify_exist(self):
        with app.test_client() as client:
            response = client.get('/send?email=2681735200@qq.com')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["code"], 500)
    
    def test_email_verify_incorrect(self):
        with app.test_client() as client:
            response = client.get('/send?email=abcdefg')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["code"], 300)

if __name__ == '__main__':
    unittest.main()