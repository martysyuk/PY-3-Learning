# -*- coding: UTF-8 -*-
# Домашнее задание по уроку 2-2
# «Работа с разными форматами данных»
# Выполнил Мартысюк Илья PY-3


import xml.etree.cElementTree as ET
import re


def open_data_file(path, encoding):
    parser = ET.XMLParser(encoding=encoding)
    tree = ET.parse(path, parser=parser)
    root = tree.getroot()
    return root


def compile_data(root):
    long_dict = dict()
    for i in root.iter('description'):
        cleanr = re.compile(r'<.*?>|[^\w\s]+|[\d]+|[a-z]+|[A-Z]+|[\n]')
        cleantext = cleanr.sub('', i.text)
        temp_list = cleantext.strip().split(' ')
        for t in temp_list:
            if len(t) > 6:
                try:
                    long_dict[t] += 1
                except KeyError:
                    long_dict.update({t: 1})

    long_dict = sorted(long_dict.items(), key=lambda x: x[1], reverse=True)
    print(long_dict)

    return long_dict


def print_result(long_dict):
    print('ТОП 10 самых часто встречающихся слов:')
    for i in range(10):
        print('{}) Слово "{}" встречается {} раз'.format(i+1, long_dict[i][0], long_dict[i][1]))

path = './lesson2-2/newsafr.xml'
encoding = 'utf-8'
print_result(compile_data(open_data_file(path, encoding)))