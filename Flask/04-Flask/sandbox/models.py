from sandbox import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(2048), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def buy_item(self,user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    def sell_item(self,user):
        self.owner = None
        user.budget += self.price
        db.session.commit()

    def __repr__(self):
        return '<Item %r>' % self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=32), nullable=False, unique=True)
    email_address = db.Column(db.String(length=64), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owner_user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        return self.password

    @property
    def prettier_budget(self):
        my_list = list(str(self.budget))
        my_new_list = ""
        for i,e in enumerate(reversed(my_list),1):
            if i % 3 == 0 and len(my_list) != 3:
                my_new_list = f"{my_new_list}{e},"
            else:
                my_new_list = f"{my_new_list}{e}"
        return f"{my_new_list[::-1]}"

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)

    def can_purchase(self,item_obj):
        return self.budget >= item_obj.price

    def can_sell(self,item_obj):
        return item_obj in self.items

    def __repr__(self):
        return '<User %r>' % self.username
