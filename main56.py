
# 56.248 Менеджер пакетов PIP
# PACKAGE MANAGER FOR PYTHON
# pip --version
# какие пакеты были инсталлированы глобально
# pip list

# оюновить версию PIP
# pip install --upgrade pip
# может выдать такой ответ
# Requirement already satisfied:
# pip in c:\python\lib\site-packages (25.0.1)
# где
# 25.0.1
# 25 -основная версия - major
# следующая основная версия будет 23.0.0
# 0- минорная версия - minor
# это когда добавляется небольшая новая ф-кция
# 1 - paj
# если исправляется мелкая ошибка
# либо добавляется мелкое дополнение
# установим
# pip install pygame
# если выдаст ошибку, значит пакет 'pygame'
# не совместим с версией установленного python
# значит, на сайте 'pypi.org' ищем 'Release history'
# ищем последнюю верссию
# текущая версия будет указана как
# THIS VERSION
# если и сейчас выдаст ошибку, то удалим и установим
# заново
# pip uninstall pygame
# pip install pygame
# если и здесь не заработает - тогда ищем
# исправление ошибки в интернете
# посмотрим заново список пакетов
# pip list
# import pygame
# pygame.init()
# """
# pygame 2.6.1 (SDL 2.28.4, Python 3.12.0)
# Hello from the pygame
# community. https://www.pygame.org/contribute.html
# """
# можно попробовать установить пакет следующей командой
# pip install (название пакета) 2.*
# или
# pip install (название пакета) 2.1.*
# удалим 'pygame'
# pip uninstall pygame


# 56.249 Виртуальные среды и Pipenv
# выпоним
# pip install pipenv
# pip list

# 56.250 Создание виртуальной среды
# создадим новую папку '.venv'
# откроем терминал
# напишем
# pipenv install requests
# pip list
# активируем виртуальную среду
# pipenv shell
# нажмем в VScode справа снизу на цифры версии Python
# Выберем 'Recommended'

# 56.251 Файлы Pipfile и Pipfile.lock
# Должны быть файлы 'Pipfile' и 'Pipfile.lock'
# Исполняемые файлы для этой виртуальной среды
# находятся: .venv/Scripts
# в папке Lib - находятся инсталлированные пакеты
# перейдем в версию 'Global'
# удалим папку .venv (то есть виртуальную среду)

# создадим заново папку '.venv'
# она будет пустой
# создадим виртуальную среду заново
# НО, при этом, файлы
# 'Pipfile' и 'Pipfile.lock' у нас остались
# откроем терминал
# выйдем из виртуальной среды
# exit
# введем команду
# pipenv install
# без указания конкретных пакетов
# к-рые мы хотим установить
# создалась заново виртуальная среда
# Из уже ранее созданного файла 'Pipfile.lock'
# в папке '.venv'
# мы увидим ту же структуру, что и ранее
# активируем виртуальную среду
# pipenv shell
# цифры версии Python
# нажимаем 'Recommended'

# 56.252 Использование пакетов в виртуальной среде
"""
import requests
my_requests = requests.get('https://www.python.org')
print(my_requests)
# в терминале напишем
# pip install autopep8
# вводим 'pwd'
# получаем путь к папке 'main56.py'
# Path
# ----
# D:\python\bogdan
# передем в настройки 'code runner'
# 'settings'
# вводим в поиск
# 'code runner executor map'
# нажимаем на ссылку
# 'edit in settings.json'
# нужно указать путь к интерпритатору 'Python'
# в виртуальной среде, для этого
# в настройках 'code runner'
# в файле 'settings.json'
# находим '"python": "python -u",'
# пишем
# "python": "D:\python\bogdan\.venv\Scripts\python -u",
# снова выполняем файл 'main56.py'
# получаем ответ
# <Response [200]>
# получим ответ в текстовом виде
print(my_requests.text)
print(my_requests.status_code)
# выполним ещё раз и увидим .html страницу
# активируем выиртуальную среду
# pipenv shell
# выполним файл main56.py
"""


# 56.253 Инсталляция дополнительных пакетов
# в виртуальной среде
# установим пакет pip install pandas
# напишем в терминале
# pipenv shell
# pip install pandas
# вводим pip list
"""
ДОПОЛНЕНО ВИРТУАЛЬНАЯ СРЕДА

https://docs.python.org/3/tutorial/venv.html
pip freeze > requirements.txt      - создание файла
pip install -r requirements.txt    - чтение установленных библиотек из созданного файла
pip uninstall 'name of library'    - удаление установленной ранее библиотеки, где в '  ' указывается название библиотеки. Название можно взять из файла 'requirements.txt'


если вдруг при выполнении команды 'pip freeze > requirements.txt'________выдаст 
'Fatal error in launcher: Unable to create process using '"c:\users\hp\desktop\environment\scripts\python.exe"  
"C:\Users\HP\Desktop\backend\environment\Scripts\pip.exe" freeze': ?? ??????? ????? ????????? ????.'

то, выполнить команду 'python -m pip install --upgrade pip'
"""
# 56.254 Дерево пакетов и обновление пакетов


my_requests = requests.get('https://www.python.org')
print(my_requests)

print(my_requests.text)
print(my_requests.status_code)
# напишем в терминале
# pipenv graph
# увидим список пакетов и их зависимостей
# в виртуальной среде
# ниже команда, как обновить
# список пакетов в виртуальной среде
# pipenv update
# увидим команду
# 'All dependencies are now up-to-date!'
# можно обнвить конкретный пакет
# pipenv update requests
# 'All dependencies are now up-to-date!'
