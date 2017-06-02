# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com

Модуль для работы с ВКонтакте API
"""

import requests
import time
import sys


class VkApi:

    def __init__(self, user_id, token, api_ver='5.64'):
        self.token = token
        self.api_ver = api_ver
        self.user_info = self.response('users.get', {'user_ids': user_id})[0]
        self.user_id = self.user_info['id']
        print('Проверяем данные для пользователя: {} {} (id: {})'.format(self.user_info['last_name'],
                                                                         self.user_info['first_name'],
                                                                         self.user_id))

    @staticmethod
    def response_error(_response):
        if _response['error']['error_code'] == 6:
            time.sleep(0.5)
            return True
        else:
            print('Error code: {}: {}'.format(_response['error']['error_code'], _response['error']['error_msg']))
            return False

    def response(self, _method, _params):
        _params.update({'access_token': self.token,
                        'v': self.api_ver
                        })
        while True:
            _response = requests.get('https://api.vk.com/method/' + _method, _params).json()
            try:
                return _response['response']
            except KeyError:
                if self.response_error(_response):
                    continue
                else:
                    return False

    def get_groups_data(self, _groups):
        _groups_in = dict()
        for _group in _groups:
            point()
            _append = self.response('groups.getById', {'group_id': _group, 'fields': 'members_count'})[0]
            try:
                _groups_in.update({_group: {'Group name': _append['name'], 'Members in group': _append['members_count']}})
            except KeyError:
                pass
        return _groups_in

    def get_friends_list_in_user_groups(self, _groups, _friends):

        def parts(lst, n=25):
            return [lst[i:i + n] for i in iter(range(0, len(lst), n))]

        def compile_execute_code(_friends_ids):
            code = 'return {'
            for _friend_id in _friends_ids:
                code = '%s%s' % (code, '"%s": API.groups.get({"user_id": %s}),' % (_friend_id, _friend_id))
            code = '%s%s' % (code, '};')
            return code

        _friends = parts(_friends)
        _executions = list()
        _groups_with_friends = list()
        for _part in _friends:
            _executions.append(compile_execute_code(_part))

        for _current_count, _execut in enumerate(_executions):
            _group_list = self.response('execute', {'code': _execut})
            point()
            for _friend in _group_list:
                try:
                    _groups_with_friends.extend(_group_list[_friend]['items'])
                except TypeError:
                    pass
        _done = list(set(_groups) - set(_groups_with_friends))
        return self.get_groups_data(_done)


def point():
    sys.stdout.write('.')
    sys.stdout.flush()
