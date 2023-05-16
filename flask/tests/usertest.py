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

# #################################################################################################################################
#     # 0. Test the layout page
#     def test_layout_page(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000")  

#         # Check if the page title is correct
#         self.assertIn("Doggie Chat", driver.title)

#         # Check if the logo is displayed
#         logo = driver.find_element_by_xpath("//div[@class='logo']/a/img")
#         self.assertTrue(logo.is_displayed())

#         # Check if the navigation links are displayed
#         nav_links = driver.find_elements_by_xpath("//ul[@class='navbar-nav ml-auto']/li/a")
#         self.assertEqual(len(nav_links), 3)

#         # Check if the "Sign Up" button is displayed
#         signup_button = driver.find_element_by_xpath("//button[contains(text(), 'Sign Up')]")
#         self.assertTrue(signup_button.is_displayed())

#         # Check if the "Log In" button is displayed
#         login_button = driver.find_element_by_xpath("//button[contains(text(), 'Log In')]")
#         self.assertTrue(login_button.is_displayed())

#         # Check if the footer is displayed
#         footer = driver.find_element_by_xpath("//footer/p[@class='footer']")
#         self.assertTrue(footer.is_displayed())


#     def test_navigation_links(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000")

#         # Click on the home link and check the redirect URL
#         home_link = driver.find_element_by_css_selector("a.nav-link[href='home']")
#         driver.execute_script("arguments[0].click();", home_link)
#         redirect_url = driver.current_url
#         self.assertIn("/home", redirect_url)

#         # Click on the chat link and check the redirect URL
#         chat_link = driver.find_element_by_css_selector("a.nav-link[href='chat']")
#         driver.execute_script("arguments[0].click();", chat_link)
#         redirect_url = driver.current_url
#         if not "/login" in redirect_url:
#             self.assertIn("/chat", redirect_url)
#         else:
#             self.assertIn("/login", redirect_url)
#             # Log in with valid credentials
#             username = driver.find_element_by_id("login-username")
#             username.clear()
#             username.send_keys("testuser")

#             password = driver.find_element_by_id("pwd")
#             password.clear()
#             password.send_keys("password123")

#             login_button = driver.find_element_by_xpath("//input[@value='Login']")
#             driver.execute_script("arguments[0].click();", login_button)

#             # Check if the user is redirected to the home page
#             self.assertIn("/home", driver.current_url)

#             # Click on the chat link and check the redirect URL
#             chat_link = driver.find_element_by_css_selector("a.nav-link[href='chat']")
#             chat_link.click()
#             redirect_url = driver.current_url
#             self.assertIn("/chat", redirect_url)
         
#         # Click on the history link and check the redirect URL
#         history_link = driver.find_element_by_css_selector("a.nav-link[href='history']")
#         driver.execute_script("arguments[0].click();", history_link)
#         redirect_url = driver.current_url
#         if not "/login" in redirect_url:
#             self.assertIn("/history", redirect_url)
#         else:
#             self.assertIn("/login", redirect_url)
#             # Log in with valid credentials
#             username = driver.find_element_by_id("login-username")
#             username.clear()
#             username.send_keys("testuser")

#             password = driver.find_element_by_id("pwd")
#             password.clear()
#             password.send_keys("password123")

#             login_button = driver.find_element_by_xpath("//input[@value='Login']")
#             driver.execute_script("arguments[0].click();", login_button)

#             # Check if the user is redirected to the home page
#             self.assertIn("/home", driver.current_url)

#             # Click on the history link and check the redirect URL
#             history_link = driver.find_element_by_css_selector("a.nav-link[href='history']")
#             driver.execute_script("arguments[0].click();", history_link)
#             redirect_url = driver.current_url
#             self.assertIn("/history", redirect_url)

# ################################################################################################################################
#     # 1. Test the home page
#     def test_home_page(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000")

#         # Check if the welcome message is displayed
#         welcome_message = driver.find_element_by_xpath("//h1[@class='intro']")
#         self.assertIsNotNone(welcome_message)

#          # Check if the "Let's chat!" button is present
#         chat_button = driver.find_element_by_xpath("//a[@id='start-chat']")
#         self.assertIsNotNone(chat_button)

#         # Click on the "Let's chat!" button
#         driver.execute_script("arguments[0].click();", chat_button)

#         # Get the redirected URL
#         redirect_url = driver.current_url

