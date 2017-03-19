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
