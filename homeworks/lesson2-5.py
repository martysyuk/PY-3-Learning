# -*- coding: UTF-8 -*-
# Домашнее задание по уроку 2.5
# «Работа с папками, путями»
# Выполнил Мартысюк Илья PY-3

import glob
from os.path import join

work_dir = ['lesson2-5','homework','Advanced']
files = glob.glob(join(*work_dir, '*.sql'))
filtered_list = files


# def filter_files(filter):
#     filter = '*' + filter + '*.sql'
#     files = glob.glob(join(*work_dir, filter))
#     for index, file in enumerate(files):
#         print(str(index+1)+') '+file)
#     print('Всего {} файлов.'.format(str(len(files))))

while True:
    user_filter = input('Введите фильтр: ')
    if user_filter == '':
        exit(0)
    filtered_list = filter(lambda x: x.find(user_filter), files)
    print(filtered_list)