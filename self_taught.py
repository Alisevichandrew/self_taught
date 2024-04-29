
# Task of 'set'
# 1. Create set from different element of 'int'
# 2. Add to it another one element
# 3. Create other set with some of elements, notes:
# some elements of other set, must includ the similar
# elements of the first set
# 4. Find the common elements in the both of elements
# (use the method 'intersection' (&))
# and put them into another new set
# 5. make the conversion common set into the list ([])
# and entering the list into the terminal
# 6. Make another operations with resault set (by your wishes)

# decision (i'm)
my_set = {12, 20}
my_set.add(45)
print(my_set)

other_set = {20, 50, 7, 12}

common_set = my_set & other_set
print(common_set)
common_set = my_set.intersection(other_set)
print(common_set)
common_set = list(common_set)
print(common_set)
print(type(common_set))
common_set = set(common_set)
print(type(common_set))
common_set.remove(12)
print(common_set)
