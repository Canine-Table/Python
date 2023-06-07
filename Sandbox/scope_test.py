#!/usr/bin/python3

spam = "global scope spam"

def test_scope():

    spam = "test spam"

    def do_local():
        spam = "local assignment spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal assignment spam"

    def do_global():
        global spam
        spam = "global assignment spam"

    do_local()
    print("After local assignment:",spam)
    do_nonlocal()
    print("After nonlocal assignment:",spam)
    do_global()
    print("After global assignment:",spam)


print("Before global scope:",spam)
test_scope()
print("After global scope:",spam)
