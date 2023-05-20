from flask import Flask, render_template,request,redirect,url_for,jsonify
from exts import db
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import User,History,Checkin
from werkzeug.security import generate_password_hash,check_password_hash
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTPRecipientsRefused
from chatgpt import chatgpt
from prompt import messages,dogdic,name
import random
import string
import openai
from datetime import date,datetime
#setup chatgpt api
openai.api_key = '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'
openai.organization = "org-TbfW12zKWBbFDrfoDdtPTlQv"
dicuser={"role": "user", "content": ""}
dicass={"role": "assistant", "content": ""}
#setup email api and SSL
host_server = 'smtp.gmail.com'  
sender_mail = 'test001ceshi@gmail.com'
pwd = 'dslvhouvwuvtvbvw'
mail_title = 'Webchat Authentication code'
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.secret_key='ezra'
migrate=Migrate(app,db)
login_manager=LoginManager()
login_manager.init_app(app)
users=[] # grab all users in the db
emailst=[] # grab all the emails in the db
code={} # store the verification code temporarily
maildress=""
# The code below tests whether the database is connected successfully
""" with app.app_context():
    with db.engine.connect() as conn:
        rs=conn.execute(text("select 1"))
        print(rs.fetchone()) """

# store all the users and emails from database to a list.
with app.app_context():
    allusers=User.query.all()
    for i in allusers:
        users.append(i.username)
        emailst.append(i.email)

# define the login manager
@login_manager.user_loader
def load_user(username):
    return db.session.get(User, username)

# define the route of home page of our website
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

# define the route of login page of our website
@app.route("/login", methods=['POST','GET'])
def login():
    msg=""
    if current_user.is_authenticated: # check whether the user is already logged in. if true, redirect the user to home page.
        return redirect(url_for('index'))
    elif request.method == 'POST':# to get the user's input info and whether the user check the checkbox.
        username = request.form.get("username")
        password = request.form.get("pwd")
        my_checkbox = request.form.get('my-checkbox')
        user=User.query.filter_by(username=username).first()
        if username is not None:
            if username not in users:# if the user's username is not exists, return to register page
                msg="username not found, please register first!"
                return redirect(url_for("register"))
            elif user and check_password_hash(user.password, password):# the user's input matches record
                if my_checkbox == "on":# check whether user checked 'remember me'
                    login_user(user,remember=True)
                    return redirect(url_for('index'))# login success and return to home page
                else:
                    login_user(user,remember=False)
                    return redirect(url_for('index'))
            else:
                msg="Incorrect password, please try again"# user's input not match the database, parse message to html and return to login page again.
                return render_template("login.html",msg=msg)
    return render_template("login.html")

# define the user logout.
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("login.html")

# if the user access login required page before login, return to login page.
@login_manager.unauthorized_handler
def unauthorized():
    # Redirect unauthorized users to the login page
    return redirect(url_for("login"))

# define the route of register page.
@app.route("/register", methods=['POST','GET'])
def register():
    if request.method == 'POST':# get the user's input via POST.
        username = request.form.get('username')
        password = request.form.get('pwd')
        repassword = request.form.get('repwd')
        email = request.form.get("email")
        key = request.form.get("key")
        if username in users: # check whether username exists.
            msg="Username already exists! Please login in!"
            return render_template('login.html',msg=msg,users=users)
        elif password != repassword: # check whether input passwords are same
            msg="The passwords are not the same!"
            return redirect(url_for("register"))
        elif len(password)<=6 or len(password)>=16:# check the length of password
            msg="The length of the password should be more than 6 and less than 15."
            return redirect(url_for("register"))
        elif email not in code.keys() or key!=code[email]:# check whether the email code is correct.
            msg="Invalid Code! please verify your email!"
            return redirect(url_for("register"))
        else: # everything is correct.
            user=User(username=username,password=generate_password_hash(password),email=email)# store the user's info into user table.
            check=Checkin(username=username,checkincount=0)# create a checkin record in checkin table at the same time.
            db.session.add(user)
            db.session.add(check)
            db.session.commit()# update the new records to database.
            users.append(username)# add the new username to list.
            emailst.append(email)# add the new email to list.
            msg="Registeration Successful!"
            return redirect(url_for("login"))
    return render_template('register.html',users=users)

