# __INIT__.PY underneath app folder

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# initiate login manager
login_manager = LoginManager()
# create Flask application
app = Flask(__name__)
# this is for security
app.config['SECRET_KEY'] = 'bridge360PH'
# get the base directory of __file__ --> app.py
basedir = os.path.abspath(os.path.dirname(__file__))

# create database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
# we don't want to track every modeification
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False
# connect app to Sql alchemy
db = SQLAlchemy(app)
# connect the app to the database
Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'login'

from moses_app.hospital_info.views import hospital_info_blueprint
app.register_blueprint(hospital_info_blueprint, url_prefix='/')
