# -*- coding: utf8 -*-

import json

# Шкала установки на социально-желательные ответы.
boys_social_orient_keys_yes = [13, 30, 32]
boys_social_orient_keys_no = [2, 4, 6, 21, 23, 33, 38, 47, 54, 79, 83, 87]
girls_social_orient_keys_yes = [13, 30, 32]
girls_social_orient_keys_no = [2, 4, 8, 21, 33, 38, 45, 79, 83, 87]

# Шкала склонности к преодолению норм и правил.
boys_over_rules_keys_yes = [11, 22, 34, 41, 44, 50, 53, 59, 80, 88, 91]
boys_over_rules_keys_no = [1, 10, 55, 61, 86, 93]
girls_over_rules_keys_yes = [1, 11, 22, 34, 41, 44, 50, 53, 55, 59, 61, 80, 91]
girls_over_rules_keys_no = [10, 86, 93]

# Шкала склонности к аддиктивному поведению.
boys_addictive_behavior_keys_yes = [14, 18, 22, 26, 27, 31, 34, 35, 43, 46, 59, 60, 62, 63, 64, 67, 74, 81, 91]
boys_addictive_behavior_keys_no = [95]
girls_addictive_behavior_keys_yes = [14, 18, 22, 26, 27, 31, 34, 35, 43, 59, 60, 62, 63, 64, 67, 74, 81, 91]
girls_addictive_behavior_keys_no = [95]

# Шкала склонности к самоповреждающему и саморазрушающему поведению.
boys_self_harm_behavior_keys_yes = [3, 6, 9, 12, 16, 27, 28, 37, 39, 51, 52, 58, 68, 73, 90, 91, 92, 96, 98]
boys_self_harm_behavior_keys_no = [24, 76]
girls_self_harm_behavior_keys_yes = [3, 6, 9, 12, 27, 28, 39, 51, 52, 58, 68, 73, 75, 76, 90, 91, 92, 96, 98, 99]
girls_self_harm_behavior_keys_no = [24]

# Шкала склонности к агрессии и насилию.
boys_aggression_behavior_keys_yes = [3, 5, 16, 17, 25, 37, 42, 45, 48, 49, 51, 65, 66, 70, 71, 72, 77, 89, 94, 97]
boys_aggression_behavior_keys_no = [15, 40, 75, 82]
girls_aggression_behavior_keys_yes = [3, 5, 16, 17, 25, 42, 45, 48, 49, 51, 65, 66, 71, 77, 82, 85, 89, 94, 101, 102,
                                      103, 104]
girls_aggression_behavior_keys_no = [15, 40]

# Шкала волевого контроля эмоциональных реакций.
boys_emotional_reaction_keys_yes = [7, 19, 20, 36, 49, 56, 57, 69, 70, 71, 78, 84, 89, 94]
boys_emotional_reaction_keys_no = [29]
girls_emotional_reaction_keys_yes = [7, 19, 20, 36, 49, 56, 57, 69, 70, 71, 78, 84, 89, 94]
girls_emotional_reaction_keys_no = [29]

# Шкала склонности к деликвентному поведению.
boys_delinquency_behavior_keys_yes = [18, 26, 31, 34, 35, 42, 43, 44, 48, 52, 62, 63, 64, 67, 74, 91, 94]
boys_delinquency_behavior_keys_no = [55, 61, 86]
girls_delinquency_behavior_keys_yes = [1, 3, 7, 11, 25, 28, 31, 35, 43, 48, 53, 58, 61, 63, 64, 66, 79, 98, 99, 102]
girls_delinquency_behavior_keys_no = [93]

# Шкала принятия женской социальной роли.
women_social_role_keys_yes = [93, 95, 105, 107]
women_social_role_keys_no = [3, 5, 9, 16, 18, 25, 41, 45, 51, 58, 61, 68, 73, 85, 96, 106]

key_balls = dict()
keys_name = ['social_orient_balance', 'over_rules_balance', 'addictive_behavior', 'self_harm_behavior',
        'aggression_behavior', 'emotional_reaction', 'delinquency_behavior', 'women_social_role']

