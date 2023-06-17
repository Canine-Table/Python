from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
from sandbox.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user
from sandbox.models import Item, User
from sandbox import app, db


@app.route("/")
@app.route("/home")
def home_index_page():
    return render_template("home_index.html",messages=get_flashed_messages())


@app.route("/about")
def about_index_page():
    return render_template("about_index.html")


@app.route("/market", methods=["GET","POST"])
@login_required
def market_index_page():
    purchase_form = PurchaseItemForm()
    sell_form = SellItemForm()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_obj = Item.query.filter_by(name=purchased_item).first()
        if p_item_obj:
            if current_user.can_purchase(p_item_obj):
                p_item_obj.buy_item(current_user)
                flash(f"congratulations on your purchase, we hope you enjoy your new {p_item_obj.name}", category='success')
            else:
                flash(f"insufficient funds, you cannot purchase this {p_item_obj.name}", category='danger')

        sold_item = request.form.get('sold_item')
        s_item_obj = Item.query.filter_by(name=sold_item).first()
        if s_item_obj:
            if current_user.can_sell(s_item_obj):
                s_item_obj.sell_item(current_user)
                flash(f"congratulations , you sold your {s_item_obj.name} back to the flask marketplace", category='success')
            else:
                flash(f"you do not own this {s_item_obj.name}, therefore you can not sell it", category='danger')

        return redirect( url_for('market_index_page') )

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template("market_index.html", items=items, messages=get_flashed_messages(), purchase_form=purchase_form, sell_form=sell_form, owned_items=owned_items)


@app.route("/users")
@login_required
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
        login_user(user_to_create)
        flash(f'Account created successfully! you are now logged in as {user_to_create.username}', category='success')
        return redirect( url_for('market_index_page'))
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
            return redirect( url_for('market_index_page'))
        else:
            flash(f'Username or Password do not match, please try again', category='danger')
    return render_template("login_index.html", form=form)


@app.route("/logout")
def logout_index_page():
    flash("you logged out of your account", category='primary')
    logout_user()
    return redirect( url_for('home_index_page'))

