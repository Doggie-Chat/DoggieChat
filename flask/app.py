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
import time
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
# test whether the database is connected successfully
""" with app.app_context():
    with db.engine.connect() as conn:
        rs=conn.execute(text("select 1"))
        print(rs.fetchone()) """

""" users=[]
ppl={}
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username """

with app.app_context():
    allusers=User.query.all()
    for i in allusers:
        users.append(i.username)
        emailst.append(i.email)

""" with app.app_context():
    db.create_all()   """

@login_manager.user_loader
def load_user(username):
    return db.session.get(User, username)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():
    msg=""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    elif request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("pwd")
        my_checkbox = request.form.get('my-checkbox')
        user=User.query.filter_by(username=username).first()
        if username is not None:
            if username not in users:
                return redirect(url_for("register"))
            elif user and check_password_hash(user.password, password):
                if my_checkbox == "on":
                    login_user(user,remember=True)
                    return redirect(url_for('index'))
                else:
                    login_user(user,remember=False)
                    return redirect(url_for('index'))
            else:
                msg="Incorrect password, please try again"
                return render_template("login.html",msg=msg)
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("login.html")

@login_manager.unauthorized_handler
def unauthorized():
    # Redirect unauthorized users to the login page
    return redirect(url_for("login"))

@app.route("/register", methods=['POST','GET'])
def register():
    msg=""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')
        repassword = request.form.get('repwd')
        email = request.form.get("email")
        key = request.form.get("key")
        if username in users:
            msg="Username already exists! Please login in!"
            return render_template('login.html')
        elif password != repassword:
            msg="The passwords are not the same!"
            return redirect(url_for("register"))
        elif len(password)<=6 or len(password)>=16:
            msg="The length of the password should be more than 6 and less than 15."
            return redirect(url_for("register"))
        elif email not in code.keys() or key!=code[email]:
            msg="Invalid Code! please verify your email!"
            return redirect(url_for("register"))
        else:
            user=User(username=username,password=generate_password_hash(password),email=email)
            check=Checkin(username=username,checkincount=0)
            db.session.add(user)
            db.session.add(check)
            db.session.commit()
            users.append(username)
            emailst.append(email)
            msg="Registeration Successful!"
            return redirect(url_for("login"))
    return render_template('register.html', users=users)

@app.route("/send", methods=['POST','GET'])
def send():
    email = request.args.get("email")
    if email in emailst:
        return jsonify({"code":500,"message": "","data":None})
    elif request.method == 'GET':
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
        print(msg.as_string())
        try:
           smtp.sendmail(sender_mail,receiver,msg.as_string())
           return jsonify({"code":200,"message": "","data":verifycode})
        except SMTPRecipientsRefused:
           return jsonify({"code":300,"message": "","data":None})
        
@app.route("/reset", methods=['POST','GET'])
def reset():
    if request.method == 'POST':
        username = request.form.get('username')
        newpassword = request.form.get('pwd')
        repassword = request.form.get('repwd')
        email = request.form.get("email")
        key = request.form.get("key")
        usr=User.query.filter_by(username=username).first()
        if username not in users:
            msg="username not exists! Please register!"
            return render_template("reset.html")
        elif newpassword != repassword:
            msg="The passwords are not the same!"
            return render_template("reset.html")
        elif len(newpassword)<=6 or len(newpassword)>=16:
            msg="The length of the password should be more than 6 and less than 15."
            return render_template("reset.html")
        elif usr.email!=email:
            msg="Email not correct!"
            return render_template("reset.html",msg=msg)
        elif email not in code.keys():
            msg="please send verification code first!"
            return render_template("reset.html",msg=msg)
        elif key!=code[email]:
            msg="incorrect code"
            return render_template("reset.html",msg=msg)
        else:
            usr.password=generate_password_hash(repassword)
            db.session.commit()
            return render_template("login.html")
    return render_template("reset.html", users=users)
    
