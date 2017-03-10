# -*- coding: utf8 -*-


import json


def open_keys_json_file(path):
    print('ЧИТАЕМ ДАННЫЕ КЛЮЧЕЙ ИЗ ФАЙЛА: {}\n'.format(path))
    try:
        with open(path, encoding='utf8') as f:
            keys = json.loads(f.read())
            return keys
    except:
        print('ФАЙЛ КЛЮЧЕЙ НЕ НАЙДЕН!\n')
        exit(0)


def open_json_data_file(path):
    print('ЧИТАЕМ ДАННЫЕ ИЗ ФАЙЛА: {}\n'.format(path))
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


def save_data_to_json_file(path, data):
    with open(path, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)


def list_data(data):
    for person in data:
        print(person + ', {} лет'.format(data[person]['Возреаст']))


def input_new_data():
    print('ВВОД НОВЫХ ДАННЫХ\nДля завершения введите пустое имя тестируемого.\n')
    input_data = dict()
    while True:
        name = input('Имя тестируемого: ')

        if name == '':
            break

        age = input('Возраст: ')
        sex = input('Пол (м/ж): ')
        chooses = input('Номера отмеченных ответов через запятую (безпробелов):\n').rstrip().split(',')

        if sex == "м":
            input_data.update({name: {'Возреаст': age, 'Пол': sex, 'Выбор': chooses, 'social_orient_balance': 0,
                                      'over_rules_balance': 0, 'addictive_behavior': 0, 'self_harm_behavior': 0,
                                      'aggression_behavior': 0, 'emotional_reaction': 0, 'delinquency_behavior': 0}})
        elif sex == "ж":
            input_data.update({name: {'Возреаст': age, 'Пол': sex, 'Выбор': chooses, 'social_orient_balance': 0,
                                      'over_rules_balance': 0, 'addictive_behavior': 0, 'self_harm_behavior': 0,
                                      'aggression_behavior': 0, 'emotional_reaction': 0, 'delinquency_behavior': 0,
                                      'women_social_role': 0}})
    return input_data


def counting_individual_balls(data, person):
    if data[person]['Пол'] == 'м':
        for key in keys['boys_keys']:
            data[person][key] = 0
        for choose in data[person]['Выбор']:
            for key in keys['boys_keys']:
                if (int(choose) in keys['boys']['has_it'][key]) | (int(choose) not in keys['boys']['has_not'][key]):
                    data[person][key] += 1
    if data[person]['Пол'] == 'ж':
        for key in keys['girls_keys']:
            data[person][key] = 0
        for choose in data[person]['Выбор']:
            for key in keys['girls_keys']:
                if (int(choose) in keys['girls']['has_it'][key]) | (int(choose) not in keys['girls']['has_not'][key]):
                    data[person][key] += 1


def choose_menu(data):
    print('Программа обработки даных теста СОП Орлова\n\n')
    print('МЕНЮ ПРОГРАММЫ:\n\n')
    print('1. Вывести список имеющихся респондентов')
    print('2. Добавить новые данные')
    print('3. Подсчитать результаты тестирования')
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
            for person in data:
                counting_individual_balls(data, person)
        elif choose == 'q':
            if data != {}:
                save_data_to_json_file(file_name, data)
                print('\nФАЙЛ УСПЕШНО СОХРАНЕН.')
            break


# file_name = input('Введите имя файла для сохранения данных: ')
file_name = '12-7a.json'

keys = open_keys_json_file('sop_keys.json')
choose_menu(open_json_data_file(file_name))
