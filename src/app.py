from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from api import add_resources
from data import db_session

db_session.global_init("/app/db/db.sqlite")
app = Flask(__name__, template_folder='/app/templates', static_folder='/app/static')
app.config['SECRET_KEY'] = 'secret_key'
app.config['UPLOAD_FOLDER'] = '/app/static/img/avatars'
app.debug = True
api = Api(app)
api = add_resources(api)

login_manager = LoginManager()
login_manager.init_app(app)
