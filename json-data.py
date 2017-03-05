# -*- coding: utf8 -*-
# Обработчик текстового файла и запись его в формате json
# Выполнил Мартысюк Илья PY-3

import json

cook_book = dict()


def cook_book_open():
    ingridients = list()
    with open('homeworks\lesson2-1.txt', 'r', encoding='UTF8') as f:
        line = f.readline()
        while line:
            dish_name = line.rstrip()
            ingridients_count = int(f.readline())
            cook_book.update({dish_name: {'name': dish_name, 'ingridients': []}})

            for i in range(ingridients_count):
                ingridients.append(f.readline().rstrip().split(' | '))

            for i in range(ingridients_count):
                cook_book[dish_name]['ingridients'] += [{'product': ingridients[i][0],
                                                         'quantity': int(ingridients[i][1]),
                                                         'unit': ingridients[i][2]}]

            line = f.readline()
            ingridients = list()


cook_book_open()

with open('json-data.json', 'w', encoding='utf8') as f:
    json.dump(cook_book, f, ensure_ascii=False, indent=2)
