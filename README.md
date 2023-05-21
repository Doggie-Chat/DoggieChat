# 🐶 Doggie Chat

## 💡 Purpose

The purpose of the Doggie Chat web application is to provide a platform for users to interact and chat with AI puppies. Dogs are known to be loyal friends of humans, but it can be challenging to understand their words in the real world. With Doggie Chat, users can engage in conversations and interact with six different AI dogs, each with their own unique personalities.

### Design and Use

The web application is designed with the following components:

#### Opening View

The opening view consists of three main parts:

1. Register: Users need to register an account by providing necessary information, including an email address for verification purposes.
2. Login: Registered users can log in to access the chat and search pages.
3. Reset: In case users forget their password, they can reset it through the reset password page. Users need to provide their email address for verification purpose

<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/4869fbfa-c23d-4ad3-9cf2-0e896c10dbe2" alt="opening" width="70%"/>

<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/9e70d6a0-2e54-44a6-9d60-89c8f678bb9f" alt="login" width="45%"/>
<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/32a03098-7733-4eb2-b934-863eca97a852" alt="register" width="45%"/>
<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/5694e1f2-3a02-4b27-8010-ab17b7747ac1" alt="reset" width="45%"/>
<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/aa349f4c-3510-45d7-931c-ead90ec06fd4" alt="home" width="45%"/>

#### Chat View

The chat view is the main section where users can engage in conversations with the AI dogs. This section is divided into three parts:

1. Dog Selection: Upon logging in, users can choose from three different dogs to chat with. Each dog has its own distinct personality and characteristics.
2. Chat Interface: Once a dog is selected, users can start conversing with the chosen dog. They can exchange messages and have interactive conversations.

<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/fea2fb38-edcc-4e0f-afc5-a589da0cda44" alt="chat-with-three" width="45%"/>
<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/8c944e65-1bab-499c-8323-bfc28c832428" alt="chat-with-six" width="45%"/>

3. Check-in and Mini-games: The chat page also includes a check-in feature. Users can check in once a day, earning one point for each check-in. Additionally, a number guessing mini-game is presented after check-in. Successfully completing the mini-game grants the user an extra point. The mini-game disappears once completed, ensuring users can earn a maximum of two points per day. After earning 15 points or more, the user unlocks the ability to chat with the other three dogs.

<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/52bf2cdb-adfa-41e9-8d66-6bf043c291a9" alt="chat" width="70%"/>
<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/d792cedd-5ce9-4622-acdd-1538f87e0bf4" alt="check-in" width="45%"/>
<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/a2b03685-ad03-426e-a478-1663fc58b18d" alt="mini-game" width="45%"/>



#### Search View

In the search view, users have the ability to search through their historical chat records. They can filter the records based on the dog they interacted with or specific days.

<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/1108c803-b14c-4ac9-a9d9-3e142b12956e" alt="search" width="70%"/>

<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/ae9617d4-794a-4902-bad5-8f9d0960780d" alt="history1" width="45%"/>
<img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/63afd9a9-7f96-46c4-84a0-7dc04a084df6" alt="history2" width="45%"/>

The Doggie Chat web application provides users with an enjoyable and interactive platform to chat with AI puppies. By offering different dogs with unique personalities and incorporating features like check-ins and mini-games, users can have a rewarding experience while engaging with the virtual canine companions.

## ⚙️ Architecture

The Doggie Chat web application follows a client-server architecture, with a simple and lightweight database setup using SQLite. Here is an overview of the application's architecture:

1. **Client-Side**:
   - The client-side of the application is built using HTML, CSS, AJAX, jQuery, and Bootstrap.
   - **HTML**: Provides the structure and content of the web pages.
   - **CSS**: Used for styling the user interface and creating an appealing visual experience.
   - **AJAX**: Enables asynchronous communication between the client and server, allowing for dynamic content updates without requiring a page refresh.
   - **jQuery**: A JavaScript library that simplifies client-side scripting and provides a wide range of useful functions for DOM manipulation and event handling.
   - **Bootstrap**: A popular front-end framework that offers pre-designed CSS and JavaScript components for building responsive and mobile-friendly web applications.

