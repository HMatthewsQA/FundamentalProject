from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import os
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from application import routes
