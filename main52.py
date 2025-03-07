# 52.233 Модуль для регулярных выражений re
# import re

# my_string = "My name is Andrew"
# my_string = "My name is Andrew!"
# знак '!' указвает, что строка не заканчивается
# res = re.search('Andrew', my_string)

# print(res)
# # <re.Match object; span=(11,
# # 17), match='Andrew'>
# # 11- начальный индекс, 17 - конечный индекс
# # строки 'Andrew' в строке 'My name is Andrew'

# print(type(res))
# # <class 're.Match'>

# другой пример

# res = re.search('A....w', my_string)
# print(res)
# <re.Match object; span=(11,
# 17), match='Andrew'>
# т.е. - получаем тот же р-т, что и ранее

# также есть специальные символы, к-рые
# указывают на начало или конец строки
# например:

# res = re.search('A....w$', my_string)
# символ '$' указывает на то, что хотим
# найти 'Andrew' в конце строки
# res = re.search('^A....w$', my_string)
# символ '^' - показывает, что  хотим найти в начале строки

# можно записать ещё так
# my_string = "My name is Andrew."
# res = re.search('^M.*name', my_string)
# запись '.*' - означает любые символы
# print(res)
# <re.Match object; span=(11,
# 18), match='Andrew.'>

# res = re.search('A....w.$', my_string)
# print(res)
# <re.Match object; span=(11,
# 18), match='Andrew.'>
# если в регулярном выражении мы ищем точку
# тогда ипользуем обратный слэш '\.'

# например
# res = re.search('A....w\\.$', my_string)
# print(res)
# <re.Match object; span=(11,
# 18), match='Andrew.'>

# print('A....w\\n.$')
# A....w
# .$
# print(r'A....w\\n.$')
# используем 'r' - строки
# A....w\\n.$

# поэтому следует всегда перед паттерном
# добавлять 'r', то есть:


# таким образом, окончательно
# найдем определенное совпадение
# в строке
# import re
# my_string = "My name is Andrew."

# res = re.search(r'A....w\.$', my_string)
# print(res)
# # <re.Match object; span=(11,
# # 18), match='Andrew.'>
# # или
# print(res.span())
# # (11, 18) - начало и конец результирующей строки
# # к-рые мы нашли, используя 'search'
# # видим кортеж (<class 'tuple'>) из 2-ух элементов

# print(res.start())
# # 11
# print(res.end())
# 18

# 52.234 Сохранение паттерна в отдельном объекте
# Например - паттерн - r'A....w\.$' (из предыдущщего примера)
# import re
# my_string = "My name is Andrew."

# res = re.search(r'A....w\.$', my_string)

# my_pattern = re.compile(r'A....w\.$')

# print(my_pattern)
# # re.compile('A....w\\.$')

# # можем использовать 'my_pattern'
# # чтобы находить совпадения
# print(my_pattern.search(my_string))
# re.compile('A....w\\.$')
# # <re.Match object; span=(11,
# # 18), match='Andrew.'>

# запишем так
# import re

# my_string = "My name is Andrew."
# other_string = "My name is Andrew!"

# my_pattern = re.compile(r'^My.*\.$')

# '^My' - начинается строка на 'My'
# '.*'  - потом - любые символы
# '\.'  - потом - обязательно точка '.'
# '$'   - и конец строки
# import re
# import re
# print(my_pattern)
# проверим, соответствует ли строка
# "My name is Andrew" регулярному выражению
# r'^My.*\.$'
# print(my_pattern.match(my_string))
# re.compile('^My.*\\.$')
# <re.Match object; span=(0, 18), match='My name is Andrew.'>
# т.есть строка полность совпала с регулярным выражением

# print(my_pattern.match(other_string))
# None - потому что эта строка не
# соответствует этому регулярному выражению
# вот этому - r'^My.*\.$' - ту нет знака '!'
# она не заканчивается на точку


# сделаем следующее:
# удалим 'other_string'
# заменим my_string = "My name is Andrew."
#  на следующее:
# import re

# # my_string = "My name is Andrew. Andrew is a self taught"
# # print 1
# # или
# my_string = "My name is Andrew. Aoooow is a self taught"
# # print 2
# my_pattern = re.compile(r'A....w')
# # '....' - 4-ре точки заменяют любые 4-ре символа
# print(my_pattern)

# print(my_pattern.findall(my_string))
# # получим:
# # print 1
# # re.compile('A....w')
# # ['Andrew', 'Andrew'] - получаем список из 2-ух строк

# # print 2
# # re.compile('A....w')
# # ['Andrew', 'Aoooow'] - или
# # ещё можно сказать: получили список из 2-ух элементов

# # 52.235 Проверка email с помощью регулярного выражения
# import re
# # email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
# # '^' - указывает начало строки
# # указываем допустимые символы перед знаком '@'
# # [a-zA-z0-9_.] - запись обозначаем, что должно встречаться
# # один и более раз со специальными символами: любые буквы в нижнем регистре
# # любые буквы в верхнем регмистре, любые цифры от 0 до 9-ть
# # далее, допускается знак "_" просто знак подчеркивание,
# # "." просто допускается в записи точка

