from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
db.init_app(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(2048), nullable=False, unique=True)


@app.route("/")
@app.route("/home")
def home_index_page():
    return render_template("home_index.html")


@app.route("/about/<username>")
def about_index_page(username):
    return render_template("about_index.html", username=username)


@app.route("/market")
def market_index_page():
    items = [
        {"id": 1, "name": "Phone", "barcode": 539023874334, "price": 150.00},
        {"id": 2, "name": "Laptop", "barcode": 256834854984, "price": 125.00},
        {"id": 3, "name": "KeyBoard", "barcode": 463938829392, "price": 55.00},
    ]
    return render_template("market_index.html", items=items)


if __name__ == '__main__':
    app.run(debug=True)
