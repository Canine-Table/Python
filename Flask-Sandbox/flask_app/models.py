from flask_app import db


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(2048), nullable=False, unique=True)

    def __init__(self, name, price, barcode, description):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.description = description

    def __repr__(self):
        return '<Item %r>' % self.name
