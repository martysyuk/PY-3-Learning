# -*- coding: UTF-8 -*-
# Домашнее задание по уроку 2.5
# «Работа с папками, путями»
# Выполнил Мартысюк Илья PY-3

import glob
from os.path import join


def search_in_files(search, files_list):
    temp_filtered_list = list()
    for index, file in enumerate(files_list):
        with open(file, 'r') as work_file:
            data = work_file.read().lower()
            if search in data:
                temp_filtered_list.append(file)

    return temp_filtered_list


def print_result(data):
    file_count = 0
    print('\nИскомая фраза встрачается в файлах:')
    for index, data_stdout in enumerate(data):
        print(str(index+1), ')', data_stdout)
        file_count += 1
    print('Всего найденых файлов: {}\n'.format(file_count))


work_dir = ['lesson2-5', 'homework', 'Advanced']
files = glob.glob(join(*work_dir, '*.sql'))
filtered_list = files


while True:
    search_str = input('Введите искомое слово: ')
    if search_str == '':
        exit(0)
    search_str = search_str.lower()
    filtered_list = search_in_files(search_str, filtered_list)
    print_result(filtered_list)
