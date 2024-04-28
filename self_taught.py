
# ==================================================
# import of modul
# import datetime
# print(datetime.MAXYEAR)

# or through function
import datetime


def new_func():
    return datetime.MAXYEAR


print(new_func())

# =================================================

# dict
my_dict = {}

key_1 = input("Please enter key 1: ")
value_1 = input("Please enter value 1: ")

my_dict[key_1] = value_1
# если будет запись в формате 'key_1' - то результат будет key_1
# а мы ключу присваиваем значение переменной key_1, то есть названия, которое введее после
# "Please enter key 1: "

key_2 = input("Please enter key 2: ")
value_2 = input("Please enter value 2: ")

my_dict[key_2] = value_2

key_3 = input("Please enter key 3: ")
value_3 = input("Please enter value 3: ")

my_dict[key_3] = value_3

# adding two keys
my_dict['key_4'] = 'value_4'
my_dict['key_5'] = 'value_5'

# deleting two keys
del my_dict[key_3]
del my_dict['key_4']

print(my_dict)
# ====================================================
