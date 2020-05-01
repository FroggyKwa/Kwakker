from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager
from flask_restful import reqparse, abort, Api, Resource
from api import add_resources
from data import db_session

db_session.global_init("db/db.sqlite")
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'secret_key'
app.config['UPLOAD_FOLDER'] = 'D:\\FroggLing\\Python\\Kwakker\\static\\img\\avatars'
app.debug = True
api = Api(app)
api = add_resources(api)

login_manager = LoginManager()
login_manager.init_app(app)
