# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

import config
import vkapi as vk
import sys
import json


def get_user_groups_list(_user_id):
    try:
        _response = vk.api_request('groups.get', {'user_id': _user_id})['response']
        return _response['items']
    except KeyError:
        _error = vk.api_request('groups.get', {'user_id': _user_id})['error']
        print('Error code: {}: {}'.format(_error['error_code'], _error['error_msg']))
        return ''


def get_user_friends_list(_user_id):
    try:
        _response = vk.api_request('friends.get', {'user_id': _user_id})['response']
        return _response['items']
    except KeyError:
        _error = vk.api_request('friends.get', {'user_id': _user_id})
        print('Error code: {}: {}'.format(_error['error_code'], _error['error_msg']))
        return ''


def get_users_list_in_group(_group_id):
    try:
        _response = vk.api_request('groups.getMembers', {'group_id': _group_id})['response']
        return _response['items']
    except KeyError:
        _error = vk.api_request('groups.getMembers', {'group_id': _group_id})
        print('\nError code: {}: {} (group ID: {})'.format(_error['error']['error_code'], _error['error']['error_msg'], _group_id))
        return ''


def get_group_info(_group_id):
    try:
        _response = vk.api_request('groups.getById', {'group_id': _group_id, 'fields': 'description'})['response']
        return _response[0]
    except KeyError:
        _error = vk.api_request('groups.getMembers', {'group_id': _group_id})
        print('\nError code: {}: {} (group ID: {})'.format(_error['error']['error_code'], _error['error']['error_msg'], _group_id))
        return ''


def get_friends_list_in_user_groups(_groups, _friends):
    _groups_in = dict()
    for _group in _groups:
        _user_list = get_users_list_in_group(_group)
        sys.stdout.write('.')
        sys.stdout.flush()
        _result = list(set(_user_list) & set(_friends))
        if not _result:
            _append = get_group_info(_group)
            try:
                _groups_in.update({_group: {'Name': _append['name'], 'Description': _append['description']}})
            except KeyError:
                pass
    print('\n')
    if _groups_in:
        return _groups_in


def search_user_with_1000_groups():
    for x in range(100,1000000):
        print('Проверяем ID: {}'.format(str(x)))
        if get_user_groups_list(x) >= 1000:
            print(x)
            break


def save_to_json(_file, _data):
    with open(_file, 'w', encoding='utf8') as json_file:
        try:
            json.dump(_data, json_file, ensure_ascii=False, indent=2)
            print('Результат обработки сохранен в файл {}'.format(_file))
        except OSError:
            print('Ошибка сохранения файла.')
    pass


#search_user_with_1000_groups()

user_id, user_first_name, user_last_name = vk.get_user_data(config.USER_ID)
print('Проверяем данные для пользователя: {} {} (id: {})'.format(user_last_name, user_first_name, user_id))

groups_list = get_user_groups_list(user_id)
friends_list = get_user_friends_list(user_id)
save_to_json(config.FILE_NAME, get_friends_list_in_user_groups(groups_list, friends_list))