#         # Check if the user is redirected to the login page or the chat page based on login status
#         if "/login" in redirect_url:
#             # Log in with valid credentials
#             username = driver.find_element_by_id("login-username")
#             username.clear()
#             username.send_keys("testuser")

#             password = driver.find_element_by_id("pwd")
#             password.clear()
#             password.send_keys("password123")

#             login_button = driver.find_element_by_xpath("//input[@value='Login']")
#             driver.execute_script("arguments[0].click();", login_button)

#             # Check if the user is redirected to the home page
#             self.assertIn("/home", driver.current_url)
#             # Find the chat button on the home page
#             chat_button = driver.find_element_by_xpath("//a[@id='start-chat']")
#             self.assertIsNotNone(chat_button)
#             # Click on the chat button    
#             driver.execute_script("arguments[0].click();", chat_button)
            
#         self.assertIn("/chat", driver.current_url)
# #################################################################################################################################
#     # 2.Test the login page
#     def test_login_success(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/login")  

#         # Test the username field
#         username = driver.find_element_by_id("login-username")
#         username.clear()
#         username.send_keys("testuser")  

#         # Test the password field
#         password = driver.find_element_by_id("pwd")
#         password.clear()
#         password.send_keys("password123")  

#         # Test the remember me checkbox
#         remember_me = driver.find_element_by_id("my-checkbox")
#         if not remember_me.is_selected():
#             driver.execute_script("arguments[0].click();", remember_me)

#         # Test the login button
#         login_button = driver.find_element_by_xpath("//input[@value='Login']")
#         driver.execute_script("arguments[0].click();", login_button)

#         # Add assertions to check successful login
#         self.assertIn("/home", driver.current_url)  
#         self.assertNotIn("login", driver.current_url)  # Ensure we are redirected from the login page

#         # Add additional assertions to check the expected behavior after successful login
#         welcome_message = driver.find_element_by_xpath("//p[@id='Welcome-msg']")
#         self.assertIsNotNone(welcome_message)  # Check if a welcome message is displayed

#         # Check if user information is displayed correctly
#         username_displayed = driver.find_element_by_xpath("//span[@id='username']")
#         self.assertEqual(username_displayed.text, "TESTUSER") 

#         # Check if logout button is present
#         logout_button = driver.find_element_by_xpath("//button[text()='Log Out']")
#         self.assertTrue(logout_button.is_displayed())


#     def test_login_invalid_username(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/login")

#         # Test invalid username
#         username = driver.find_element_by_id("login-username")
#         username.clear()
#         username.send_keys("asdf")  

#         # Provide the password field
#         password = driver.find_element_by_id("pwd")
#         password.clear()
#         password.send_keys("1234567")  

#         # Test the login button
#         login_button = driver.find_element_by_xpath("//input[@value='Login']")
#         driver.execute_script("arguments[0].click();", login_button)

#         # Check if redirected to the register page
#         self.assertEqual('http://127.0.0.1:5000/register', driver.current_url)  


#     def test_login_invalid_password(self):
#         driver = self.driver

#         driver.get("http://127.0.0.1:5000/login")

#         # Provide the username field
#         username = driver.find_element_by_id("login-username")
#         username.clear()
#         username.send_keys("123")       

#         # Test invalid password
#         password = driver.find_element_by_id("pwd")
#         password.clear()
#         password.send_keys("123")  

#         # Test the login button
#         login_button = driver.find_element_by_xpath("//input[@value='Login']")
#         driver.execute_script("arguments[0].click();", login_button)

#         # Add assertions to check if error message is displayed
#         error_message = driver.find_element_by_id("login-error")
#         self.assertIsNotNone(error_message)
#         self.assertEqual(error_message.text, "Incorrect password, please try again") 

#         # Add assertions to check if still on the login page
#         self.assertIn("login", driver.current_url)  # Ensure we are still on the login page

#     def test_login_empty_fields(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/login")

#         # Test empty username and password fields
#         username = driver.find_element_by_id("login-username")
#         username.clear()

#         password = driver.find_element_by_id("pwd")
#         password.clear()

#         # Test the login button
#         login_button = driver.find_element_by_xpath("//input[@value='Login']")
#         driver.execute_script("arguments[0].click();", login_button)

