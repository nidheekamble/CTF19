import os
from flask import Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628cb0b12ce6c676dfde280ba246'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db'
db = SQLAlchemy(app)
Bootstrap(app)
from hush import routes