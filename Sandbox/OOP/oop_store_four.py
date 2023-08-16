#!/usr/bin/python3
from oop_modules.store import Item
from oop_modules.store.phone import Phone


item_one = Item(name='Labtop',price=1000.94,quantity=5)
item_two = Item(name='Phone',price=2000.04)

print(item_one.apply_discount(pay_rate=0.7))
print(item_two.apply_discount())
Item.instantiate_from_csv()
for instance in Item.all:
    print(instance)
print(Item.is_integer(34))
print(Item.is_integer('hi'))
print(Item.is_integer(34.0))


# magic attributes
print(item_two.__dict__)
print(Item.__dict__)

phone1 = Phone(name='jscPhonev10',price=500,quantity=14)
phone2 = Phone(name='jscPhonev20',price=700,quantity=8)

print(phone2)

del phone2.quantity
print(phone2)

print(phone1.apply_discount(pay_rate=0.5))
print(phone2.apply_discount())
print(Item.all)
print(Phone.all)