#         # Add assertions to check if error message is displayed
#         username_invalid = driver.execute_script("return document.getElementById('login-username').validity.valid")
#         password_invalid = driver.execute_script("return document.getElementById('pwd').validity.valid")

#         self.assertFalse(username_invalid)  # This should be False, because the username field is invalid (it's empty)
#         self.assertFalse(password_invalid)  # This should be False, because the password field is invalid (it's empty)

#         # Add assertions to check if still on the login page
#         self.assertIn("login", driver.current_url)  # Ensure we are still on the login page


#     def test_remember_me_checkbox(self): # Validates the "Remember me" checkbox's functionality.
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/login")

#         # Check if the "Remember me" checkbox is selected by default
#         remember_me = driver.find_element_by_id("my-checkbox")
#         self.assertTrue(remember_me.is_selected())

#         # Unselect the "Remember me" checkbox
#         driver.execute_script("arguments[0].click();", remember_me)

#         # Check if the "Remember me" checkbox is not selected
#         self.assertFalse(remember_me.is_selected())

#         # Select the "Remember me" checkbox
#         driver.execute_script("arguments[0].click();", remember_me)

#         # Check if the "Remember me" checkbox is selected
#         self.assertTrue(remember_me.is_selected())

#     def test_remember_me_cookie(self): # Checks if the 'remember_token' cookie is set correctly.
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/login")

#         # Fill out the form
#         username = driver.find_element_by_id("login-username")
#         username.clear()
#         username.send_keys("testuser")

#         password = driver.find_element_by_id("pwd")
#         password.clear()
#         password.send_keys("password123")

#         # Select the "Remember me" checkbox
#         remember_me = driver.find_element_by_id("my-checkbox")
#         if not remember_me.is_selected():
#             driver.execute_script("arguments[0].click();", remember_me)

#         # Submit the form
#         login_button = driver.find_element_by_xpath("//input[@value='Login']")
#         driver.execute_script("arguments[0].click();", login_button)

#         # Check if the remember_me cookie is set
#         cookies = driver.get_cookies()
#         remember_me_cookie = [cookie for cookie in cookies if cookie['name'] == 'remember_token']
#         self.assertTrue(len(remember_me_cookie) > 0)

#         # Logout
#         logout_button = driver.find_element_by_xpath("//button[text()='Log Out']")
#         driver.execute_script("arguments[0].click();", logout_button)

#         driver.get("http://127.0.0.1:5000/login")

#         # Fill out the form again
#         username = driver.find_element_by_id("login-username")
#         username.clear()
#         username.send_keys("testuser")

#         password = driver.find_element_by_id("pwd")
#         password.clear()
#         password.send_keys("password123")

#         # Ensure "Remember me" checkbox is not selected
#         remember_me = driver.find_element_by_id("my-checkbox")
#         if remember_me.is_selected():
#             driver.execute_script("arguments[0].click();", remember_me)

#         # Submit the form
#         login_button = driver.find_element_by_xpath("//input[@value='Login']")
#         driver.execute_script("arguments[0].click();", login_button)

#         # Check if the remember_me cookie is not set
#         cookies = driver.get_cookies()
#         remember_me_cookie = [cookie for cookie in cookies if cookie['name'] == 'remember_token']
#         self.assertTrue(len(remember_me_cookie) == 0)


#     def test_forgot_password(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/login")

#         # Find and click the "Forgot password" link
#         forgot_password = driver.find_element_by_link_text("Forget password")
#         driver.execute_script("arguments[0].click();", forgot_password)

#         # Check if the page has been redirected to the reset password page
#         self.assertIn("/reset", driver.current_url)

#     def test_register_link(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/login")

#         # Find and click the "Register" link using CSS selector
#         register_link = driver.find_element_by_css_selector("#register a")
#         driver.execute_script("arguments[0].click();", register_link)

#         # Check if the page has been redirected to the registration page
#         self.assertIn("/register", driver.current_url)

# # #################################################################################################################################
#     # 3.Test the register page
#     def test_register_success(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/register")

#         # Check if the register form is displayed
#         register_form = driver.find_element_by_css_selector("div.register-part form")
#         self.assertTrue(register_form.is_displayed())

#         # Fill out the registration form
#         username = driver.find_element_by_id("register-username")
#         username.clear()
#         username.send_keys("test123") 

#         password = driver.find_element_by_id("register-password")
#         password.clear()
#         password.send_keys("1234567") 

