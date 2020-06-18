from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)

from application import routes
