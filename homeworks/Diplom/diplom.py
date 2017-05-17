# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

import config
import vkapi as vk
import json
import time


def get_friends_list_in_user_groups(_groups, _friends):
    _groups_in = dict()
    _max_count = len(_groups)
    for _current_count, _group in enumerate(_groups, 1):
        _user_list = vk.get_users_list_in_group(_group)
        print('Выполнено {} из {} запросов.'.format(_current_count, _max_count))
        _result = list(set(_user_list) & set(_friends))
        if not _result:
            _append = vk.get_group_info(_group)
            try:
                _groups_in.update({_group: {'Name': _append['name'], 'Description': _append['description']}})
            except KeyError:
                pass
            except Exception:
                time.sleep(1)
                _append = vk.get_group_info(_group)
                _groups_in.update({_group: {'Name': _append['name'], 'Description': _append['description']}})
    print('\n')
    if _groups_in:
        return _groups_in


def save_to_json(_file, _data):
    with open(_file, 'w', encoding='utf8') as json_file:
        try:
            json.dump(_data, json_file, ensure_ascii=False, indent=2)
            print('Результат обработки сохранен в файл {}'.format(_file))
        except OSError:
            print('Ошибка сохранения файла.')
    pass


user_id, user_first_name, user_last_name = vk.get_user_data(config.USER_ID)
print('Проверяем данные для пользователя: {} {} (id: {})'.format(user_last_name, user_first_name, user_id))

groups_list = vk.get_user_groups_list(user_id)
friends_list = vk.get_user_friends_list(user_id)
save_to_json(config.FILE_NAME, get_friends_list_in_user_groups(groups_list, friends_list))