# define the function of sending verification email code.
@app.route("/send", methods=['POST','GET'])
def send():
    email = request.args.get("email")# get the input email.
    if email in emailst:# email has already been used.
        return jsonify({"code":500,"message": "","data":None})
    elif request.method == 'GET':
        verifycode=''.join(random.choices(string.ascii_uppercase + string.digits, k=6))# generate 6 characters verification code.
        code[email]=verifycode# store code to dictionary
        mail_content = verifycode# add the code to mail content
        # the code below use the smtp and SSL to send the code to the input email.
        msg = MIMEMultipart()
        msg["Subject"] = Header(mail_title,'utf-8')
        msg["From"] = sender_mail
        smtp = SMTP_SSL(host_server,465)
        smtp.login(sender_mail,pwd)
        msg.attach(MIMEText(mail_content,'html','utf-8'))
        receiver = [email ]
        msg["To"] = Header(str(receiver),'utf-8')
        print(msg.as_string())
        try:# successfully sent the email
           smtp.sendmail(sender_mail,receiver,msg.as_string())
           return jsonify({"code":200,"message": "","data":verifycode})
        except SMTPRecipientsRefused:# the email is incorrect
           return jsonify({"code":300,"message": "","data":None})

# define the route of reset page.
@app.route("/reset", methods=['POST','GET'])
def reset():
    if request.method == 'POST': # get all the input info
        username = request.form.get('username')
        newpassword = request.form.get('pwd')
        repassword = request.form.get('repwd')
        email = request.form.get("email")
        key = request.form.get("key")
        usr=User.query.filter_by(username=username).first()# get the record from database
        if username not in users:# username not exist
            msg="username not exists! Please register!"
            return render_template("reset.html",users=users,msg=msg)
        elif newpassword != repassword:# different password
            msg="The passwords are not the same!"
            return render_template("reset.html",users=users,msg=msg)
        elif len(newpassword)<=6 or len(newpassword)>=16:# check the length of password
            msg="The length of the password should be more than 6 and less than 15."
            return render_template("reset.html",users=users,msg=msg)
        elif usr.email!=email:# check whether the email match the records in database.
            msg="Email not correct!"
            return render_template("reset.html",users=users,msg=msg)
        elif email not in code.keys():# check whether user has send the email code.
            msg="please send verification code first!"
            return render_template("reset.html",users=users,msg=msg)
        elif key!=code[email]:# check whether the code match the record stored in dictionary.
            msg="incorrect code"
            return render_template("reset.html",users=users,msg=msg)
        else:# pass the verification and correctly reset the password.
            usr.password=generate_password_hash(repassword)# use hash to encode the password.
            db.session.commit() # Update the new password to record in database.
            return redirect(url_for("login"))
    return render_template("reset.html",users=users)

# define the function of sending email verification code in reset page which is similar to the function of sending email verification code in register page.
@app.route("/reset/update", methods=['POST','GET'])
def update():
    email = request.args.get("email")
    username = request.args.get("username")
    if username in users:
        actemail=User.query.filter_by(username=username).first().email
    else:
        actemail=None
    if email not in emailst:#email not exist
        return jsonify({"code":500,"message": "","data":None})
    elif actemail!=email:#email not match the username or username not exist.
        return jsonify({"code":400,"message": "","data":None})
    elif request.method == 'GET':
        # generate the code and send email to user's input email
        verifycode=''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        code[email]=verifycode
        mail_content = verifycode
        msg = MIMEMultipart()
        msg["Subject"] = Header(mail_title,'utf-8')
        msg["From"] = sender_mail
        smtp = SMTP_SSL(host_server,465)
        smtp.login(sender_mail,pwd)
        msg.attach(MIMEText(mail_content,'html','utf-8'))
        receiver = [email ]
        msg["To"] = Header(str(receiver),'utf-8')
        try:
           smtp.sendmail(sender_mail,receiver,msg.as_string())
           return jsonify({"code":200,"message": "","data":verifycode})
        except SMTPRecipientsRefused:
           return jsonify({"code":300,"message": "","data":None})
        
# define the route of chat page.
@app.route("/chat", methods=['POST','GET'])
@login_required
def chat():# parse the username, checkin days and time to html.
    username=current_user.username
    current_time = datetime.now().strftime("%I:%M:%S %p").lower().lstrip("0")
    checkin=Checkin.query.filter_by(username=username).first().checkincount
    return render_template("chat.html",username=username,checkin=checkin,current_time=current_time)

