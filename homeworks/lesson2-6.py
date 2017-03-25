# -*- coding: UTF-8 -*-
# Домашнее задание по уроку 2.6
# «Вызов внешних программ»
# Выполнил Мартысюк Илья PY-3

import os
import glob
from os.path import join, dirname, realpath
from subprocess import Popen, PIPE


def get_image_files_list(sub_dir):
    work_dir = dirname(realpath(__file__))
    images_path = join(work_dir, sub_dir)
    os.chdir(images_path)
    files = glob.glob('*.jpg')
    os.chdir(work_dir)
    return files


def subprocess_run(image_files, source_dir, result_dir):
    for file_name in image_files:
        get_file_name = join(source_dir, file_name)
        done_file_name = join(result_dir, file_name)
        # convert input.jpg -resize 200 output.jpg
        process = Popen(['convert', get_file_name, '-resize', '200', done_file_name])#, stdout=PIPE, stderr=PIPE)
        process.communicate()
        if process.returncode != 0:
            print('ОШИБКА конвертации файла {}.'.format(file_name))
            print(process.returncode)
        else:
            print('Конвертация файла {} успешно завершина'.format(file_name))


source_folder = 'Source'
result_folder = 'Result'
files_list = get_image_files_list(source_folder)
subprocess_run(files_list, source_folder, result_folder)

