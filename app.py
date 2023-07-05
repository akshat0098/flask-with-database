import os 
import time
from flask import Flask, render_template, request, url_for, redirect , Response
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
## creating the databse flask

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

app.app_context().push()


app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(100),nullable=False)
    lastname = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(300),nullable=False)
    password = db.Column(db.String(300),nullable=False)
    email = db.Column(db.String(80),nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),server_default= func.now())
    updated_at = db.Column(db.DateTime(timezone=True),server_default= func.now(),onupdate=func.now())

    def __repr__(self):
        return f"Student('{self.firstname}','{self.lastname}','{self.email}','{self.password}','{self.email}')"
    




@app.route('/')
def home():
   return Response("This is homepage")

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)