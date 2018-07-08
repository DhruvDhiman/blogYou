from werkzeug import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class user(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    loginid = db.Column(db.String(100))
    password = db.Column(db.String(100))
    
    def __init__(self, loginid, password):
        self.loginid = loginid.title()
        self.password = password.title()
        
    def check_password(self, loginid):
        return (self.loginid, self.password)

class blogModel(db.Model):
    __tablename__='blog'
    blog_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    blog = db.Column(db.String(200))
    user_id=db.column(db.String(100))

    def __init__(self, title, blog , user_id):
        self.title = title.title()
        self.blog = blog.title()
        self.user_id = user_id.title()


    