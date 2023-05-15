#!/usr/bin/python3

# Tuples
# a collection which is ordered and unchangeable
# used to group together related data

student_1 = ('Mohamed',22,'Male')
student_2 = ('Brisa',22,'Female')
student_3 = ('Carl',22,'Male')
student_4 = ('Isabell',22,'Female')
students = [student_1,student_2,student_3,student_4]
for i in students:
    if i.count('Male') == True:
        print(i[0],"Gender: Male\nIndex:",i.index('Male'))
    elif i.count('Female') == True:
        print(i[0],"Gender: Female\nIndex:",i.index('Female'))
    print("Name:",i[0])
    print("Count of 22:",i.count(22))