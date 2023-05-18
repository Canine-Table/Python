#!/usr/bin/python3

# filter()
# creates a collection of elements from an iterable for which a function returns
# filter(function, iterable)

my_store = [
    ('shirt',46.99),
    ('pants',44.99),
    ('shoes',999.99),
    ('jacket',299.99),
    ('socks',10.99),
    ('sweater',28.99)
]

less_than_100 = lambda cost: cost[1] <= 100
cost_less_than_100 = list(filter(less_than_100, my_store))
for i in cost_less_than_100:
    print('\nitem:',i[0],'\tcost: ${:.2f}'.format(i[1]))
print()

greater_than_100 = lambda cost: cost[1] >= 100
cost_greater_than_100 = list(filter(greater_than_100, my_store))
for i in cost_greater_than_100:
    print('\nitem:',i[0],'\tcost: ${:.2f}'.format(i[1]))
print()
