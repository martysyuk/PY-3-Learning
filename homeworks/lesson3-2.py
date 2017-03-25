# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com

«Работа с API ВК, json, работа с менеджером пакетов»
"""

from urllib.parse import urlencode, urlparse
import requests
import time
from tkinter import *
import tkinter.scrolledtext as scrolledtext

AUTHORIZE_URL = 'http://oauth.vk.com/authorize'
VERSION = '5.62'
APP_ID = 5940806
access_token = 'd017efd0a0f44f817534bb671f357f1fc5167aafd629a9e9b0f7f3e7c6684ce076c823cb32c2f9f3a2fb7'


def print_access_token_url():
    auth_data = {
        'client_id': APP_ID,
        'display': 'popup',
        'response_type': 'token',
        'scope': 'friends,messages,search,users',
        'v': VERSION
    }
    print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))


def get_access_token():
    token_url = 'https://oauth.vk.com/blank.html#access_token' \
                '=0e1d258e13b4199493b68e4fca580fcc9f53c2b2c2168614e892b57c4100cdf763682ad32e3f626e53ca1&expires_in' \
                '=86400&user_id=4119375'

    o = urlparse(token_url)
    fragments = dict((i.split('=') for i in o.fragment.split('&')))
    return fragments['access_token']


def use_vk_api(method, params):
    params.update({'access_token': access_token,
                   'v': VERSION
                   })
    response = requests.get('https://api.vk.com/method/'+method, params)
    return response.json()


def get_friends_of_friend(main_user_id, checked_friends_list, max_users, output):
    friends_of_my_friend = dict()
    response_count = 1
    if max_users == 'all':
        max_users = len(checked_friends_list)
    for index, uid in enumerate(checked_friends_list):
        if index < max_users:
            mutual = use_vk_api('friends.getMutual', {'source_uid': main_user_id, 'target_uid': uid})
            if mutual['response']:
                # print('{}) {}: {}'.format(index+1, uid, mutual['response']))
                friends_of_my_friend.update({uid: mutual['response']})
            response_count += 1
            if response_count > 3:
                time.sleep(0.5)
                response_count = 1
            output.delete(1.0, END)
            output.insert(1.0, 'Выполнено {}%'.format(int((index / len(checked_friends_list)) * 100)))
            root.update()

    output.destroy()
    output = scrolledtext.ScrolledText(font=('times', 12), width=75, height=30, wrap=WORD)
    output.pack(expand=YES, fill=BOTH)
    for each in friends_of_my_friend:
        output.insert('1.0', '\nID: ' + str(each) + ' = ' + str(friends_of_my_friend[each]) + '\n')
    output.insert('1.0', 'Всего друзей с общими друзьями {} из {}\n'.format(len(friends_of_my_friend),
                                                                            len(checked_friends_list)))
    root.mainloop()


root = Tk()
label = Text(font=('times', 12), width=75, height=1, wrap=WORD)
label.pack(expand=YES, fill=BOTH)
label.insert('1.0', 'Выполнено 0%')
root.update()

user_id = '2'
friends_list = use_vk_api('friends.get', {'user_id': user_id})['response']['items']

'''
Параметры вызова функции
1) ID осмновного пользователя.
2) Список друзей основного пользователя в виде списка с ID номерами.
3) Максимально обрабатываемое колличество друзей. если поставить 'all' обработаются все друзья.
4) Текстовое поле в окне созданном Tkinter
'''
get_friends_of_friend(user_id, friends_list, 'all', label)
