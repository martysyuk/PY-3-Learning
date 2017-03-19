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
    return glob.glob('*.jpg')


def subprocess_run(image_files):
    for file_name in image_files:
        done_file_name = 'resize-'+file_name
        # convert input.jpg -resize 200 output.jpg
        process = Popen(['convert', file_name, '-resize', '200', done_file_name], stdout=PIPE, stderr=PIPE)
        process.communicate()
        if process.returncode != 0:
            print('ОШИБКА конвертации файла {}.'.format(file_name))
        else:
            print('Конвертация файла {} успешно завершина'.format(file_name))


sub_folder_name = 'lesson2-6'
subprocess_run(get_image_files_list(sub_folder_name))

