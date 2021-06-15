from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:harry0916@127.0.0.1:3306/dbms"
app.config['SECRET_KEY'] = 'your key'
db = SQLAlchemy(app)
