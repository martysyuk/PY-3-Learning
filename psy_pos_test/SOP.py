# -*- coding: utf8 -*-
# Программа генирации файла JSON с данными ответов по тесту СОП Орлова

import json


def open_json_data_file(path):
    print('ЧИТАЕМ ДАННЫЕ ИЗ ФАЙЛА: {}'.format(path))
    try:
        with open(path, 'r', encoding='utf8') as f:
            try:
                data = json.loads(f.read())
                return data
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

        input_data.update({name: {'Возреаст': age, 'Пол': sex, 'Выбор': chooses, 'social_orient_balance': 0,
                                  'over_rules_balance': 0, 'addictive_behavior': 0, 'self_harm_behavior': 0,
                                  'aggression_behavior': 0, 'emotional_reaction': 0, 'delinquency_behavior': 0,
                                  'women_social_role': 0}})

    return input_data


def save_data_to_json_file(path, data):
    with open(path, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)


def choose_menu(data):
    print('Программа обработки даных теста СОП Орлова\n\n')
    print('МЕНЮ ПРОГРАММЫ:\n\n')
    print('1. Вывести список имеющихся респондентов')
    print('2. Добавить новые данные')
    print('3. Вывести результаты тестирования')
    print('q. Выход')
    choose = 0

    while choose != 'q':
        choose = input('\nСделайте выбор (1, 2, 3 или q): ')
        if choose == '1':
            list_data(data)
        elif choose == '2':
            if data is not None:
                data.update(input_new_data())
            else:
                data = (input_new_data())
        elif choose == '3':
            asd
        elif choose == 'q':
            if (data != {}):
                save_data_to_json_file(file_name, data)
                print('\nФАЙЛ УСПЕШНО СОХРАНЕН.')
            elif data == load_data:
                print('\nНЕ БЫЛО ВНЕСЕНО НОВЫХ ДАННЫХ')
            break


def list_data(data):
    for person in data:
        print(person+', {} лет'.format(data[person]['Возреаст']))


# file_name = input('Введите имя файла для сохранения данных: ')
file_name = '12-7a.json'

choose_menu(open_json_data_file(file_name))
