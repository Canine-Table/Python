#!/bin/python3

# Sets
# collection which is unordered, unindexed. No duplicate values
# faster than lists

utensils = {'fork','spoon','knife','knife'}
dishes = {'bowl','plate','cup','knife'}

print('diff:',dishes.difference(utensils))
print('same:',dishes.intersection(utensils))
utensils.add('napkin')
utensils.remove('knife')
utensils.update(dishes)
dinner_table = dishes.union(utensils)

for i in dinner_table:
    print(i)
for j in utensils:
    print(j)