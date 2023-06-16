from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask import Flask
from os import urandom

app = Flask(__name__)
secret_key = urandom(12).hex()
app.config.from_object(__name__)
login_manager = LoginManager(app)
login_manager.login_view = "login_index_page"
login_manager.login_message_category = "info"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from enl8720 import routes
