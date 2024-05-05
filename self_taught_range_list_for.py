# Other examples with 'for' and 'generator list'
# decision with generator of list
list_a = [-6, -4, 0, 1, 2, 3, 4, 5]
list_b = [x for x in list_a if x % 2 == 0 and x > 0]
# # take thaht 'x', in which elements together even numbers and more 'null'
print(list_b)   # [2, 4]

# decision with cycle 'for'
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = []
for x in list_a:
    if x % 2 == 0:
        if x > 0:
            list_b.append(x)

print(list_b)
