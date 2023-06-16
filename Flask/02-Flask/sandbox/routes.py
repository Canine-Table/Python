from flask import render_template, redirect, url_for, flash
from sandbox import app, db
from sandbox.models import Item, User
from sandbox.forms import RegisterForm, LoginForm

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

@app.route("/db/usr")
@app.route("/db/user")
@app.route("/database/usr")
@app.route("/database/user")
def user_index_page():
    users = User.query.all()
    return render_template("users_index.html", users=users)

@app.route("/register", methods=["GET","POST"])
def register_index_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,email_address=form.email_address.data,password=form.password_two.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect( url_for('database_index_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Caught error: {err_msg}', category='danger')
    return render_template("register_index.html", form=form)


@app.route("/login", methods=["GET","POST"])
def login_index_page():
    form = LoginForm()

    return render_template("login_index_page.html", form=form)