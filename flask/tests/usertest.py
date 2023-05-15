import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class UserTest(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path=r'/Users/jessiexie/Documents/GitHub/DoggieChat/flask/tests/chromedriver') 
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    # Test the login page
    def test_login_success(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/login")  

        # Test the username field
        username = driver.find_element_by_id("login-username")
        username.clear()
        username.send_keys("123")  

        # Test the password field
        password = driver.find_element_by_id("pwd")
        password.clear()
        password.send_keys("1111111")  

        # Test the remember me checkbox
        remember_me = driver.find_element_by_id("my-checkbox")
        if not remember_me.is_selected():
            remember_me.click()

        # Test the login button
        login_button = driver.find_element_by_xpath("//input[@value='Login']")
        login_button.click()

        # Add assertions to check successful login
        self.assertIn("/home", driver.current_url)  
        self.assertNotIn("login", driver.current_url)  # Ensure we are redirected from the login page

        # Add additional assertions to check the expected behavior after successful login
        welcome_message = driver.find_element_by_xpath("//p[@id='Welcome-msg']")
        self.assertIsNotNone(welcome_message)  # Check if a welcome message is displayed

        # Check if user information is displayed correctly
        username_displayed = driver.find_element_by_xpath("//span[@id='username']")
        self.assertEqual(username_displayed.text, "123") 

        # Check if logout button is present
        logout_button = driver.find_element_by_xpath("//button[text()='Log Out']")
        self.assertTrue(logout_button.is_displayed())

        # Add more assertions as needed to cover the expected behavior after successful login


    # def test_login_invalid_username(self):
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000/login")

    #     # Test invalid username
    #     username = driver.find_element_by_id("login-username")
    #     username.clear()
    #     username.send_keys("asdf")  

    #     # Provide the password field
    #     password = driver.find_element_by_id("pwd")
    #     password.clear()
    #     password.send_keys("1111111")  

    #     # Test the login button
    #     login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #     login_button.click()

    #     # Check if redirected to the register page
    #     self.assertEqual('http://127.0.0.1:5000/register', driver.current_url)  


    # def test_login_invalid_password(self):
    #     driver = self.driver

    #     driver.get("http://127.0.0.1:5000/login")

    #     # Provide the username field
    #     username = driver.find_element_by_id("login-username")
    #     username.clear()
    #     username.send_keys("123")       

    #     # Test invalid password
    #     password = driver.find_element_by_id("pwd")
    #     password.clear()
    #     password.send_keys("123")  

    #     # Test the login button
    #     login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #     login_button.click()

    #     # Add assertions to check if error message is displayed
    #     error_message = driver.find_element_by_id("login-error")
    #     self.assertIsNotNone(error_message)
    #     self.assertEqual(error_message.text, "Incorrect password, please try again") 

    #     # Add assertions to check if still on the login page
    #     self.assertIn("login", driver.current_url)  # Ensure we are still on the login page

    def test_login_empty_fields(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/login")

        # Test empty username and password fields
        username = driver.find_element_by_id("login-username")
        username.clear()

        password = driver.find_element_by_id("pwd")
        password.clear()

        # Test the login button
        login_button = driver.find_element_by_xpath("//input[@value='Login']")
        login_button.click()

        # Add assertions to check if error message is displayed
        username_invalid = driver.execute_script("return document.getElementById('login-username').validity.valid")
        password_invalid = driver.execute_script("return document.getElementById('pwd').validity.valid")

        self.assertFalse(username_invalid)  # This should be False, because the username field is invalid (it's empty)
        self.assertFalse(password_invalid)  # This should be False, because the password field is invalid (it's empty)

        # Add assertions to check if still on the login page
        self.assertIn("login", driver.current_url)  # Ensure we are still on the login page

    def test_remember_me_checkbox(self): # Validates the "Remember me" checkbox's functionality.
        driver = self.driver
        driver.get("http://127.0.0.1:5000/login")

        # Check if the "Remember me" checkbox is selected by default
        remember_me = driver.find_element_by_id("my-checkbox")
        self.assertTrue(remember_me.is_selected())

        # Unselect the "Remember me" checkbox
        remember_me.click()

        # Check if the "Remember me" checkbox is not selected
        self.assertFalse(remember_me.is_selected())

        # Select the "Remember me" checkbox
        remember_me.click()

        # Check if the "Remember me" checkbox is selected
        self.assertTrue(remember_me.is_selected())

    def test_remember_me_cookie(self): # Checks if the 'remember_token' cookie is set correctly.
        driver = self.driver
        driver.get("http://127.0.0.1:5000/login")

        # Fill out the form
        username = driver.find_element_by_id("login-username")
        username.clear()
        username.send_keys("123")

        password = driver.find_element_by_id("pwd")
        password.clear()
        password.send_keys("1111111")

        # Select the "Remember me" checkbox
        remember_me = driver.find_element_by_id("my-checkbox")
        if not remember_me.is_selected():
            remember_me.click()

        # Submit the form
        login_button = driver.find_element_by_xpath("//input[@value='Login']")
        login_button.click()

        # Check if the remember_me cookie is set
        cookies = driver.get_cookies()
        remember_me_cookie = [cookie for cookie in cookies if cookie['name'] == 'remember_token']
        self.assertTrue(len(remember_me_cookie) > 0)

        # Logout
        logout_button = driver.find_element_by_xpath("//button[text()='Log Out']")
        logout_button.click()

        driver.get("http://127.0.0.1:5000/login")

        # Fill out the form again
        username = driver.find_element_by_id("login-username")
        username.clear()
        username.send_keys("123")

        password = driver.find_element_by_id("pwd")
        password.clear()
        password.send_keys("1111111")

        # Ensure "Remember me" checkbox is not selected
        remember_me = driver.find_element_by_id("my-checkbox")
        if remember_me.is_selected():
            remember_me.click()

        # Submit the form
        login_button = driver.find_element_by_xpath("//input[@value='Login']")
        login_button.click()

        # Check if the remember_me cookie is not set
        cookies = driver.get_cookies()
        remember_me_cookie = [cookie for cookie in cookies if cookie['name'] == 'remember_token']
        self.assertTrue(len(remember_me_cookie) == 0)



    def tearDown(self):
        self.driver.close()
        self.driver.quit()  # Close the browser and quit the WebDriver


if __name__ == "__main__":
    unittest.main()


