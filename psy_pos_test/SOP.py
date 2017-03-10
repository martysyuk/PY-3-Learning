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
        if name == '': break
        age = input('Возраст: ')
        sex = input('Пол (м/ж): ')
        chooses = input('Номера отмеченных ответов через запятую (безпробелов):\n').rstrip().split(',')

        input_data.update({name: {'Возреаст': age, 'Пол': sex, 'Выбор': chooses, 'social_orient_balance': 0,
                                  'over_rules_balance': 0, 'addictive_behavior': 0, 'self_harm_behavior': 0,
                                  'aggression_behavior': 0, 'emotional_reaction': 0, 'delinquency_behavior': 0,
                                  'women_social_role': 0}})

    return input_data


def counting_individual_balls(data, person):
    for i in range(len(data[person]['Выбор'])):
        if data[person]['Пол'] == 'м':  # Подсчет балов для Мальчиков
            for key in keys[]:
                if (int(data[person]['Выбор'][i]) in key['has_it']) | \
                        (int(data[person]['Выбор'][i]) not in key['has_not']):
                    data[person][key] += 1

            # if (int(data[person]['Выбор'][i]) in boys_social_orient_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in boys_social_orient_keys_no):
            #     key_balls[person]['social_orient_balance'] += 1
            # if (int(data[person]['Выбор'][i]) in boys_over_rules_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in boys_over_rules_keys_no):
            #     key_balls[person]['over_rules_balance'] += 1
            # if (int(data[person]['Выбор'][i]) in boys_addictive_behavior_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in boys_addictive_behavior_keys_no):
            #     key_balls[person]['addictive_behavior'] += 1
            # if (int(data[person]['Выбор'][i]) in boys_self_harm_behavior_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in boys_self_harm_behavior_keys_no):
            #     key_balls[person]['self_harm_behavior'] += 1
            # if (int(data[person]['Выбор'][i]) in boys_aggression_behavior_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in boys_aggression_behavior_keys_no):
            #     key_balls[person]['aggression_behavior'] += 1
            # if (int(data[person]['Выбор'][i]) in boys_emotional_reaction_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in boys_emotional_reaction_keys_no):
            #     key_balls[person]['emotional_reaction'] += 1
            # if (int(data[person]['Выбор'][i]) in boys_delinquency_behavior_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in boys_delinquency_behavior_keys_no):
            #     key_balls[person]['delinquency_behavior'] += 1

        if data[person]['Пол'] == 'ж':  # Подсчет балов для Девочек
            print('sss')
            # if (int(data[person]['Выбор'][i]) in girls_social_orient_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in girls_social_orient_keys_no):
            #     key_balls[person]['social_orient_balance'] += 1
            # if (int(data[person]['Выбор'][i]) in girls_over_rules_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in girls_over_rules_keys_no):
            #     key_balls[person]['over_rules_balance'] += 1
            # if (int(data[person]['Выбор'][i]) in girls_addictive_behavior_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in girls_addictive_behavior_keys_no):
            #     key_balls[person]['addictive_behavior'] += 1
            # if (int(data[person]['Выбор'][i]) in girls_self_harm_behavior_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in girls_self_harm_behavior_keys_no):
            #     key_balls[person]['self_harm_behavior'] += 1
            # if (int(data[person]['Выбор'][i]) in girls_aggression_behavior_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in girls_aggression_behavior_keys_no):
            #     key_balls[person]['aggression_behavior'] += 1
            # if (int(data[person]['Выбор'][i]) in girls_emotional_reaction_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in girls_emotional_reaction_keys_no):
            #     key_balls[person]['emotional_reaction'] += 1
            # if (int(data[person]['Выбор'][i]) in girls_delinquency_behavior_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in girls_delinquency_behavior_keys_no):
            #     key_balls[person]['delinquency_behavior'] += 1
            # if (int(data[person]['Выбор'][i]) in women_social_role_keys_yes) | \
            #         (int(data[person]['Выбор'][i]) not in women_social_role_keys_no):
            #     key_balls[person]['women_social_role'] += 1


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
            for person in data:
                counting_individual_balls(data, person)
        elif choose == 'q':
            if data != {}:
                save_data_to_json_file(file_name, data)
                print('\nФАЙЛ УСПЕШНО СОХРАНЕН.')
            elif data == load_data:
                print('\nНЕ БЫЛО ВНЕСЕНО НОВЫХ ДАННЫХ')
            break


# file_name = input('Введите имя файла для сохранения данных: ')
file_name = '12-7a.json'

keys = open_keys_json_file('sop_keys.json')
choose_menu(open_json_data_file(file_name))
