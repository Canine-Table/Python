#!/usr/bin/python3

# Dictionary
# a changeable, unordered collection of unique key:value pairs
# fast because they use hashing, allowing us to access values quickly
# dictionaries like sets are mutable 'changeable'

capitals = {
    'USA':'Washington DC',
    'India':'New Dehli',
    'China':'Beijing',
    'France':'???'
}

capitals.update({'Germany':'Berlin'})
capitals.update({'France':'Paris'})

print(capitals.get('France'))
print('Keys: ',capitals.keys())
print('Values: ',capitals.values())
print('All Items:',capitals.items())
capitals.pop('China')
for key,value in capitals.items():
    print('The capital of',key,"is",value+'.')
capitals.clear()
print('cleared:',capitals)