def add_person_in_dicts(person_in):
    keys = {person_in: {'social_orient_balance': 0, 'over_rules_balance': 0, 'addictive_behavior': 0,
                        'self_harm_behavior': 0, 'aggression_behavior': 0, 'emotional_reaction': 0,
                        'delinquency_behavior': 0, 'women_social_role': 0}}
    return keys


def counting_individual_balls(data, person):
    for i in range(len(data[person]['Выбор'])):
        if data[person]['Пол'] == 'м':  # Подсчет балов для Мальчиков
            if (int(data[person]['Выбор'][i]) in boys_social_orient_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in boys_social_orient_keys_no):
                key_balls[person]['social_orient_balance'] += 1
            if (int(data[person]['Выбор'][i]) in boys_over_rules_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in boys_over_rules_keys_no):
                key_balls[person]['over_rules_balance'] += 1
            if (int(data[person]['Выбор'][i]) in boys_addictive_behavior_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in boys_addictive_behavior_keys_no):
                key_balls[person]['addictive_behavior'] += 1
            if (int(data[person]['Выбор'][i]) in boys_self_harm_behavior_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in boys_self_harm_behavior_keys_no):
                key_balls[person]['self_harm_behavior'] += 1
            if (int(data[person]['Выбор'][i]) in boys_aggression_behavior_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in boys_aggression_behavior_keys_no):
                key_balls[person]['aggression_behavior'] += 1
            if (int(data[person]['Выбор'][i]) in boys_emotional_reaction_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in boys_emotional_reaction_keys_no):
                key_balls[person]['emotional_reaction'] += 1
            if (int(data[person]['Выбор'][i]) in boys_delinquency_behavior_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in boys_delinquency_behavior_keys_no):
                key_balls[person]['delinquency_behavior'] += 1

        if data[person]['Пол'] == 'ж':  # Подсчет балов для Девочек
            if (int(data[person]['Выбор'][i]) in girls_social_orient_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in girls_social_orient_keys_no):
                key_balls[person]['social_orient_balance'] += 1
            if (int(data[person]['Выбор'][i]) in girls_over_rules_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in girls_over_rules_keys_no):
                key_balls[person]['over_rules_balance'] += 1
            if (int(data[person]['Выбор'][i]) in girls_addictive_behavior_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in girls_addictive_behavior_keys_no):
                key_balls[person]['addictive_behavior'] += 1
            if (int(data[person]['Выбор'][i]) in girls_self_harm_behavior_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in girls_self_harm_behavior_keys_no):
                key_balls[person]['self_harm_behavior'] += 1
            if (int(data[person]['Выбор'][i]) in girls_aggression_behavior_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in girls_aggression_behavior_keys_no):
                key_balls[person]['aggression_behavior'] += 1
            if (int(data[person]['Выбор'][i]) in girls_emotional_reaction_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in girls_emotional_reaction_keys_no):
                key_balls[person]['emotional_reaction'] += 1
            if (int(data[person]['Выбор'][i]) in girls_delinquency_behavior_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in girls_delinquency_behavior_keys_no):
                key_balls[person]['delinquency_behavior'] += 1
            if (int(data[person]['Выбор'][i]) in women_social_role_keys_yes) | \
                    (int(data[person]['Выбор'][i]) not in women_social_role_keys_no):
                key_balls[person]['women_social_role'] += 1


def total_counting_balls():
    key_balls.update({'Средний бал': {}})
    for i in range(len(keys_name)):
        key_balls['Средний бал'].update({keys_name[i]: 0})
    for person in key_balls:
        for i in range(len(keys_name)):
                key_balls['Средний бал'][keys_name[i]] += key_balls[person][keys_name[i]]

    for i in range(len(keys_name)):
        key_balls['Средний бал'][keys_name[i]] = int(key_balls['Средний бал'][keys_name[i]] / (len(key_balls) - 1))

    print(key_balls['Средний бал']['social_orient_balance'])


with open('12-7a.json', 'r', encoding='utf8') as f:
    load_data = json.loads(f.read())
    for persona in load_data:
        key_balls.update(add_person_in_dicts(persona))
        counting_individual_balls(load_data, persona)
    print(key_balls)
    total_counting_balls()
