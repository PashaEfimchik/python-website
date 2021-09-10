from website import db
from sqlalchemy import ForeignKey, update
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField ,SubmitField, validators

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    user_blog = db.relationship('Posts', backref='list', lazy=True)

    def __init__(self, username, email, password):
        self.username = username 
        self.email = email
        self.password = password
        
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_time = db.Column(db.DateTime, index=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    content = db.Column(db.String(500), unique=False, nullable=False)
    parent_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self,post_time, title, content, parent_id):
        self.post_time = post_time
        self.title = title 
        self.content = content
        self.parent_id = parent_id
    def __repr__(self):
       return f"Post('{self.title}', '{self.post_time}')"



class PostForm(FlaskForm):
    post_time = datetime.today().replace(microsecond=0)
    title = StringField('title', [validators.InputRequired()])
    content = TextAreaField('content', [validators.InputRequired()])
    submit = SubmitField('Submit')