# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com

Модуль для работы с ВКонтакте API
"""

from urllib.parse import urlencode, urlparse
import requests
import config
import time

AUTHORIZE_URL = 'http://oauth.vk.com/authorize'


def print_access_token_url(_scope):
    auth_data = {
        'client_id': config.APP_ID,
        'display': 'popup',
        'response_type': 'token',
        'scope': '_scope',
        'v': config.VERSION
    }
    print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))


def get_user_data(_id):
    try:
        user_data = api_request('users.get', {'user_ids': _id})['response']
    except KeyError:
        print('Error')
    return user_data[0]['id'], user_data[0]['first_name'], user_data[0]['last_name']


def api_request(method, params):
    params.update({'access_token': config.VK_API_TOKEN,
                   'v': config.VERSION
                   })
    response = requests.get('https://api.vk.com/method/'+method, params)
    return response.json()
