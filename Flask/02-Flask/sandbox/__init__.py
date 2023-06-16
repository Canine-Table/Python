from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
secret_key = os.urandom(12).hex()
app.config.from_object(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app)


from sandbox import routes
