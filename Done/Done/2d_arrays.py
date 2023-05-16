#!/usr/bin/python3

# Lists
# used to store multiple values in a single variable

# 2D Lists
# a list of lists

animals = ['chimpanzee','fawn','bull','tapir','cow','iguana']
for i in range(0,len(animals),1):
    print("animal: ",animals[i])

male_names = ['Mohamed','Haiden','Terrell','Neil','Carl','Ezekiel']
female_names = ['Brisa','Leyla','Daniella','Isabell','Rayna','Tania']
female_names.append('Tanya')
female_names.remove('Leyla')
names = [male_names,female_names]
male_names.insert(6,'Enzo')
male_names.sort()
for j in names:
    print("list: ",j)
    for name in j:
        print("name: ",name)