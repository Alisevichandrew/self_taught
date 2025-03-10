# 54.242 Модукль SQLite3 и создание базы данных
# 54.243 Практика – Запись данных в таблицу SQLite

# import sqlite3
# # ниже, создадим базу данных и файл базы данных
# DB_NAME = "sqlite_db.db"

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(sqlite3.version)
# <sqlite3.Connection object at 0x000001B6638E4D60>
# 0x000001B6638E4D60 - это местоположение объекта в памяти
# установим программу для графического взаимодействия с базой данных
# переходим в браузере по ссылке https://sqlitebrowser.org/dl/
# это будет DB Broeser for SQLite
# необходимо открыть программу DB Browser (SQLite)
# подключимся к базе данных локально
# выбираем в sqlite - open database и выбираем путь
# к нашей базе, созданной в файле main54.py

# создадим программно в python таблицу в базе данных (см. ниже)

# import sqlite3
# DB_NAME = "sqlite_db.db"

# courses = [
#     (265, "Java full course", 21, 43),
#     (97, "Go lang course", 18, 5),
#     (69, "C", 16, 8),
# ]
# # создадим подключение
# # используем with, чтобы автоматически закрывать
# # подключение к базе данных,
# # иначе, нам необходимо использовать close
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     # проведем итерацию, уберем строку ниже:
#     # sqlite_conn.execute(sql_request, (151, "Python crash course", 32, 15))
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()
# необходимо заменить знаки '?' определенными значениями (id, title, students_qty, reviews_qty )
# # Create new table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)
# перходим в DB Browser (SQLite) и нажимаем F5

# нажимаем F5
# чтобы проверить, заполнились ли данные, переходим
# в DB Browser (SQLite) на вкладку Brouse Data


# 54.244 Практика – Чтение данных из таблицы SQLite
import sqlite3
DB_NAME = "sqlite_db.db"

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty>=10"
    sql_cursor = sqlite_conn.execute(sql_request)
    # for record in sql_cursor:
    #     # print(record) # выводим все
    #     print(record[1])  # например, вывести только название курсов
    records = sql_cursor.fetchall()
    print(records)


# # Add records to the courses table
# courses = [
#     (265, "Java full course", 21, 43),
#     (97, "Go lang course", 18, 5),
#     (69, "C", 16, 8),
# ]

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     # проведем итерацию, уберем строку ниже:
#     # sqlite_conn.execute(sql_request, (151, "Python crash course", 32, 15))
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()