@app.route("/reset/update", methods=['POST','GET'])
def update():
    email = request.args.get("email")
    username = request.args.get("username")
    actemail=User.query.filter_by(username=username).first().email
    print(username)
    if email not in emailst:
        return jsonify({"code":500,"message": "","data":None})
    elif actemail!=email:
        return jsonify({"code":400,"message": "","data":None})
    elif request.method == 'GET':
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
           return jsonify({"code":200,"message": "","data":None})
        except SMTPRecipientsRefused:
           return jsonify({"code":300,"message": "","data":None})
        
@app.route("/chat", methods=['POST','GET'])
@login_required
def chat():
    username=current_user.username
    current_time = datetime.now().strftime("%I:%M:%S %p").lower().lstrip("0")
    checkin=Checkin.query.filter_by(username=username).first().checkincount
    return render_template("chat.html",username=username,checkin=checkin,current_time=current_time)

@app.route("/chat/answer", methods=['POST','GET'])
def answer():
    response=""
    username = current_user.username
    question = request.args.get('question')
    today = date.today()
    print(question)
    dicuser["content"]=question
    messages.append(dicuser)
    response=chatgpt(messages)
    print(response)
    history=History(username=username,content="Q: "+question+" A: "+response,date=today,name=name)
    db.session.add(history)
    db.session.commit()
    dicass["content"]=response
    messages.append(dicass)
    return jsonify({"response":response}) 

@app.route("/chat/check", methods=['POST','GET'])
@login_required
def check():
    username=current_user.username
    today = date.today()
    check=Checkin.query.filter_by(username=username).first()
    if check.current_login==today:
        return jsonify({"counts":check.checkincount})
    else:
        if check.checkincount is None:
            check.checkincount=1
        else:
            check.checkincount=check.checkincount+1
        check.last_login=check.current_login
        check.current_login=today
        db.session.commit()
    return jsonify({"counts":check.checkincount}) 

@app.route("/chat/switch", methods=['POST','GET'])
@login_required
def switch():
    dog=request.args.get("dog")
    global messages
    messages=dogdic[dog]
    global name
    name=dog
    return jsonify({"code":200})

@app.route("/history", methods=['POST','GET'])
@login_required
def history():
    username=current_user.username
    today = date.today()
    return render_template("history.html",username=username,today=today)

@app.route("/history/search", methods=['POST','GET'])
@login_required
def search():
    username=current_user.username
    date = request.form.get('date')
    if date == "":
        print(True)
    else:
        print(False)
    dogname = request.form.get('dogname')
    if  dogname !='All' and date != "":
        data = History.query.filter_by(username=username,name=dogname,date=date).all()
        datelist=[]
        doglist=[]
        content=[]
        for row in data:
            datelist.append(str(row.date))
            doglist.append(row.name)
            content.append(row.content)
        return jsonify({'date':datelist,'dog':doglist,'content':content})
    elif dogname =='All' and date != "":
        data = History.query.filter_by(username=username,date=date).all()
        datelist=[]
        doglist=[]
        content=[]
        for row in data:
            datelist.append(str(row.date))
            doglist.append(row.name)
            content.append(row.content)
        return jsonify({'date':datelist,'dog':doglist,'content':content})
    elif dogname=='All' and date == "":
        data = History.query.filter_by(username=username).all()
        datelist=[]
        doglist=[]
        content=[]
        for row in data:
            datelist.append(str(row.date))
            doglist.append(row.name)
            content.append(row.content)
        return jsonify({'date':datelist,'dog':doglist,'content':content})
    else:
        data = History.query.filter_by(username=username,name=dogname).all()
        datelist=[]
        doglist=[]
        content=[]
        for row in data:
            datelist.append(str(row.date))
            doglist.append(row.name)
            content.append(row.content)
        return jsonify({'date':datelist,'dog':doglist,'content':content})
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')