# # [a-zA-Z0-9] - любые знаки и буквы но уже без спец символов
# #  один и более раз
# # '\.' - обязательно должна быть точка

# # '[a-zA-Z0-9-.]+'   добавили "-." потому что могут быть поддомены
# # добавили '+' потомучно записи в квадратных скобках могут встречаться
# # один и более раз после записи '\.'

# # '$' - указывает на то, что строка должна закончится

# # далее, создадим пттерн на основании этого регулярного выражения:
# # email_check_pattern = re.compile(email_regexp)
# # 'compile' создает новый паттерн на основании регулярного выражения 'email_regexp'

# #  создадим ф-кцию и ей уже будем передавать выражение


# def check_email(email):
#     email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
#     email_check_pattern = re.compile(email_regexp)
#     validation_result = "valid" if email_check_pattern.fullmatch(
#         email) else "not valid"
#     return (email, validation_result)


# # Valid
# print(check_email('dopysk1980@gmail.com'))
# print(check_email('do._pysk1980@gmail.com'))
# # запись "._" делает этот email также валидным
# print(check_email('dopysk1980@sub.gmail.com'))
# # Invalid
# print(check_email('dopysk1980gmail.com'))
# print(check_email('dopysk1980@gmailcom'))
# print(check_email('@gmail.com'))
# print(check_email('dopysk1980@'))

# # ('dopysk1980@gmail.com', 'valid')
# # ('do._pysk1980@gmail.com', 'valid')
# # ('dopysk1980@sub.gmail.com', 'valid')
# # ('dopysk1980gmail.com', 'not valid')
# # ('dopysk1980@gmailcom', 'not valid')
# # ('@gmail.com', 'not valid')
# # ('dopysk1980@', 'not valid')


# 52.236 Задача - Проверка пароля
"""
1. Создайте ф-кциюдля проверки пароля
check_password
2. Пароль должен быть миннимум 8 символов
3. В пароле должны быть:
- буквы в нижнем регистре
- буквы в верхнем регистре
- цифры
- специальные символы
4. Попросите пользователя ввести пароль в 
терминале и проверьте его используя
ф-кцию, которую мы создали
"""

# 52.237 Решение
import re


def check_password(password):
    # создаем паттерн для проверки длиня пароля
    lenght_pattern = re.compile(r"\S{8,}")
    # проверяем, что в строке минимум 8-мь символов
    # '\S' говорит о том, что пробелы и перенос на другую
    # строку не считается
    # создадим паттерн, который будет проверять, что
    # в пароле есть буквы в нижнем регистре
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    # '^.*' - покрывает начало строки (может быть а может и не быть символа)
    # '.*$' - покрывает конец строки (любой символ может быть любое количество раз)
    # а может и не быть
    # "[a-z]+" любая буква должна встречаться в пароле
    # один и более раз
    # проверка, в пароле есть ли буквы в верхнем регистре
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    # добавляем паттерн для проверки наличия хотя бы одной цифры
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    # паттерн для проверки специяального символа в пароле
    spesial_sumbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")
    # проверка на отсутствие табуляции или пробелов
    no_whitespace_pattern = re.compile(r"^\S*$")
    # '\S' - говорит, что могут быть любые символы в строке
    # любое количество раз, НО КРОМЕ ПРОБЕЛОВ,
    # ПЕРЕХОДОВ НА ДРУГУЮ СТРОКУ И НЕСКОЛЬКО
    # ДРУГИХ СПЕЦИАЛЬНЫХ СИМВОЛОВ
    #  '+' указываетя для того, чтобы был хотя бы один из символов
    # из этого списка
    # # spesial_sumbol_pattern = re.compile(r"[@%#!&*^\.]")
    # '\.' - это если допускается точка
    # проверяем общий пароль согласно этих паттернов
    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, "No whitespases allowed in the password")
    if not re.fullmatch(lenght_pattern, password):
        return (False, "Password must have at least 8 symbols")

    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least one lower case letter")

    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least one upper case letter")

    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least one number")

    if not re.fullmatch(spesial_sumbol_pattern, password):
        return (False, "Password must have at least one spesial symbol '@%#!&*^'")

    return (True, "Password is valid!")


# print(check_password('asdfASD 2342   !234'))
# print(check_password('123'))
# print(check_password('12345678'))
# print(check_password('1234567a'))
# print(check_password('asdbADGAG'))
# print(check_password('3234sfASDF'))
# print(check_password('asdfASDF3242!&'))
# (False, 'No whitespases allowed in the password')
# (False, 'Password must have at least 8 symbols')
# (False, 'Password must have at least one lower case letter')
# (False, 'Password must have at least one upper case letter')
# (False, 'Password must have at least one number')
# (False, "Password must have at least one spesial symbol '@%#!&*^'")
# (True, 'Password is valid!')

while True:
    password = input("Please enter password: ")
    password_check_res = check_password(password)
    if password_check_res[0]:  # выводим по индексам - будет True или False
        print(password_check_res[1])  # выводим по сообщениям (1-ый индекс)
        break
    print(password_check_res[1])