#         confirm_password = driver.find_element_by_id("confirm-register-password")
#         confirm_password.clear()
#         confirm_password.send_keys("0000000")

#         email = driver.find_element_by_id("register-email")
#         email.clear()
#         email.send_keys("usertest@register.com") 

#         # Click the verify button
#         verify_button = driver.find_element_by_id("captcha-btn")
#         driver.execute_script("arguments[0].click();", verify_button)
        
#         try:
#             # Wait for the alert to appear
#             alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
#             # Get the alert text
#             alert_text = alert.text
#             # Handle the alert
#             if alert_text == "Sucessfully send the code!":
#                 # Accept the alert
#                 alert.accept()
#             else:
#                 # Dismiss the alert
#                 alert.dismiss()

#         except TimeoutException:
#             # Handle the case when no alert is present
#             pass

#         # Send a request to generate a verification code
#         response = requests.get("http://127.0.0.1:5000/send", params={"email": "usertest@register.com"}) 
#         data = response.json()

#         # Check the response and get the verification code
#         if data.get("code") == 200 and "data" in data:
#             verification_code = data["data"]
#             # Wait for the verification code input field to be visible
#             code_input = driver.find_element_by_id("register-varify")
#             # Enter the verification code
#             code_input.clear()
#             code_input.send_keys(verification_code)
#             # Submit the registration form
#             submit_button = driver.find_element_by_id("register-submit")
#             # Click the submit button using JavaScript
#             driver.execute_script("arguments[0].click();", submit_button)
#             # Check if the user is redirected to the login page after successful registration
#             self.assertIn("/login", driver.current_url)
#         elif data.get("code") == 500:
#             print("Email is already registered")
#             self.assertIn("/register", driver.current_url)
#             return
#         else:
#             # Handle the case when the verification code generation fails
#             print("Failed to generate verification code")
#             return

#     def test_register_username_exists(self): # Test whether to print an error message if the username exists in the database
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/register")

#         # Fill out the registration form with an existing username
#         username_input = driver.find_element_by_id("register-username")
#         username_input.clear()
#         username_input.send_keys("testuser")

#         # Trigger the onblur event using JavaScript
#         driver.execute_script("arguments[0].blur();", username_input)

#         # Check if the error message is displayed
#         error_message = driver.find_element_by_id("register-username-message")
#         self.assertTrue(error_message.is_displayed())
#         self.assertEqual(error_message.text, "Username already exists!")

#     def test_register_password_not_match(self): # Test whether to print an error message if the password is not match
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/register")

#         # Fill out the registration form with an invalid password
#         password_input = driver.find_element_by_id("register-password")
#         password_input.clear()
#         password_input.send_keys("password123")

#         confirm_password_input = driver.find_element_by_id("confirm-register-password")
#         confirm_password_input.clear()
#         confirm_password_input.send_keys("password456")

#         # Trigger the onblur event using JavaScript
#         driver.execute_script("arguments[0].blur();", confirm_password_input)

#         # Check if the error message is displayed
#         error_message = driver.find_element_by_id("register-password-message")
#         self.assertTrue(error_message.is_displayed())
#         self.assertEqual(error_message.text, "Passwords do not match!")

#     def test_register_password_invalid(self): # Test whether to print an error message if the password is invalid
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/register")

#         # Fill out the registration form with an invalid password
#         password_input = driver.find_element_by_id("register-password")
#         password_input.clear()
#         password_input.send_keys("123")

#         # Fill out the registration form with an invalid password
#         confirm_password_input = driver.find_element_by_id("confirm-register-password")
#         confirm_password_input.clear()
#         confirm_password_input.send_keys("123")

#         # Trigger the onblur event using JavaScript
#         driver.execute_script("arguments[0].blur();", confirm_password_input)

#         # Check if the error message is displayed
#         error_message = driver.find_element_by_id("register-password-message")
#         self.assertTrue(error_message.is_displayed())
#         self.assertEqual(error_message.text, "Password must be between 7 and 15 characters!")

#     def test_register_required_fields(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/register")

#         # Click the Verify button without filling in any input fields
#         verify_button = driver.find_element_by_id("captcha-btn")
#         driver.execute_script("arguments[0].click();", verify_button)

#         # Check if the error message is displayed
#         error_message = driver.find_element_by_id("register-verify-message")
#         self.assertTrue(error_message.is_displayed())
#         self.assertEqual(error_message.text, "Please fill out all required fields.")


