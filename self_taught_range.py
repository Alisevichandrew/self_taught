# Диапазоны - структура и синтаксис
my_range = range(7)  # my_range - this is the variable
# 7 - верхняя граница, которая не включается в диапазон

print(type(my_range))
# <class 'range'>
# каждый диапазон - это экземпляр класса range

print(my_range)
# range(0, 7)

print(list(my_range))
# [0, 1, 2, 3, 4, 5, 6]
