#!/usr/bin/python3

# sort() method
# used with lists

# sort function
# used with iterables

students = ['Squidward','Samdy','Patrick','Sandy','Mr. Krabs']
students.sort()

for i in students:
    print('\nname:',i)

students.sort(reverse=True)

for i in students:
    print('\nreversed:',i)

students_tuple = ('Squidward','Samdy','Patrick','Sandy','Mr. Krabs')
sorted_students = sorted(students_tuple)

for i in sorted_students:
    print('\nsorted:',i)


sorted_students = sorted(students_tuple,reverse=True)

for i in sorted_students:
    print('\nsorted reverse:',i)

students_list_tuple_dictionary = [
    (
        {'Squidward':'name'},
        {'D-':'grade'},
        {26:'age'}
    ),

    (
        {'Patrick':'name'},
        {'R':'grade'},
        {32:'age'}
    ),

    (
        {'Sandy':'name'},
        {'A+':'grade'},
        {23:'age'}
    ),

    (
        {'Mr. Krabs':'name'},
        {'B-':'grade'},
        {52:'age'}
    ),

    (
        {'Spongebob':'name'},
        {'C':'grade'},
        {21:'age'}
    )    
]

print('\n\n')
for i in students_list_tuple_dictionary:
    for j in i:
        for key,value in j.items():
            print(value+':\t',key)
    print('\n')

print('Done\n\n')
