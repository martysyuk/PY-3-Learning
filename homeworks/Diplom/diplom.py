# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

import config
import vkapi as vk
import json


def save_to_json(_file, _data):
    with open(_file, 'w', encoding='utf8') as json_file:
        try:
            json.dump(_data, json_file, ensure_ascii=False, indent=2)
            print('\nРезультат обработки сохранен в файл {}'.format(_file))
        except OSError:
            print('\nОшибка сохранения файла.')


def main():
    vk_request = vk.VkApi(config.USER, config.TOKEN)

    groups_list = vk_request.response('groups.get', {'user_id': vk_request.user_id})['items'][:config.MAXIMUM_GROUPS]
    friends_list = vk_request.response('friends.get', {'user_id': vk_request.user_id})['items']

    save_to_json(config.FILE_NAME, vk_request.get_friends_list_in_user_groups(groups_list, friends_list))

if __name__ == '__main__':
    main()
