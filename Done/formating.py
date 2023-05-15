#!/usr/bin/python3

# str.format
# optional methods that give users 
# more control when displaying output

num = 3.14159
number = 1000000.14159
numbers = 314159
name = 'Canine Table'
hey_diddle_diddle = 'Hey, diddle, diddle, The {3} and the fiddle, The {2} jumped over the {1} The little {0} laughed To see such sport, And dish ran away with the spoon'
print(hey_diddle_diddle.format('dog','moon','cow','cat'))

hey_diddle_diddle = 'Hey, diddle, diddle, The {} and the fiddle, The {} jumped over the {} The little {} laughed To see such sport, And dish ran away with the spoon'
print(hey_diddle_diddle.format('cat','cow','moon','dog'))

hey_diddle_diddle = 'Hey, diddle, diddle, The {0} and the fiddle, The {0} jumped over the {0} The little {0} laughed To see such sport, And dish ran away with the spoon'
print(hey_diddle_diddle.format('dog'))

print("Hello {0:20}!!".format(name))
print("Hello {name:<20}!!".format(name='John Doe'))
print("Hello {:^20}!!".format(name))
print("Hello {:>20}!!".format(name))
print("Hello {:^20.2f}!!".format(num))
print("Hello {:^20,.4f}!!".format(number))
print("Hello {:^20b}!!".format(numbers)) # bin
print("Hello {:^20o}!!".format(numbers)) # oct
print("Hello {:^20x}!!".format(numbers)) # hex
print("Hello {:^20X}!!".format(numbers)) # HEX
print("Hello {:^20e}!!".format(numbers)) # scientific
print("Hello {:^20E}!!".format(numbers)) # SCIENTIFIC
