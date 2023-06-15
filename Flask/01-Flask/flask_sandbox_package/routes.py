from flask_sandbox_package import create_app # do not rename it as app
from flask import render_template
from flask_sandbox_package.models import Item

app = create_app() # create the app object here

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

@app.route("/database")
@app.route("/db")
def database_index_page():
    items = Item.query.all()
    return render_template("database_index.html", items=items)