# ##################################################################################################################################
#     # 4.Test the reset page
#     def test_reset_success(self): # Test whether the user can successfully reset the password
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/reset")

#         # Check if the register form is displayed
#         reset_form = driver.find_element_by_css_selector("div.reset-part form")
#         self.assertTrue(reset_form.is_displayed())

#         # Fill out the registration form
#         username = driver.find_element_by_id("reset-username")
#         username.clear()
#         username.send_keys("resetuser")

#         password = driver.find_element_by_id("reset-password")
#         password.clear()
#         password.send_keys("0000000")

#         confirm_password = driver.find_element_by_id("confirm-reset-password")
#         confirm_password.clear()
#         confirm_password.send_keys("0000000")

#         email = driver.find_element_by_id("reset-email")
#         email.clear()
#         email.send_keys("usertest@reset.com")

#         # Click the verify button
#         verify_button = driver.find_element_by_id("captcha-btnr")
#         driver.execute_script("arguments[0].click();", verify_button)
        
#         try:
#             # Wait for the alert to appear
#             alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
#             # Get the alert text
#             alert_text = alert.text
#             # Handle the alert
#             if alert_text == "Sucessfully send the code!":
#                 # Accept the alert
#                 alert.accept()
#             else:
#                 # Dismiss the alert
#                 alert.dismiss()

#         except TimeoutException:
#             # Handle the case when no alert is present
#             pass
    
#         # Send a request to generate a verification code
#         response = requests.get("http://127.0.0.1:5000/reset/update", params={"username": "resetuser", "email": "usertest@reset.com"})
#         data = response.json()
    
#         # Check the response data and get the verification code
#         if data.get("code") == 200:
#             verification_code = data["data"]
#             # Enter the verification code
#             code_input = driver.find_element_by_id("reset-varify")
#             code_input.clear()
#             code_input.send_keys(verification_code)
#             # Submit the reset form
#             submit_button = driver.find_element_by_id("reset-submit")
#             # Click the submit button using JavaScript
#             driver.execute_script("arguments[0].click();", submit_button)      
#             # Check if the user is redirected to the login page after successful reset
#             self.assertIn("/login", driver.current_url)
#         else:
#             # Handle the case when the verification code generation fails
#             print("Failed to generate verification code")


#     def test_reset_username_not_exist(self): # Test whether to print an error message if the username does not exist in the database
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/reset")

#         # Fill out the form with a username that is not in the list
#         username = driver.find_element_by_id("reset-username")
#         username.clear()
#         username.send_keys("nonexistentuser")

#          # Trigger the onblur event using JavaScript
#         driver.execute_script("arguments[0].blur();", username)

#         # Check if the error message is displayed
#         error_message = driver.find_element_by_id("reset-username-message")
#         self.assertTrue(error_message.is_displayed())
#         self.assertEqual(error_message.text, "Username does not exist!")


#     def test_reset_invalid_email(self): # Test invalid email address (the email address is not in the database)
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/reset")

#         # Fill out the form with invalid email
#         username = driver.find_element_by_id("reset-username")
#         username.send_keys("testuser")

#         email = driver.find_element_by_id("reset-email")
#         email.send_keys("invalid_email")

#         # Check the response
#         response = requests.get("http://127.0.0.1:5000/reset/update", params={"email": "invalid_email", "username": "testuser"})
#         self.assertEqual(response.json()["code"], 500)

#     def test_non_matching_email_and_username(self): # Test non-matching email and username if the email is in the database
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/reset")

#         # Fill out the form with non-matching email and username
#         username = driver.find_element_by_id("reset-username")
#         username.send_keys("test1")

#         email = driver.find_element_by_id("reset-email")
#         email.send_keys("usertest@reset.com")

#         # Check the response
#         response = requests.get("http://127.0.0.1:5000/reset/update", params={"email": "usertest@reset.com", "username": "test1"})
#         self.assertEqual(response.json()["code"], 400)

#     def test_reset_required_fields(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5000/reset")

#         # Click the Verify button without filling in any input fields
#         verify_button = driver.find_element_by_id("captcha-btnr")
#         driver.execute_script("arguments[0].click();", verify_button)

