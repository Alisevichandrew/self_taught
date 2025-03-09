# 53.238 Отправка email с помощью модуля smtplib
# активация Docker
# https://login.docker.com/activate
#
# https://github.com/rnwood/smtp4dev
# создание и запуск локального smtp сервера
# https://github.com/rnwood/smtp4dev/wiki/Installation

# как запустить smtp сервер в Docker контейнере - скопировать ниже
# docker run --rm -it -p 5000:80 -p 2525:25 rnwood/smtp4dev

# открываем Docker
# переходим в терминал powershall
# docker version
# проверяем, какие контейнеры запущены
# docker ps
# вставляем команду в командную строку Powershall
# docker run --rm -it -p 5000:80 -p 2525:25 rnwood/smtp4dev
# переходим в вэб браузер
# вставляем
# http://localhost:5000/
# либо (что одно и тоже)
# http://127.0.0.1:5000/


# Docker Engine Experimental False Fixed
# https://www.youtube.com/watch?v=IfY1xxNBH18

# Важно !
# SMTP Server is listening on port 25 (::).
# Keeping last 100 messages per mailbox and 100 sessions.
# IMAP Server is listening on port 143 (::)
# Overriding HTTP_PORTS '80' and HTTPS_PORTS ''. Binding to values defined by URLS instead 'http://*:80'.
# Now listening on: http://[::]:80

# 53.239 Компоновка и отправка email
# 53.240 HTML шаблоны для отправки email
# 53.241 Отправка вложений в Email
from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

my_email = EmailMessage()
# относительный путь к файлу index.html
html_template = Template(Path("templates/index.html").read_text())
# substitute позволяет заменить значение переменных
html_content = html_template.substitute({'name': 'Andrew', 'date': 'tomorrow'})
my_email['from'] = 'Andrew <dopysk1980@gmail.com>'
my_email['to'] = 'dopysk1980@gmail.com'
my_email['subject'] = "Email with image"
my_email.set_content(html_content, 'html')

# отправим вложенный файл
# rb - read binary
with open('images/Snoopy.jpg', 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image',
                            subtype='jpg', filename='Snoopy.jpg')

with smtplib.SMTP(host='127.0.0.1', port=2525) as smtp_server:
    smtp_server.ehlo()
    """
    В нашем случае - это не требуется, но если нужно, можно использовать ниже:
    # если требуется шифровка
    smtp_server.starttls()  
    # если требуется авторизоваться
    smtp_server.login('username', 'password')
    """
    smtp_server.send_message(my_email)
    print('Email was sent weell done!')
    # Email was sent !
    # перейдем в вэб браузер и проверим
    # http://localhost:5000/
    # закроем powershall
    # ctrl + c
    # docker ps
