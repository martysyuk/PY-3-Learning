# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

import config
import vkapi as vk
import json
from pprint import pprint


def start_execute(_lst):
    print('Ожидаем ответ от серверов ВКонтакте.')

    def parts(lst, n=25):
        return [lst[i:i + n] for i in iter(range(0, len(lst), n))]

    result = []
    for _short_list in parts(_lst):
        code = 'return {'
        for _group_id in _short_list:
            code = '%s%s' % (code, '"%s": API.groups.getMembers({"group_id": %s}),' % (_group_id, _group_id))
        code = '%s%s' % (code, '};')
        _params = {'access_token': config.VK_API_TOKEN,
                   'v': config.VERSION,
                   'code': code
                   }
        result.append(vk.requests.get('https://api.vk.com/method/execute', _params).json())

    print('Ответ получен. Начинаем обработку данных.')
    return result


def calculate_data(_data, _friends):
    _groups_in = dict()
    _max_count = len(_data[0]['response'])
    for _current_count, _group in enumerate(_data[0]['response'], 1):
        print('Выполнено {} из {} запросов.'.format(_current_count, _max_count))
        _result = list(set(_data[0]['response'][_group]) & set(_friends))
        if not _result:
            _append = vk.get_vk_response('groups.getById', {'group_id': _group, 'fields': 'description'})[0]
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


user_info = vk.get_vk_response('users.get', {'user_ids': config.USER})[0]
user_id = user_info['id']
print('Проверяем данные для пользователя: {} {} (id: {})'.format(user_info['last_name'], user_info['first_name'],
                                                                 user_id))

groups_list = vk.get_vk_response('groups.get', {'user_id': user_id})['items']
friends_list = vk.get_vk_response('friends.get', {'user_id': user_id})['items']

save_to_json(config.FILE_NAME, calculate_data(start_execute(groups_list), friends_list))

# save_to_json(config.FILE_NAME, get_friends_list_in_user_groups(groups_list, friends_list))
