# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

"""

Работа с строками

"""

# Формат в строке
print('Тестовая {0} в котороую {1} {2}'.format('строка', 'вставляются', 'данные'))

# Поменять местами значение переменных
a = 2
b = 4
# Вариант 1
a, b = b, a

print('A = ' + str(a) + ' : B = ' + str(b))

# Перевернусть строку в обратную сторону
a = "12345abc"
# Вариант 1
b = ''.join(reversed(a))
# Вариант 2
b = a[::-1]  # обращение ко всем символам в строке с интервалом -1.

print(b)

# Развернуть строку
a = [1, 5, -3, 22, 80, 3]

if a != []:
    minElement = a[0]
    for element in a[1:]:
        if element < minElement:
            minElement = element
    print(minElement)
else:
    print('массив пустой')

# Проверить строку на соответсвие и напечатать True или False
s = input()
print(any(c.isalnum() for c in s))  # Строка содержит Буквы и Цифры
print(any(c.isalpha() for c in s))  # Строка содержит Буквы
print(any(c.isdigit() for c in s))  # Строка содержит Цифры
print(any(c.islower() for c in s))  # Строка содержит Буквы в Нижнем регистре
print(any(c.isupper() for c in s))  # Строка содержит Буквы в Верхнем регистре


"""

Кодирование MD5, лучший способ шифрования на сегодня sha512

"""

import hashlib

code = hashlib.md5(b'Hello World!')
print(code.hexdigest())

input_code = input('Введи строку для кодирования: ')
decode = hashlib.md5(input_code.encode())
print(decode.hexdigest())


# Кодирование и декодирование в другие кодировки и бинарную строку
s = 'Привет!'
s1 = s.encode('utf-8')
print(s1)

s2 = s1.decode('utf-8')
print(s2)


"""

Работа с файлами.

"""

# Импорт библиотеки целиком
import os
import glob
# Можно импортировать только конкретные функции из библиотеки, для сокращения вызова их в коде.
from os.path import join, dirname
# Или можно импортировать функцию как переменную
import os.path as path

# Задаем пусть в вие последовательности папок в списке
work_path = ['home', 'user', 'ivan']
print(work_path)
print(*work_path)

# Объеденяем именя папок в путь формата операционной системы (для каждлой свой формат)
new_path = join(*work_path)  # А можно написать new_path = os.path.join
print(new_path)

# Выводим путь и имя текущего (в катором написан данный код) файла
print(__file__)

# Задаем переменной полнй путь до текущего файла
dir_name = dirname(path.realpath(__file__))
print(dir_name)

# Добавляем к текущему пути папку выше
dir_name = join(dir_name, 'homeworks')
print(dir_name)

# Меняем текущую (рабочую) папку на новую
os.chdir(dir_name)

# выводим списко файлов в текущей папке по фильтру
print(glob.glob('*.py'))

# получение списка файлов определенного расширения.
image_file_ext = ('jpg', 'png', 'jpeg', 'gif', 'bmp')
image_files = list()
working_path = 'C:\Windows\System32'
for file in os.listdir(working_path):
    if file.endswith(image_file_ext):
        image_files.append(file)
if len(image_files) == 0:
    print('no image files in the directory: "' + working_path + '"')
print(image_files)