2. **Server-Side**:
   - The server-side of the application is implemented using Python and the Flask framework.
   - Flask is a lightweight web framework that handles the routing, request handling, and response generation.
   - The server interacts with the client through HTTP(S) requests and responses.
   - It handles user registration, login, password reset, and other user-related functionalities.
   - The server also manages the AI chatbot logic, which processes user messages and generates responses.
   - The server communicates with the OpenAI API to utilize the AI models for generating dog-like responses.
   - The server uses Flask-SQLAlchemy to perform CRUD operations in the database.

3. **Database**:
   - The Doggie Chat web application uses SQLite as the database system.
   - SQLite stores user information, chat history, and other relevant data in a single file.
   - It provides a lightweight and efficient solution for managing the application's data without requiring additional database software.
   - Database schema:
   <img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/7b566db6-2cea-4d03-9587-a9cfa6b5384a" alt="schema" width="60%"/>

4. **API Integration**:
   - The Doggie Chat web application integrates with external APIs to enhance its functionality.
   - It utilizes the OpenAI API for the AI chatbot's natural language processing capabilities, allowing the dogs to generate contextually relevant responses.
   - Additionally, an email API is used for sending verification emails, password reset emails, and other email notifications to the users.

5. **Security**:
   - The web application incorporates security measures to protect user data and ensure a secure experience.
   - User passwords are stored using secure hashing techniques, preventing unauthorized access to sensitive information.
   - User authentication and authorization mechanisms are implemented to control access to the application's features and resources.

The Doggie Chat web application architecture provides a simple and efficient platform for users to chat with AI puppies. It leverages client-side technologies like HTML, CSS, AJAX, jQuery, and Bootstrap, along with server-side technologies and database management, to deliver a seamless and engaging user experience.


## 💻 How to launch the web application

To launch the Doggie Chat web application locally, follow these steps:

