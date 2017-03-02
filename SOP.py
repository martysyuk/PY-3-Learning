# -*- coding: utf8 -*-
# Программа генирации файла JSON с данными ответов по тесту СОП Орлова

import json


def open_json_data_file(path):
    print('ЧИТАЕМ ДАННЫЕ ИЗ ФАЙЛА: {}'.format(path))
    try:
        with open(path, 'r', encoding='utf8') as f:
            try:
                load_data = json.loads(f.read())
                return load_data
            except:
                print('\nВ ФАЙЛЕ ДАННЫХ НЕ ОБНАРУЖЕНО\n')
                return
    except:
        print('\nФАЙЛ НЕ ОБНАРУЖЕН.\nСОЗДАЕМ НОВЫЙ ФАЙЛ {}\n'.format(path))


def input_new_data():
    print('ВВОД НОВЫХ ДАННЫХ\nДля завершения введите пустое имя тестируемого.\n')
    input_data = dict()
    while True:
        name = input('Имя тестируемого: ')
        if name == '': break
        age = input('Возраст: ')
        sex = input('Пол (м/ж): ')
        chooses = input('Номера отмеченных ответов через запятую (безпробелов):\n').rstrip().split(',')

        input_data.update({name: {'Возреаст': age, 'Пол': sex, 'Выбор': chooses}})

    return input_data


def save_data_to_json_file(path):
    with open(path, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)


def choose_menu():
    print('\n'*100)
    print('Программа обработки даных теста СОП Орлова\n\n')
    print('МЕНЮ ПРОГРАММЫ:\n\n')
    print('1. Вывести список имеющихся респондентов')
    print('2. Добавить новые данные')


# file_name = input('Введите имя файла для сохранения данных: ')
file_name = '12-7a.json'
load_data = open_json_data_file(file_name)
if load_data != None:
    data = load_data
    data.update(input_new_data())
else:
    data = (input_new_data())

if data != {}:
    save_data_to_json_file(file_name)
    print('\nФАЙЛ УСПЕШНО СОХРАНЕН.')
else:
    print('\nНЕ БЫЛО ВНЕСЕНО НОВЫХ ДАННЫХ')