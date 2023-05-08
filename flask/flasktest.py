from flask import url_for
from werkzeug.security import generate_password_hash
import unittest
from app import app
from config import Config

class Testlogin(unittest.TestCase):
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
            response = client.get('/send?email=abcd@123.com')
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
    
    def test_register_correct(self):
        with app.test_client() as client:
        # Make a request to /send to obtain the verification code
            response_send = client.get('/send?email=abcd@123.com')
            self.assertEqual(response_send.json["code"], 200)
            verify = response_send.json["data"]

        # Make a request to /register with the obtained verification code
            response_register = client.post('/register', data=dict(
                username='test4',
                pwd='abcdefgh',
                repwd='abcdefgh',
                email='abcd@123.com',
                key=verify
            ), follow_redirects=True)
            self.assertEqual(response_register.status_code, 200)
            self.assertIn(b'LOGIN', response_register.data)

    def test_register_incorrect_key(self):
        with app.test_client() as client:
        # Make a request to /send to obtain the verification code
            response_send = client.get('/send?email=abcd@456.com')
            self.assertEqual(response_send.json["code"], 200)
            verify = response_send.json["data"]

            response_register = client.post('/register', data=dict(
                username='test5',
                pwd='abcdefgh',
                repwd='abcdefgh',
                email='abcd@456.com',
                key='ABCDEF'
            ), follow_redirects=True)# use invalid key
            self.assertEqual(response_register.status_code, 200)
            self.assertIn(b'REGISTER', response_register.data)

    def test_register_exist_username(self):
        with app.test_client() as client:
        # Make a request to /send to obtain the verification code
            response_send = client.get('/send?email=abcd@456.com')
            self.assertEqual(response_send.json["code"], 200)
            verify = response_send.json["data"]

            response_register = client.post('/register', data=dict(
                username='test1',
                pwd='abcdefgh',
                repwd='abcdefgh',
                email='abcd@456.com',
                key='ABCDEF'
            ), follow_redirects=True)# use invalid key as the program will check whether the username exists first and To distinguish it from correctly register.
            self.assertEqual(response_register.status_code, 200)
            self.assertIn(b'LOGIN', response_register.data)
    
if __name__ == '__main__':
    unittest.main()