# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

import config
import vkapi as vk
import json
import sys


def point():
    sys.stdout.write('.')
    sys.stdout.flush()


def get_groups_data(_groups):
    _groups_in = dict()
    for _group in _groups:
        point()
        _append = vk.get_vk_response('groups.getById', {'group_id': _group, 'fields': 'members_count'})[0]
        try:
            _groups_in.update({_group: {'Group name': _append['name'], 'Members in group': _append['members_count']}})
        except KeyError:
            pass
    return _groups_in


def parts(lst, n=25):
    return [lst[i:i + n] for i in iter(range(0, len(lst), n))]


def get_friends_list_in_user_groups(_groups, _friends):

    def compile_execute_code(_friends_ids):
        code = 'return {'
        for _friend_id in _friends_ids:
            code = '%s%s' % (code, '"%s": API.groups.get({"user_id": %s}),' % (_friend_id, _friend_id))
        code = '%s%s' % (code, '};')
        return code

    _executions = list()
    _groups_with_friends = list()
    for _part in _friends:
        _executions.append(compile_execute_code(_part))

    for _current_count, _execut in enumerate(_executions):
        _group_list = vk.get_vk_response('execute', {'code': _execut})
        point()
        for _friend in _group_list:
            try:
                _groups_with_friends.extend(_group_list[_friend]['items'])
            except TypeError:
                pass
    _done = list(set(_groups) - set(_groups_with_friends))
    return get_groups_data(_done)


def save_to_json(_file, _data):
    with open(_file, 'w', encoding='utf8') as json_file:
        try:
            json.dump(_data, json_file, ensure_ascii=False, indent=2)
            print('\nРезультат обработки сохранен в файл {}'.format(_file))
        except OSError:
            print('\nОшибка сохранения файла.')


user_info = vk.get_vk_response('users.get', {'user_ids': config.USER})[0]
user_id = user_info['id']
print('Проверяем данные для пользователя: {} {} (id: {})'.format(user_info['last_name'], user_info['first_name'], user_id))

groups_list = vk.get_vk_response('groups.get', {'user_id': user_id})['items'][:config.MAXIMUM_GROUPS]
friends_list = vk.get_vk_response('friends.get', {'user_id': user_id})['items']

save_to_json(config.FILE_NAME, get_friends_list_in_user_groups(groups_list, parts(friends_list)))
