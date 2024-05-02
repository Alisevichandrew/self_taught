# Min and max in range
# 1. Create a range of some numbers
# 2. Get the minimum and maximum number from that range

my_range = range(0, 10, 2)

max_el, min_el = my_range[0], my_range[0]

for i in range(1, len(my_range)):
    if my_range[i] < min_el:
        min_el = my_range[i]

    if my_range[i] > max_el:
        max_el = my_range[i]

print("the minimum element of the range", my_range, 'is', min_el)
print("the maximum element of the range", my_range, 'is', max_el)
print(type(my_range))
