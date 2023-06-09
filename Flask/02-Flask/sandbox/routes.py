from flask import render_template, redirect, url_for, flash, get_flashed_messages
from flask_login import login_user, logout_user
from sandbox.forms import RegisterForm, LoginForm
from sandbox.models import Item, User
from sandbox import app, db

@app.route("/")
@app.route("/home")
def home_index_page():
    return render_template("home_index.html",messages=get_flashed_messages())

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
    return render_template("database_index.html", items=items,messages=get_flashed_messages())

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
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Successfully logged in: {attempted_user.username}', category='success')
            return redirect( url_for('database_index_page'))
        else:
            flash(f'Username or Password do not match, please try again', category='danger')
    return render_template("login_index.html", form=form)




@app.route("/logout")
def logout_index_page():
    flash("you logged out of your account", category='primary')
    logout_user()
    return redirect( url_for('home_index_page'))
    















