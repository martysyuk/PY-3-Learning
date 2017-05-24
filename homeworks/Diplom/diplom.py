# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

import config
import vkapi as vk
import json


def get_friends_list_in_user_groups(_groups, _friends, _maximum_friends_count):
    _groups_in = dict()
    _max_count = len(_groups)
    for _current_count, _group in enumerate(_groups, 1):
        try:
            _user_list = vk.get_vk_response('groups.getMembers', {'group_id': _group})['items']
            print('Выполнено {} из {} запросов.'.format(_current_count, _max_count))
            _result = list(set(_user_list) & set(_friends))
            if len(_result) <= _maximum_friends_count:
                _append = vk.get_vk_response('groups.getById', {'group_id': _group, 'fields': 'members_count'})[0]
                _groups_in.update({_group: {'Group name': _append['name'], 'Members in group': _append['members_count'],
                                        'Friends count': len(_result)}})
        except TypeError:
            pass
    print('\n')
    return _groups_in


def save_to_json(_file, _data):
    with open(_file, 'w', encoding='utf8') as json_file:
        try:
            json.dump(_data, json_file, ensure_ascii=False, indent=2)
            print('Результат обработки сохранен в файл {}'.format(_file))
        except OSError:
            print('Ошибка сохранения файла.')


user_info = vk.get_vk_response('users.get', {'user_ids': config.USER})[0]
user_id = user_info['id']
print('Проверяем данные для пользователя: {} {} (id: {})'.format(user_info['last_name'], user_info['first_name'], user_id))

groups_list = vk.get_vk_response('groups.get', {'user_id': user_id})['items'][:config.MAXIMUM_GROUPS]
friends_list = vk.get_vk_response('friends.get', {'user_id': user_id})['items']

save_to_json(config.FILE_NAME, get_friends_list_in_user_groups(groups_list, friends_list, config.MAXIMUM_FRIENDS_COUNT))
