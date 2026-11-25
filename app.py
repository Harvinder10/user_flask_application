from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")



app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
db = SQLAlchemy(app)
migrate = Migrate(app,db)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Fname = db.Column(db.String(50),nullable=False)
    Lname = db.Column(db.String(50),nullable=True)
    Email = db.Column(db.String(50),nullable=False,unique=True)
    dob = db.Column(db.Date,nullable=False)
    created_at = db.Column(db.DateTime,server_default=db.func.now())

class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    userid = db.Column(db.Integer,nullable=False)
    contact= db.Column(db.Integer,nullable=False)

app.run(debug=True,port=5001)