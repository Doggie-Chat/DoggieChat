from exts import db
from flask_login import UserMixin
class User(db.Model,UserMixin):
    __tablename__="user"
    username=db.Column(db.String(100),primary_key=True,nullable=False)
    password=db.Column(db.String(15),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    def get_id(self):
        return self.username
class History(db.Model):
    __tablename__="history"
    num=db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    username=db.Column(db.String(15),db.ForeignKey("user.username"),nullable=False)
    content=db.Column(db.Text,nullable=False)
    date=db.Column(db.Date,nullable=False)
    name=db.Column(db.String(20),nullable=False)
class Checkin(db.Model):
    __tablename__="checkin"
    username=db.Column(db.String(100),primary_key=True,nullable=False)
    last_login=db.Column(db.Date,nullable=True)
    current_login=db.Column(db.Date,nullable=True)
    checkincount=db.Column(db.Integer,nullable=True)
