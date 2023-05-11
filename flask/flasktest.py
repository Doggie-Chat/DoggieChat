import unittest
from app import app

'''This class test all the functions related to the login system which includes the login, register and reset page.'''
class Testlogin(unittest.TestCase):
    def setUp(self):# init
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    # This function tests the username and password matches the record in database.
    def test_successful_login(self):
        with app.test_client() as client:
            response = client.post('/login', data=dict(
                username='test1',
                pwd='aaaaaaaa'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'DOGGIE CHAT', response.data)

    # This function tests the correct username and wrong password
    def test_incorrect_password(self):
        with app.test_client() as client:
            response = client.post('/login', data=dict(
                username='test1',
                pwd='wrongpassword'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Incorrect password, please try again', response.data)

    # This function tests the username not exist
    def test_username_not_found(self):
        with app.test_client() as client:
            response = client.post('/login', data=dict(
                username='nonexistentuser',
                pwd='password'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'REGISTER', response.data)
    
    # This function tests the verification for new email registration.
    def test_email_verify_new(self):
        with app.test_client() as client:
            response = client.get('/send?email=abcd@123.com')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["code"], 200)
    
    # This function tests the existed email in register.
    def test_email_verify_exist(self):
        with app.test_client() as client:
            response = client.get('/send?email=2681735200@qq.com')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["code"], 500)
    
    # This function tests the incorrect email in register.
    def test_email_verify_incorrect(self):
        with app.test_client() as client:
            response = client.get('/send?email=abcdefg')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["code"], 300)
    
    # This function tests the correct registration steps.
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

    # This function tests the correct registration steps with wrong email verify key.
    def test_register_incorrect_key(self):
        with app.test_client() as client:
        # Make a request to /send to obtain the verification code
            response_send = client.get('/send?email=abcd@456.com')
            self.assertEqual(response_send.json["code"], 200)
            response_register = client.post('/register', data=dict(
                username='test5',
                pwd='abcdefgh',
                repwd='abcdefgh',
                email='abcd@456.com',
                key='ABCDEF'
            ), follow_redirects=True)# use invalid key
            self.assertEqual(response_register.status_code, 200)
            self.assertIn(b'REGISTER', response_register.data)

    # This function tests the existed username in register.
    def test_register_exist_username(self):
        with app.test_client() as client:
        # Make a request to /send to obtain the verification code
            response_send = client.get('/send?email=abcd@456.com')
            self.assertEqual(response_send.json["code"], 200)
            response_register = client.post('/register', data=dict(
                username='test1',
                pwd='abcdefgh',
                repwd='abcdefgh',
                email='abcd@456.com',
                key='ABCDEF'
            ), follow_redirects=True)# use invalid key as the program will check whether the username exists first and To distinguish it from correctly register.
            self.assertEqual(response_register.status_code, 200)
            self.assertIn(b'LOGIN', response_register.data)
    
    # This function tests the not existed username in reset.
    def test_reset_incorrect_username(self):
        with app.test_client() as client:
            response = client.post('/reset', data=dict(
                username='testnone', # not existed username
                pwd='wrongpassword',
                repwd='wrongpassword',
            ))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'RESET PASSWORD', response.data)
    
    # This function tests the password less than 7 characters in reset.
    def test_reset_incorrect_passwordlength_short(self):
        with app.test_client() as client:
            response = client.post('/reset', data=dict(
                username='test3',
                pwd='short', # password less than 7 characters
                repwd='short',
            ))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'RESET PASSWORD', response.data)
    
    # This function tests the password more than 15 characters in reset.
    def test_reset_incorrect_passwordlength_long(self):
        with app.test_client() as client:
            response = client.post('/reset', data=dict(
                username='test3',
                pwd='longpassword12345',
                repwd='longpassword12345',# password more than 15 characters
            ))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'RESET PASSWORD', response.data)
    
    # This function tests the correct steps in reset.
    def test_reset_verify_email_correctcode(self):
        with app.test_client() as client:
        # Make a request to /reset/update to obtain the verification code
            response_send = client.get('/reset/update?email=2681735200@qq.com&username=test3')
            self.assertEqual(response_send.json["code"], 200)
            verify = response_send.json["data"]
            response_reset = client.post('/reset', data=dict(
                username='test3',
                pwd='bbbbbbbb',
                repwd='bbbbbbbb',
                email='2681735200@qq.com',
                key=verify
            ))# use valid key
            self.assertEqual(response_reset.status_code, 200)
            self.assertIn(b'LOGIN', response_reset.data)
    
    # This function tests correct steps with wrong email verify key in reset.
    def test_reset_verify_email_incorrectcode(self):
        with app.test_client() as client:
        # Make a request to /reset/update to obtain the verification code
            response_send = client.get('/reset/update?email=2681735200@qq.com&username=test3')
            self.assertEqual(response_send.json["code"], 200)
            response_reset = client.post('/reset', data=dict(
                username='test3',
                pwd='aaaaaaaa',
                repwd='aaaaaaaa',
                email='2681735200@qq.com',
                key='abcdef'
            ))# use invalid key
            self.assertEqual(response_reset.status_code, 200)
            self.assertIn(b'RESET PASSWORD', response_reset.data)

