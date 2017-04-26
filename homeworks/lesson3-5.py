# -*- coding: UTF-8 -*-
"""
Lesson 3.5

Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

import requests
from urllib.parse import urlencode, urlparse, urljoin


'''
Запрос TOKEN

API_ID = '2d0728f98b08438184dd2ec406a1e281'
API_KEY = 'f2cb02016e37496d8c772c02db6f281e'
AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
API_CALLBACK_URL = 'https://oauth.yandex.ru/verification_code'


def print_access_token_url():
    auth_data = {
        'client_id': API_ID,
        'response_type': 'token'
    }
    print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))

print_access_token_url()
'''


TOKEN = 'AQAAAAAAZ6SoAAQ6br8a4qhCzUHWgwIdjsZ-4Nk'


class YandexMetrika(object):
    _METRIKA_STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/'
    _METRIKA_MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/'
    token = None

    def __init__(self, token):
        self.token = token

    def get_header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def counter_list(self):
        url = urljoin(self._METRIKA_MANAGEMENT_URL, 'counters')
        headers = self.get_header()
        response = requests.get(url, headers=headers)
        counter_list = [c['id'] for c in response.json()['counters']]
        return counter_list

    def visits(self, counter_id):
        url = urljoin(self._METRIKA_STAT_URL, 'data')
        headers = self.get_header()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits'
        }
        response = requests.get(url, params, headers=headers)
        visits = response.json()['data'][0]['metrics'][0]
        return visits

    def pageviews(self, counter_id):
        url = urljoin(self._METRIKA_STAT_URL, 'data')
        headers = self.get_header()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:pageviews'
        }
        response = requests.get(url, params, headers=headers)
        pageviews = response.json()['data'][0]['metrics'][0]
        return pageviews

    def users(self, counter_id):
        url = urljoin(self._METRIKA_STAT_URL, 'data')
        headers = self.get_header()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:users'
        }
        response = requests.get(url, params, headers=headers)
        users = response.json()['data'][0]['metrics'][0]
        return users

counter = '44427730'

metrika = YandexMetrika(TOKEN)
print('Всего визитов: {}'.format(metrika.visits(counter)))
print('Всего просмотров: {}'.format(metrika.pageviews(counter)))
print('Всего посетителей: {}'.format(metrika.users(counter)))