# define the function of getting the user's input question and generate response from Chatgpt API and parse it to front-end via Ajax.
@app.route("/chat/answer", methods=['POST','GET'])
def answer():
    response=""
    username = current_user.username
    question = request.args.get('question')# get the user's input question.
    today = date.today()# get the time
    dicuser["content"]=question # store the question in a dictionary
    messages.append(dicuser)
    response=chatgpt(messages)# get chatgpt's response
    history=History(username=username,content="Q: "+question+" A: "+response,date=today,name=name)# store the history into the history table
    db.session.add(history)
    db.session.commit()# update the new record to database
    dicass["content"]=response# store the answer in a dictionary
    messages.append(dicass)# add the history to prompt to let chatgpt know the history.
    return jsonify({"response":response,"status":"success"}) # parse the response to front-end via Ajax

# define the function of check in days via Ajax.
@app.route("/chat/check", methods=['POST','GET'])
@login_required
def check():
    username=current_user.username
    today = date.today()
    check=Checkin.query.filter_by(username=username).first()# get the previous check in days from database.
    if check.current_login==check.last_login==today:# if the user has already checked in today, keep the count. the "yes" represents the user has already checked in today.
        return jsonify({"counts":check.checkincount,"status":"checked","today":"yes"})
    elif check.current_login==today:
        return jsonify({"counts":check.checkincount,"status":"checked","today":"no"})
    else:
        if check.checkincount is None:# check whether the user has checked before
            check.checkincount=1
        else:
            check.checkincount=check.checkincount+1
        check.last_login=check.current_login
        check.current_login=today
        db.session.commit()
    return jsonify({"counts":check.checkincount,"status":"checked","today":"no"}) # parse the checked days to front-end via ajax.

# define the function of switch dogs.
@app.route("/chat/switch", methods=['POST','GET'])
@login_required
def switch():
    dog=request.args.get("dog")
    global messages
    messages=dogdic[dog]# switch to different prompt based on the dogname.
    global name
    name=dog
    return jsonify({"code":200,"dog":name})

# define the route of history page.
@app.route("/history", methods=['POST','GET'])
@login_required
def history():
    username=current_user.username
    today = date.today()
    return render_template("history.html",username=username,today=today)# parse the username and date to front-end.

# define the function of searching histories.
@app.route("/history/search", methods=['POST','GET'])
@login_required
def search():
    username=current_user.username
    date = request.form.get('date')# get the user's input date
    dogname = request.form.get('dogname')# get the user's input dogname
    if  dogname !='All' and date != "":# use the specific dogname and date to filter the database and get related records
        data = History.query.filter_by(username=username,name=dogname,date=date).all()
        datelist=[]
        doglist=[]
        content=[]
        for row in data:# get the data and store them into a list and parse them to front-end via ajax.
            datelist.append(str(row.date))
            doglist.append(row.name)
            content.append(row.content)
        return jsonify({'date':datelist,'dog':doglist,'content':content,'status':'success1'})
    elif dogname =='All' and date != "":# use the specific date to filter the database and get related records as users select all dogs.
        data = History.query.filter_by(username=username,date=date).all()
        datelist=[]
        doglist=[]
        content=[]
        for row in data:# get the data and store them into a list and parse them to front-end via ajax.
            datelist.append(str(row.date))
            doglist.append(row.name)
            content.append(row.content)
        return jsonify({'date':datelist,'dog':doglist,'content':content,'status':'success2'})
    elif dogname=='All' and date == "":# get all records as users select all dogs and all dates.
        data = History.query.filter_by(username=username).all()
        datelist=[]
        doglist=[]
        content=[]
        for row in data:# get the data and store them into a list and parse them to front-end via ajax.
            datelist.append(str(row.date))
            doglist.append(row.name)
            content.append(row.content)
        return jsonify({'date':datelist,'dog':doglist,'content':content,'status':'success3'})
    else:# use the specific dogname to filter the database and get related records as users select all dates.
        data = History.query.filter_by(username=username,name=dogname).all()
        datelist=[]
        doglist=[]
        content=[]
        for row in data:# get the data and store them into a list and parse them to front-end via ajax.
            datelist.append(str(row.date))
            doglist.append(row.name)
            content.append(row.content)
        return jsonify({'date':datelist,'dog':doglist,'content':content,'status':'success4'})

# define the function of the gaming result. It will add a bonus point to user's account if they finish the game.
@app.route("/chat/game", methods=['POST','GET'])
@login_required
def game():
    username=current_user.username # get the username 
    check=Checkin.query.filter_by(username=username).first()#get the points in the account
    today = date.today()
    if check.current_login == check.last_login == today:
        return jsonify({"counts":check.checkincount,"status":"updated"})
    else:
        check.checkincount=check.checkincount+1 # add 1 point to account
        check.last_login=check.current_login
        db.session.commit()
        return jsonify({"counts":check.checkincount,"status":"success"})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')