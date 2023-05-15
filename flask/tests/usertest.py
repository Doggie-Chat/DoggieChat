import unittest
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

class UserTest(unittest.TestCase):


    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path=r'/Users/jessiexie/Documents/GitHub/DoggieChat/flask/tests/chromedriver') 
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


    # # # 0. Test the layout page
    # # def test_layout_page(self):
    # #     driver = self.driver
    # #     driver.get("http://127.0.0.1:5000")  

    # #     # Check if the page title is correct
    # #     self.assertIn("Doggie Chat", driver.title)

    # #     # Check if the logo is displayed
    # #     logo = driver.find_element_by_xpath("//div[@class='logo']/a/img")
    # #     self.assertTrue(logo.is_displayed())

    # #     # Check if the navigation links are displayed
    # #     nav_links = driver.find_elements_by_xpath("//ul[@class='navbar-nav ml-auto']/li/a")
    # #     self.assertEqual(len(nav_links), 3)

    # #     # Check if the "Sign Up" button is displayed
    # #     signup_button = driver.find_element_by_xpath("//button[contains(text(), 'Sign Up')]")
    # #     self.assertTrue(signup_button.is_displayed())

    # #     # Check if the "Log In" button is displayed
    # #     login_button = driver.find_element_by_xpath("//button[contains(text(), 'Log In')]")
    # #     self.assertTrue(login_button.is_displayed())

    # #     # Check if the footer is displayed
    # #     footer = driver.find_element_by_xpath("//footer/p[@class='footer']")
    # #     self.assertTrue(footer.is_displayed())


    # def test_navigation_links(self):
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000")

    #     # Click on the home link and check the redirect URL
    #     home_link = driver.find_element_by_css_selector("a.nav-link[href='home']")
    #     home_link.click()
    #     redirect_url = driver.current_url
    #     self.assertIn("/home", redirect_url)

    #     # Click on the chat link and check the redirect URL
    #     chat_link = driver.find_element_by_css_selector("a.nav-link[href='chat']")
    #     chat_link.click()
    #     redirect_url = driver.current_url
    #     if not "/login" in redirect_url:
    #         self.assertIn("/chat", redirect_url)
    #     else:
    #         self.assertIn("/login", redirect_url)
    #         # Log in with valid credentials
    #         username = driver.find_element_by_id("login-username")
    #         username.clear()
    #         username.send_keys("123")

    #         password = driver.find_element_by_id("pwd")
    #         password.clear()
    #         password.send_keys("1111111")

    #         login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #         login_button.click()

    #         # Check if the user is redirected to the home page
    #         self.assertIn("/home", driver.current_url)

    #         # Click on the chat link and check the redirect URL
    #         chat_link = driver.find_element_by_css_selector("a.nav-link[href='chat']")
    #         chat_link.click()
    #         redirect_url = driver.current_url
    #         self.assertIn("/chat", redirect_url)
         
    #     # Click on the history link and check the redirect URL
    #     history_link = driver.find_element_by_css_selector("a.nav-link[href='history']")
    #     history_link.click()
    #     redirect_url = driver.current_url
    #     if not "/login" in redirect_url:
    #         self.assertIn("/history", redirect_url)
    #     else:
    #         self.assertIn("/login", redirect_url)
    #         # Log in with valid credentials
    #         username = driver.find_element_by_id("login-username")
    #         username.clear()
    #         username.send_keys("123")

    #         password = driver.find_element_by_id("pwd")
    #         password.clear()
    #         password.send_keys("1111111")

    #         login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #         login_button.click()

    #         # Check if the user is redirected to the home page
    #         self.assertIn("/home", driver.current_url)

    #         # Click on the history link and check the redirect URL
    #         history_link = driver.find_element_by_css_selector("a.nav-link[href='history']")
    #         history_link.click()
    #         redirect_url = driver.current_url
    #         self.assertIn("/history", redirect_url)



    # # 1. Test the home page
    # def test_home_page(self):
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000")

    #     # Check if the welcome message is displayed
    #     welcome_message = driver.find_element_by_xpath("//h1[@class='intro']")
    #     self.assertIsNotNone(welcome_message)

    #      # Check if the "Let's chat!" button is present
    #     chat_button = driver.find_element_by_xpath("//a[@id='start-chat']")
    #     self.assertIsNotNone(chat_button)

    #     # Click on the "Let's chat!" button
    #     chat_button.click()

    #     # Get the redirected URL
    #     redirect_url = driver.current_url

    #     # Check if the user is redirected to the login page or the chat page based on login status
    #     if "/login" in redirect_url:
    #         # Log in with valid credentials
    #         username = driver.find_element_by_id("login-username")
    #         username.clear()
    #         username.send_keys("123")

    #         password = driver.find_element_by_id("pwd")
    #         password.clear()
    #         password.send_keys("1111111")

    #         login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #         login_button.click()

    #         # Check if the user is redirected to the home page
    #         self.assertIn("/home", driver.current_url)
    #         # Find the chat button on the home page
    #         chat_button = driver.find_element_by_xpath("//a[@id='start-chat']")
    #         self.assertIsNotNone(chat_button)
    #         # Click on the chat button    
    #         chat_button.click()
            
    #     self.assertIn("/chat", driver.current_url)


    # # 2.Test the login page
    # def test_login_success(self):
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000/login")  

    #     # Test the username field
    #     username = driver.find_element_by_id("login-username")
    #     username.clear()
    #     username.send_keys("123")  

    #     # Test the password field
    #     password = driver.find_element_by_id("pwd")
    #     password.clear()
    #     password.send_keys("1111111")  

    #     # Test the remember me checkbox
    #     remember_me = driver.find_element_by_id("my-checkbox")
    #     if not remember_me.is_selected():
    #         remember_me.click()

    #     # Test the login button
    #     login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #     login_button.click()

    #     # Add assertions to check successful login
    #     self.assertIn("/home", driver.current_url)  
    #     self.assertNotIn("login", driver.current_url)  # Ensure we are redirected from the login page

    #     # Add additional assertions to check the expected behavior after successful login
    #     welcome_message = driver.find_element_by_xpath("//p[@id='Welcome-msg']")
    #     self.assertIsNotNone(welcome_message)  # Check if a welcome message is displayed

    #     # Check if user information is displayed correctly
    #     username_displayed = driver.find_element_by_xpath("//span[@id='username']")
    #     self.assertEqual(username_displayed.text, "123") 

    #     # Check if logout button is present
    #     logout_button = driver.find_element_by_xpath("//button[text()='Log Out']")
    #     self.assertTrue(logout_button.is_displayed())


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

    # def test_login_empty_fields(self):
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000/login")

    #     # Test empty username and password fields
    #     username = driver.find_element_by_id("login-username")
    #     username.clear()

    #     password = driver.find_element_by_id("pwd")
    #     password.clear()

    #     # Test the login button
    #     login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #     login_button.click()

    #     # Add assertions to check if error message is displayed
    #     username_invalid = driver.execute_script("return document.getElementById('login-username').validity.valid")
    #     password_invalid = driver.execute_script("return document.getElementById('pwd').validity.valid")

    #     self.assertFalse(username_invalid)  # This should be False, because the username field is invalid (it's empty)
    #     self.assertFalse(password_invalid)  # This should be False, because the password field is invalid (it's empty)

    #     # Add assertions to check if still on the login page
    #     self.assertIn("login", driver.current_url)  # Ensure we are still on the login page


    # def test_remember_me_checkbox(self): # Validates the "Remember me" checkbox's functionality.
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000/login")

    #     # Check if the "Remember me" checkbox is selected by default
    #     remember_me = driver.find_element_by_id("my-checkbox")
    #     self.assertTrue(remember_me.is_selected())

    #     # Unselect the "Remember me" checkbox
    #     remember_me.click()

    #     # Check if the "Remember me" checkbox is not selected
    #     self.assertFalse(remember_me.is_selected())

    #     # Select the "Remember me" checkbox
    #     remember_me.click()

    #     # Check if the "Remember me" checkbox is selected
    #     self.assertTrue(remember_me.is_selected())

    # def test_remember_me_cookie(self): # Checks if the 'remember_token' cookie is set correctly.
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000/login")

    #     # Fill out the form
    #     username = driver.find_element_by_id("login-username")
    #     username.clear()
    #     username.send_keys("123")

    #     password = driver.find_element_by_id("pwd")
    #     password.clear()
    #     password.send_keys("1111111")

    #     # Select the "Remember me" checkbox
    #     remember_me = driver.find_element_by_id("my-checkbox")
    #     if not remember_me.is_selected():
    #         remember_me.click()

    #     # Submit the form
    #     login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #     login_button.click()

    #     # Check if the remember_me cookie is set
    #     cookies = driver.get_cookies()
    #     remember_me_cookie = [cookie for cookie in cookies if cookie['name'] == 'remember_token']
    #     self.assertTrue(len(remember_me_cookie) > 0)

    #     # Logout
    #     logout_button = driver.find_element_by_xpath("//button[text()='Log Out']")
    #     logout_button.click()

    #     driver.get("http://127.0.0.1:5000/login")

    #     # Fill out the form again
    #     username = driver.find_element_by_id("login-username")
    #     username.clear()
    #     username.send_keys("123")

    #     password = driver.find_element_by_id("pwd")
    #     password.clear()
    #     password.send_keys("1111111")

    #     # Ensure "Remember me" checkbox is not selected
    #     remember_me = driver.find_element_by_id("my-checkbox")
    #     if remember_me.is_selected():
    #         remember_me.click()

    #     # Submit the form
    #     login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #     login_button.click()

    #     # Check if the remember_me cookie is not set
    #     cookies = driver.get_cookies()
    #     remember_me_cookie = [cookie for cookie in cookies if cookie['name'] == 'remember_token']
    #     self.assertTrue(len(remember_me_cookie) == 0)


    # def test_forgot_password(self):
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000/login")

    #     # Find and click the "Forgot password" link
    #     forgot_password = driver.find_element_by_link_text("Forget password")
    #     forgot_password.click()

    #     # Check if the page has been redirected to the reset password page
    #     self.assertIn("/reset", driver.current_url)

    # def test_register_link(self):
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000/login")

    #     # Find and click the "Register" link using CSS selector
    #     register_link = driver.find_element_by_css_selector("#register a")
    #     register_link.click()

    #     # Check if the page has been redirected to the registration page
    #     self.assertIn("/register", driver.current_url)

    # 3.Test the register page
    # def test_register_success(self):
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000/register")

    #     # Check if the register form is displayed
    #     register_form = driver.find_element_by_css_selector("div.register-part form")
    #     self.assertTrue(register_form.is_displayed())

    #     # Fill out the registration form
    #     username = driver.find_element_by_id("register-username")
    #     username.clear()
    #     username.send_keys("test123")

    #     password = driver.find_element_by_id("register-password")
    #     password.clear()
    #     password.send_keys("password123")

    #     confirm_password = driver.find_element_by_id("confirm-register-password")
    #     confirm_password.clear()
    #     confirm_password.send_keys("password123")

    #     email = driver.find_element_by_id("register-email")
    #     email.clear()
    #     email.send_keys("jessiexieee@gmail.com")

    #     # Click the verify button
    #     verify_button = driver.find_element_by_id("captcha-btn")
    #     verify_button.click()
        
    #     try:
    #         # Wait for the alert to appear
    #         alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    #         # Get the alert text
    #         alert_text = alert.text
    #         # Handle the alert
    #         if alert_text == "Sucessfully send the code!":
    #             # Accept the alert
    #             alert.accept()
    #         else:
    #             # Dismiss the alert
    #             alert.dismiss()

    #     except TimeoutException:
    #         # Handle the case when no alert is present
    #         pass

    #     # Send a request to generate a verification code
    #     response = requests.get("http://127.0.0.1:5000/send", params={"email": "jessiexieee@gmail.com"})
    #     data = response.json()


    #     # Check the response and get the verification code
    #     if data.get("code") == 200 and "data" in data:
    #         verification_code = data["data"]
    #         # Wait for the verification code input field to be visible
    #         code_input = driver.find_element_by_id("register-varify")
    #         # Enter the verification code
    #         code_input.clear()
    #         code_input.send_keys(verification_code)

    #         # Submit the registration form
    #         submit_button = driver.find_element_by_id("register-submit")
    #         # Scroll down the page to the submit button
    #         driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    #         sleep(2)
    #         # Click the submit button
    #         submit_button.click()
    #         # Check if the user is redirected to the login page after successful registration
    #         self.assertIn("/login", driver.current_url)
    #     elif data.get("code") == 500:
    #         print("Email is already registered")
    #         self.assertIn("/register", driver.current_url)
    #         return
    #     else:
    #         # Handle the case when the verification code generation fails
    #         print("Failed to generate verification code")
    #         return

    # def test_register_username_exists(self): # Test whether to print an error message if the username exists in the database
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:5000/register")

    #     # Fill out the registration form with an existing username
    #     username_input = driver.find_element_by_id("register-username")
    #     username_input.clear()
    #     username_input.send_keys("test1")

    #     # Trigger the onblur event using JavaScript
    #     driver.execute_script("arguments[0].blur();", username_input)

    #     # Check if the error message is displayed
    #     error_message = driver.find_element_by_id("register-username-message")
    #     self.assertTrue(error_message.is_displayed())
    #     self.assertEqual(error_message.text, "Username already exists!")

    def test_register_password_not_match(self): # Test whether to print an error message if the password is not match
        driver = self.driver
        driver.get("http://127.0.0.1:5000/register")

        # Fill out the registration form with an invalid password
        password_input = driver.find_element_by_id("register-password")
        password_input.clear()
        password_input.send_keys("password123")

        confirm_password_input = driver.find_element_by_id("confirm-register-password")
        confirm_password_input.clear()
        confirm_password_input.send_keys("password456")

        # Trigger the onblur event using JavaScript
        driver.execute_script("arguments[0].blur();", confirm_password_input)

        # Check if the error message is displayed
        error_message = driver.find_element_by_id("register-password-message")
        self.assertTrue(error_message.is_displayed())
        self.assertEqual(error_message.text, "Passwords do not match!")

    def test_register_password_invalid(self): # Test whether to print an error message if the password is invalid
        driver = self.driver
        driver.get("http://127.0.0.1:5000/register")

        # Fill out the registration form with an invalid password
        password_input = driver.find_element_by_id("register-password")
        password_input.clear()
        password_input.send_keys("123")

        # Fill out the registration form with an invalid password
        confirm_password_input = driver.find_element_by_id("confirm-register-password")
        confirm_password_input.clear()
        confirm_password_input.send_keys("123")
        
        # Trigger the onblur event using JavaScript
        driver.execute_script("arguments[0].blur();", confirm_password_input)

        # Check if the error message is displayed
        error_message = driver.find_element_by_id("register-password-message")
        self.assertTrue(error_message.is_displayed())
        self.assertEqual(error_message.text, "Password must be between 7 and 15 characters!")

   

    def tearDown(self):
        self.driver.close()
        self.driver.quit()  # Close the browser and quit the WebDriver


if __name__ == "__main__":
    unittest.main()


