# -*- coding: UTF-8 -*-
# Домашнее задание по уроку 2.6
# «Вызов внешних программ»
# Выполнил Мартысюк Илья PY-3


import os
import glob
from os.path import join, dirname, realpath, exists
from subprocess import Popen, PIPE


def get_image_files_list(sub_dir):
    work_dir = dirname(realpath(__file__))
    images_path = join(work_dir, sub_dir)
    os.chdir(images_path)
    files = glob.glob('*.jpg')
    os.chdir(work_dir)
    if files == list():
        print('В папке \"{}\" файлов не найдено!'.format(images_path))
        exit(0)
    else:
        return files


def subprocess_run(image_files, source_dir, result_dir):
    for file_name in image_files:
        get_file_name = join(source_dir, file_name)
        done_file_name = join(result_dir, file_name)
        # convert input.jpg -resize 200 output.jpg
        process = Popen(['convert', get_file_name, '-resize', '200', done_file_name], stdout=PIPE, stderr=PIPE)
        process.communicate()
        if process.returncode != 0:
            print('ОШИБКА конвертации файла {}.'.format(file_name))
        else:
            print('Конвертация файла {} успешно завершина'.format(file_name))


def check_and_create_folder(chk_dir, what_is_dir):
    if chk_dir == '':
        chk_dir = input('Введите имя папки {}: '.format(what_is_dir))
    chk_dir = join(dirname(realpath(__file__)), chk_dir)
    if not exists(chk_dir):
        os.mkdir(chk_dir)


# Папки относительно директории с Python файлом.
source_folder = 'Source'
result_folder = 'Result'
# Файл convert.exe должен лежать в тойже папке что и Python файл.

print('Проверям папку с картинками...')
check_and_create_folder(source_folder, 'с картинками')
print('Проверяем папку назначения...')
check_and_create_folder(result_folder, 'назначения')
print('Программа готова к работе.\n')

files_list = get_image_files_list(source_folder)
subprocess_run(files_list, source_folder, result_folder)
