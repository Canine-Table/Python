#!/usr/bin/python3

# zip(*iterable)
# aggregate elements from 2 or more iterables (list,tuples,sets,etc.)
# creates a zip object paired elements stored in tuples for each element

usernames = ['Canine','Table']
passwords = ['p@ssw0rd','abc123']
echo = print

echo()
users_dict = dict(zip(usernames,passwords))
echo(type(users_dict))
for key,value in users_dict.items():
    echo(key,':',value)

echo()
user_list = list(zip(usernames,passwords))
echo(type(user_list))
for j in user_list:
    echo(j)
echo()

login_date = ['3/2/2020','1/1/2022']
trio = zip(login_date,usernames,passwords)
echo(type(trio))
for i in trio:
    print(i)
    for j in i:
        print(j)
echo()