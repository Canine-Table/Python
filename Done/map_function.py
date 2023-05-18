#!/usr/bin/python3

# map()
# applies a function to each item in an iterable (list,tuple,etc.)
# map(function,iterable)

my_store = [
    ('shirt',46.99),
    ('pants',44.99),
    ('shoes',999.99),
    ('jacket',299.99),
    ('socks',10.99),
    ('sweater',28.99)
]

to_euros = lambda data: (data[0],data[1]*0.82)

my_euro_store = list(map(to_euros, my_store))

for i in my_euro_store:
    print('\nitem:',i[0],'\tcost: €{:.2f}'.format(i[1]))
print()

to_usd = lambda data: (data[0],data[1]/0.82)

my_usd_store = list(map(to_usd, my_euro_store))

for i in my_usd_store:
    print('\nitem:',i[0],'\tcost: ${:.2f}'.format(i[1]))
print()