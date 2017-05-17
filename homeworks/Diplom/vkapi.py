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


def api_request(method, params):
    params.update({'access_token': config.VK_API_TOKEN,
                   'v': config.VERSION
                   })
    response = requests.get('https://api.vk.com/method/' + method, params)
    return response.json()


def get_user_data(_id):
    _response = api_request('users.get', {'user_ids': _id})
    try:
        return _response['response'][0]['id'], _response['response'][0]['first_name'], \
               _response['response'][0]['last_name']
    except KeyError:
        print('Error code: {}: {}'.format(_response['error_code'], _response['error_msg']))
        if _response['error']['error_code'] == 6:
            print('Try again in 1 second...\n')
    return []


def get_user_groups_list(_user_id):
    _response = api_request('groups.get', {'user_id': _user_id})
    try:
        return _response['response']['items']
    except KeyError:
        print('Error code: {}: {}'.format(_response['error_code'], _response['error_msg']))
        if _response['error']['error_code'] == 6:
            print('Try again in 1 second...\n')
    return []


def get_user_friends_list(_user_id):
    _response = api_request('friends.get', {'user_id': _user_id})
    try:
        return _response['response']['items']
    except KeyError:
        print('Error code: {}: {}'.format(_response['error_code'], _response['error_msg']))
        if _response['error']['error_code'] == 6:
            print('Try again in 1 second...\n')
    return []


def get_users_list_in_group(_group_id):
    _response = api_request('groups.getMembers', {'group_id': _group_id})
    try:
        return _response['response']['items']
    except KeyError:
        print('\nError code {}: {} (group ID: {})'.format(_response['error']['error_code'],
                                                          _response['error']['error_msg'], _group_id))
        if _response['error']['error_code'] == 6:
            print('Try again in 1 second...\n')
    return []


def get_group_info(_group_id):
    _response = api_request('groups.getById', {'group_id': _group_id, 'fields': 'description'})
    try:
        return _response['response'][0]
    except KeyError:
        print('\nError code {}: {} (group ID: {})'.format(_response['error']['error_code'],
                                                          _response['error']['error_msg'], _group_id))
        if _response['error']['error_code'] == 6:
            print('Try again in 1 second...\n')
    return []
