# Импорт библиотеки целиком
import os
import glob
# Можно импортировать только конкретные функции из библиотеки, для сокращения вызова их в коде.
from os.path import join, dirname, realpath

# Задаем пусть в вие последовательности папок в списке
path = ['home', 'user', 'ivan']
print(path)
print(*path)
# Объеденяем именя папок в путь формата операционной системы (для каждлой свой формат)
new_path = join(*path) # А можно написать new_path = os.path.join
print(new_path)
# Выводим путь и имя текущего (в катором написан данный код) файла
print(__file__)
# Задаем переменной полнй путь до текущего файла
dir_name = dirname(realpath(__file__))
print(dir_name)
# Добавляем к текущему пути папку выше
dir_name = join(dir_name, 'homeworks')
print(dir_name)
# Меняем текущую (рабочую) папку на новую
os.chdir(dir_name)
# выводим списко файлов в текущей папке по фильтру
print(glob.glob('*.py'))