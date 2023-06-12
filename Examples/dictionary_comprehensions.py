#!/usr/bin/python3

# dictionary comprehension
# create dictionaries using an expression
# can replace for loops and certain functions

# -------------------------------------------------------------------------------

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

# -------------------------------------------------------------------------------

cities_in_F = {'New York':32, 'Bostin':75, 'Los Angeles':100, 'Chicago':50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

# -------------------------------------------------------------------------------

weather = {'New York':'snowing', 'Bostin':'sunny', 'Los Angeles':'sunny', 'Chicago':'cloudy'}
sunny_weather = {key: value for (key,value) in weather.items() if value == 'sunny'}
print(sunny_weather)

# -------------------------------------------------------------------------------

def check_temp(value):
    if value < 0:
        return 'Very Cold'
    elif value >= 0 and value < 20:
        return 'Cold'
    elif value >= 20 and value < 40:
        return 'chilly'
    elif value >= 40 and value < 60:
        return 'Warm'
    elif value >= 60 and value < 80:
        return 'Hot'
    elif value >= 80 and value < 100:
        return 'Very Hot'
    else:
        return 'Heat Wave'

get_weather = {key: check_temp(value) for (key,value) in cities_in_F.items()}
print(get_weather)