'''This class test all the functions related to the chat page.'''
class Testchat(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
    
    # The test below tests whether the chat page would get response if user input the question what is your name. It aims to test whether the answer function works correctly.
    def test_get_answer(self):
        with app.test_client() as client:# login before access the chat page
            response = client.post('/login', data=dict(
                username='test1',
                pwd='aaaaaaaa'
            ), follow_redirects=True)
            self.assertIn(b'DOGGIE CHAT', response.data)
            response_chat=client.get('/chat/answer?question=what is your name?')# parse the question via get.
            self.assertEqual(response_chat.status_code, 200)
            self.assertEqual(response_chat.json["status"], "success")

    # The test below tests whether the check function works in the chat page to record the user's acccumulated checked days.
    def test_get_checked(self):
        with app.test_client() as client:# login before access the chat page
            response = client.post('/login', data=dict(
                username='test1',
                pwd='aaaaaaaa'
            ), follow_redirects=True)
            self.assertIn(b'DOGGIE CHAT', response.data)
            response_chat=client.get('/chat/check')
            self.assertEqual(response_chat.status_code, 200)
            self.assertEqual(response_chat.json["status"], "checked")

    # The test below tests whether the switch function works in the chat page. we parse the dog name Bob here. The dog name in response data should also be Bob.
    def test_dog_switch(self):
        with app.test_client() as client:# login before access the chat page
            response = client.post('/login', data=dict(
                username='test1',
                pwd='aaaaaaaa'
            ), follow_redirects=True)
            self.assertIn(b'DOGGIE CHAT', response.data)
            response_chat=client.get('/chat/switch?dog=Bob')
            self.assertEqual(response_chat.status_code, 200)
            self.assertEqual(response_chat.json["dog"], "Bob")

'''This class test all the functions related to the history page.'''
class Testhistory(unittest.TestCase):
    def setUp(self):# init
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    # The test below tests whether the search function in history page works correctly.
    def test_access_history(self):
        with app.test_client() as client:# login before access the chat page
            response = client.post('/login', data=dict(
                username='test1',
                pwd='aaaaaaaa'
            ), follow_redirects=True)
            self.assertIn(b'DOGGIE CHAT', response.data)
            response_his=client.post('/history/search', data=dict(#test the situation of all date and specified dogname
                date="",
                dogname="Luna"
            ))
            self.assertEqual(response_his.status_code, 200)
            self.assertEqual(response_his.json["status"], "success4")
            response_his=client.post('/history/search', data=dict(#test the situation of all date and all dogname
                date="",
                dogname="All"
            ))
            self.assertEqual(response_his.status_code, 200)
            self.assertEqual(response_his.json["status"], "success3")
            response_his=client.post('/history/search', data=dict(#test the situation of all dogname and specified date
                date="2023-05-05",
                dogname="All"
            ))
            self.assertEqual(response_his.status_code, 200)
            self.assertEqual(response_his.json["status"], "success2")
            response_his=client.post('/history/search', data=dict(#test the situation of specified date and specified dogname
                date="2023-05-05",
                dogname="Luna"
            ))
            self.assertEqual(response_his.status_code, 200)
            self.assertEqual(response_his.json["status"], "success1")

if __name__ == '__main__':
    unittest.main()