#         try:
#             # Wait for the alert to appear
#             alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
#             # Get the alert text
#             alert_text = alert.text
#             # Handle the alert
#             if alert_text == "The email address not correct":
#                 # Accept the alert
#                 alert.accept()
#             else:
#                 # Dismiss the alert
#                 alert.dismiss()
#         except TimeoutException:
#             # Handle the case when no alert is present
#             pass

#         # Check if the error message is displayed
#         error_message = driver.find_element_by_id("reset-verify-message")
#         self.assertTrue(error_message.is_displayed())
#         self.assertEqual(error_message.text, "Please fill out all required fields.")
##################################################################################################################################
    ## 4.Test the chat page
 
    # def test_select_different_dogs(self):
    #     driver = self.driver
    #     self.driver.get("http://127.0.0.1:5000/chat")
    #     current_url = driver.current_url
    #     if "/login" in current_url:
    #         # Log in with valid credentials
    #         username = driver.find_element_by_id("login-username")
    #         username.clear()
    #         username.send_keys("testuser")

    #         password = driver.find_element_by_id("pwd")
    #         password.clear()
    #         password.send_keys("password123")

    #         login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #         driver.execute_script("arguments[0].click();", login_button)

    #         # Check if the user is redirected to the home page
    #         self.assertIn("/home", driver.current_url)
    #         # Find the chat button on the home page
    #         chat_button = driver.find_element_by_xpath("//a[@id='start-chat']")
    #         self.assertIsNotNone(chat_button)
    #         # Click on the chat button    
    #         driver.execute_script("arguments[0].click();", chat_button)    
    #         # Check if the user is redirected to the chat page
    #         self.assertIn("/chat", driver.current_url)   

    #     # Switch to Luna tab
    #     luna_tab = self.driver.find_element_by_id("tab_1")
    #     driver.execute_script("arguments[0].click();", luna_tab)

    #     # Click the "Chat with Luna" button
    #     chat_button = self.driver.find_element_by_id("Luna")
    #     driver.execute_script("arguments[0].click();", chat_button)

    #     # Verify the updated content in the chat window
    #     main_chat = self.driver.find_element_by_id("mainchat")
    #     ans_element = main_chat.find_element_by_class_name("Ans")
    #     expected_content = "Woof woof! Hello there, I'm Luna. How can I assist you today?"
    #     actual_content = ans_element.text
    #     self.assertEqual(actual_content, expected_content)

    #     # Verify the current time element is present
    #     time_element = main_chat.find_element_by_class_name("atime")
    #     self.assertIsNotNone(time_element)
               
    #     # Switch to Jack tab
    #     jack_tab = self.driver.find_element_by_id("tab_2")
    #     driver.execute_script("arguments[0].click();", jack_tab)

    #     # Click the "Chat with Jack" button
    #     chat_button = self.driver.find_element_by_id("Jack")
    #     driver.execute_script("arguments[0].click();", chat_button)

    #     # Verify the updated content in the chat window
    #     main_chat = self.driver.find_element_by_id("mainchat")
    #     ans_element = main_chat.find_element_by_class_name("Ans")
    #     expected_content = "Woof woof! Hello there, I'm Jack. How can I assist you today?"
    #     actual_content = ans_element.text
    #     self.assertEqual(actual_content, expected_content)

    #     # Switch to Bob tab
    #     bob_tab = self.driver.find_element_by_id("tab_3")
    #     driver.execute_script("arguments[0].click();", bob_tab)

    #     # Click the "Chat with Bob" button
    #     chat_button = self.driver.find_element_by_id("Bob")
    #     driver.execute_script("arguments[0].click();", chat_button)

 
    #     # Verify the updated content in the chat window
    #     main_chat = self.driver.find_element_by_id("mainchat")
    #     ans_element = main_chat.find_element_by_class_name("Ans")
    #     expected_content = "Woof woof! Hello there, I'm Bob. How can I assist you today?"
    #     actual_content = ans_element.text
    #     self.assertEqual(actual_content, expected_content)

    # def test_chat_with_dog(self):
    #     driver = self.driver
    #     self.driver.get("http://127.0.0.1:5000/chat")
    #     current_url = driver.current_url
    #     if "/login" in current_url:
    #         # Log in with valid credentials
    #         username = driver.find_element_by_id("login-username")
    #         username.clear()
    #         username.send_keys("testuser")

    #         password = driver.find_element_by_id("pwd")
    #         password.clear()
    #         password.send_keys("password123")

    #         login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #         driver.execute_script("arguments[0].click();", login_button)

    #         # Check if the user is redirected to the home page
    #         self.assertIn("/home", driver.current_url)
    #         # Find the chat button on the home page
    #         chat_button = driver.find_element_by_xpath("//a[@id='start-chat']")
    #         self.assertIsNotNone(chat_button)
    #         # Click on the chat button    
    #         driver.execute_script("arguments[0].click();", chat_button)    
    #         # Check if the user is redirected to the chat page
    #         self.assertIn("/chat", driver.current_url)       

    #     # Switch to Luna tab
    #     luna_tab = self.driver.find_element_by_id("tab_1")
    #     driver.execute_script("arguments[0].click();", luna_tab)

    #     # Click the "Chat with Luna" button
    #     chat_button = self.driver.find_element_by_id("Luna")
    #     driver.execute_script("arguments[0].click();", chat_button)

    #     # Simulate user input
    #     chat_input = self.driver.find_element_by_class_name("chat-input")
    #     user_input = "Hi, I am testuser. May I ask about your hobbies?"
    #     chat_input.send_keys(user_input)

    #     # Submit the user input
    #     send_button = self.driver.find_element_by_class_name("chat-send-btn")
    #     self.driver.execute_script("arguments[0].click();", send_button)

    #     sleep(8)
      
    #     # Send a request to generate a response
    #     response = requests.get("http://127.0.0.1:5000/chat/answer", params={"question": user_input})
    #     print(response)

    #     # Retrieve the server response
    #     response_json = response.json()
    #     server_response = response_json["response"]
    #     print(server_response )

    #     # Verify the new response
    #     self.assertIsNotNone(server_response)
    #     self.assertNotEqual(server_response, "Woof woof! Hello there, I'm Luna. How can I assist you today?")

    # def test_login_record(self):
    #     driver = self.driver
    #     self.driver.get("http://127.0.0.1:5000/chat")
    #     current_url = driver.current_url
    #     if "/login" in current_url:
    #         # Log in with valid credentials
    #         username = driver.find_element_by_id("login-username")
    #         username.clear()
    #         username.send_keys("testuser")

    #         password = driver.find_element_by_id("pwd")
    #         password.clear()
    #         password.send_keys("password123")

    #         login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #         driver.execute_script("arguments[0].click();", login_button)

    #         # Check if the user is redirected to the home page
    #         self.assertIn("/home", driver.current_url)
    #         # Find the chat button on the home page
    #         chat_button = driver.find_element_by_xpath("//a[@id='start-chat']")
    #         self.assertIsNotNone(chat_button)
    #         # Click on the chat button    
    #         driver.execute_script("arguments[0].click();", chat_button)    
    #         # Check if the user is redirected to the chat page
    #         self.assertIn("/chat", driver.current_url)      

    #     # Check the presence of the login record section
    #     login_record_section = self.driver.find_element_by_class_name("app-login-record")
    #     self.assertIsNotNone(login_record_section)

    #     # Check the presence of the "Check in" button
    #     check_in_button = self.driver.find_element_by_id("signIn")
    #     self.assertIsNotNone(check_in_button)

    #     # Check the presence and content of the "Check in" button text
    #     check_in_button_text = check_in_button.find_element_by_id("sign-txt").text
    #     self.assertEqual(check_in_button_text, "Check in")

    #     # Check the presence and content of the login days count
    #     login_days_count = check_in_button.find_element_by_id("sign-count").text
    #     self.assertIsNotNone(login_days_count)

    #     # Check the presence of the login record tips
    #     login_record_tips = self.driver.find_element_by_class_name("tips")
    #     self.assertIsNotNone(login_record_tips)

    #     # Check the presence of the calendar section
    #     calendar_section = self.driver.find_element_by_class_name("Calendar")
    #     self.assertIsNotNone(calendar_section)

    #     # Check the presence and content of the year and month
    #     year = calendar_section.find_element_by_id("idCalendarYear").text
    #     month = calendar_section.find_element_by_id("idCalendarMonth").text
    #     self.assertIsNotNone(year)
    #     self.assertIsNotNone(month)

    #     # Check the presence of the calendar table
    #     calendar_table = calendar_section.find_element_by_tag_name("table")
    #     self.assertIsNotNone(calendar_table)

    #     # Check the presence of the calendar table headers
    #     table_headers = calendar_table.find_element_by_tag_name("thead")
    #     self.assertIsNotNone(table_headers)

    #     # Check the presence of the calendar table body
    #     table_body = calendar_table.find_element_by_tag_name("tbody")
    #     self.assertIsNotNone(table_body)
    
    # def test_already_checked_in_today(self):
    #     driver = self.driver
    #     self.driver.get("http://127.0.0.1:5000/chat")
    #     current_url = driver.current_url
    #     if "/login" in current_url:
    #         # Log in with valid credentials
    #         username = driver.find_element_by_id("login-username")
    #         username.clear()
    #         username.send_keys("testuser")

    #         password = driver.find_element_by_id("pwd")
    #         password.clear()
    #         password.send_keys("password123")

    #         login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #         driver.execute_script("arguments[0].click();", login_button)

    #         # Check if the user is redirected to the home page
    #         self.assertIn("/home", driver.current_url)
    #         # Find the chat button on the home page
    #         chat_button = driver.find_element_by_xpath("//a[@id='start-chat']")
    #         self.assertIsNotNone(chat_button)
    #         # Click on the chat button    
    #         driver.execute_script("arguments[0].click();", chat_button)    
    #         # Check if the user is redirected to the chat page
    #         self.assertIn("/chat", driver.current_url)   

    #     # Simulate the user being already checked in
    #     self.driver.execute_script("isSign = true;")

    #     # Click the "Check in" button
    #     check_in_button = self.driver.find_element_by_id("signIn")
    #     driver.execute_script("arguments[0].click();", check_in_button)
        
    #     sleep(1)
    #     # Verify the alert message
    #     alert_message = self.driver.switch_to.alert
    #     self.assertEqual(alert_message.text, "Already Checked In Today")
    #     alert_message.accept()

    #     # Verify that the UI elements are not updated
    #     sign_txt = self.driver.find_element_by_id("sign-txt")
    #     self.assertNotEqual(sign_txt.text, "Success")

    # def test_calendar_navigation(self):
    #     driver = self.driver
    #     self.driver.get("http://127.0.0.1:5000/chat")
    #     current_url = driver.current_url
    #     if "/login" in current_url:
    #         # Log in with valid credentials
    #         username = driver.find_element_by_id("login-username")
    #         username.clear()
    #         username.send_keys("testuser")

    #         password = driver.find_element_by_id("pwd")
    #         password.clear()
    #         password.send_keys("password123")

    #         login_button = driver.find_element_by_xpath("//input[@value='Login']")
    #         driver.execute_script("arguments[0].click();", login_button)

    #         # Check if the user is redirected to the home page
    #         self.assertIn("/home", driver.current_url)
    #         # Find the chat button on the home page
    #         chat_button = driver.find_element_by_xpath("//a[@id='start-chat']")
    #         self.assertIsNotNone(chat_button)
    #         # Click on the chat button    
    #         driver.execute_script("arguments[0].click();", chat_button)    
    #         # Check if the user is redirected to the chat page
    #         self.assertIn("/chat", driver.current_url)   

    #     # Click the "Previous Month" button
    #     prev_button = self.driver.find_element_by_id("idCalendarPre")
    #     driver.execute_script("arguments[0].click();", prev_button)

    #     # Verify that the calendar has moved to the previous month
    #     year_label = self.driver.find_element_by_id("idCalendarYear")
    #     month_label = self.driver.find_element_by_id("idCalendarMonth")
    #     self.assertEqual(month_label.text, "4")  # Update with the expected previous month
    #     self.assertEqual(year_label.text, "2023")  # Update with the expected year

    #     # Click the "Next Month" button
    #     next_button = self.driver.find_element_by_id("idCalendarNext")
    #     driver.execute_script("arguments[0].click();", next_button.click())

    #     # Verify that the calendar has moved to the next month
    #     year_label = self.driver.find_element_by_id("idCalendarYear")
    #     month_label = self.driver.find_element_by_id("idCalendarMonth")
    #     self.assertEqual(month_label.text, "5")  # Update with the expected next month
    #     self.assertEqual(year_label.text, "2023")  # Update with the expected year





##################################################################################################################################
    def tearDown(self):
        self.driver.close()  # Close the current browser window
        self.driver.quit()  # Quit the WebDriver and close every associated window


if __name__ == "__main__":
    unittest.main()