1. **Set up the environment**:
   - Download and install Python from the official Python website: [python.org](https://www.python.org/downloads/).
   - Install a code editor such as Visual Studio Code (VSCode) from: [code.visualstudio.com](https://code.visualstudio.com/).
   - Clone the repository to your local machine using Git. Open a terminal or command prompt and navigate to the cloned repository directory:
     ```
     git clone <repository_url>
     cd DoggieChat
     ```
   - Create a virtual environment:
     - For Windows (using Command Prompt):
       ```
       python -m venv webchat-env
       ```
     - For Windows (using PowerShell):
       ```
       python -m venv webchat-env
       ```
     - For Unix/Linux:
       ```
       python3 -m venv webchat-env
       ```
   - Activate the virtual environment:
     - For Windows (using Command Prompt):
       ```
       .\webchat-env\Scripts\activate
       ```
     - For Windows (using PowerShell):
       ```
       .\webchat-env\Scripts\Activate.ps1
       ```
     - For Unix/Linux:
       ```
       source webchat-env/bin/activate
       ```

2. **Install required packages**:
   - Make sure you are in the Doggie Chat repository directory with the virtual environment activated.
   - Install the required packages by running the following command:
     ```
     pip install -r requirements.txt
     ```

3. **Configure API Keys**:
   - Obtain your OpenAI API key and email API key.
   - Open the `app.py` file in the code editor.
   - Locate the following lines:
     ```python
     openai.api_key = '' # your openai api key
     openai.organization = '' # your openai organization id
     ```
     Replace the empty strings `''` with your OpenAI API key.
   - Similarly, find the lines:
     ```python
     host_server = ''  # your email host server
     sender_mail = '' # your sender email
     pwd = '' # your sender email key
     ```
     Replace the empty string `''` with your email API key.

4. **Run the application**:
   - Make sure you are still in the Doggie Chat repository directory with the virtual environment activated.
   - Start the application by running the following command:
     ```bash
     cd flask
     flask run
     ```

5. **Access the Doggie Chat web application**:
   - Open your web browser and enter the following URL: `http://localhost:5000`

Now you can enjoy chatting with the AI puppies on the locally hosted Doggie Chat web application. If you encounter any issues, make sure to double-check the steps and ensure that the API keys are correctly configured.


## 🔧 How to run tests
## Unit Tests

Unit tests for the Doggie Chat web application cover three main parts: the login system, chat functionality, and chat history. Here is a description of the unit tests and instructions on how to run them:

### Login System Part

#### Login Page:
- Test the correct login by providing valid credentials.
- Test an incorrect password to verify the error handling.
- Test a non-existent user to ensure appropriate error handling.

#### Register Page:
- Test a correct registration by providing valid user information.
- Test the email verification process for an already registered email.
- Test an incorrect email format to validate the error handling.
- Test an incorrect email verification code to ensure appropriate error handling.
- Test an already existing username to verify the error handling.

#### Reset Page:
- Test a non-existent username to ensure appropriate error handling.
- Test an incorrect password length to validate the error handling.
- Test the correct steps to reset the password.
- Test an incorrect email to verify the error handling.
- Test an incorrect username to ensure appropriate error handling.
- Test an incorrect email verification code to validate the error handling.

### Chat Part

- Test the answer function to ensure the chatbot can reply appropriately to user messages.
- Test the switch function to ensure users can switch between different dogs for chatting.
- Test the check-in functionality to verify if users can successfully check-in.
- Test the game bonus functionality to ensure users receive the bonus point for completing the mini-game.

### History Part

- Test various conditions to search and retrieve the user's chat history.

### Running the Unit Tests:

To run the unit tests for the Doggie Chat web application, follow these steps:

1. Enter the environment with the required packages. Make sure you have all the necessary dependencies installed.
2. Stop running the flask app, by pressing `Ctrl + C`
3. Run the `flasktest.py` script while being in the environment. Make sure you are in the `flask` folder
     ```bash
     python -m tests.flasktest
     ```
 4. Unit tests result:
 <img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/fa037838-a913-413f-ab6c-ba351d1b134c" alt="unittest" width="60%"/>


 
 
Note: The unit tests should succeed during the first run. However, when running the tests again after the initial success, failures may occur in the register test because the new account has already been created in the database during the first run of the test script. If you still want to run the test script multiple times, ensure that you remove the record of the `username test4` from both the `checkin` and `user` tables in the database.

Running the unit tests helps ensure that different parts of the Doggie Chat web application function correctly and as intended. It validates the behavior of the login system, chat functionality, and chat history, providing confidence in the application's overall reliability.

### User tests
User tests simulate users' activities to ensure that the Doggie Chat web application functions correctly. The tests cover all three views: opening, chat, and search. Follow the instructions below to run the user tests:

1. **Ensure Flask Server is Running**:
   - Before running the user tests, make sure that one terminal is running the Flask server. If not, start the server by navigating to the `flask` folder of the Doggie Chat application and executing the following command:
     ```bash
     flask run
     ```

2. **Navigate to the `flask` Folder**:
   - Open a new terminal or command prompt and navigate to the `flask` folder of the Doggie Chat repository. Use the following command:
     ```bash
     cd flask
     ```

3. **Run the User Tests**:
   - Execute the following command to run the user tests:
     ```bash
     python -m tests.usertest
     ```
4. **User Tests Results**:
   - <img src="https://github.com/Doggie-Chat/DoggieChat/assets/82140642/4cf37641-b83d-40ef-b98f-a28ffef3c1c8" alt="usertest" width="60%"/>
 
 
Running the above command will execute the user tests and verify the functionality of the web application. Note that if you want to run the user tests again within the same day, you need to modify the data for the `testuser` in the database. Specifically, you should follow these steps:

1. Access the database used by the Doggie Chat web application.
2. Locate the `checkin` table within the database.
3. Find the row corresponding to the `testuser` account.
4. Update the `last_login` and `current_login` values for the `testuser` to the previous day's date.
   - This step ensures that the functions related to the test mini-game work correctly during subsequent test runs.
5. Save the changes to the database.

## 🗓️ Commit logs

























