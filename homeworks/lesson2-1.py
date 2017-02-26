# Домашнее задание по уроку 2.1
# «Открытие и чтение файла, запись в файл»
# Выполнил Мартысюк Илья PY-3

# В Windows 10 Russian у меня проблема с выводом руссих слов из файла,
# по этому список блюд и продуктов сделан на английском.

with open('lesson2-1.txt', 'r') as f:
    title_line_number = 0
    for index, line in enumerate(f):
        if index == title_line_number:
            print(line.rstrip())
        elif line.rstrip().isdigit():
            title_line_number += int(line)+2
