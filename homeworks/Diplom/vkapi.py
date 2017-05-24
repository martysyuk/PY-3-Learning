# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com

Модуль для работы с ВКонтакте API
"""

import requests
import config
import time


def response_error(_response):
    if _response['error']['error_code'] == 6:
        time.sleep(1)
        return True
    else:
        print('Error code: {}: {}'.format(_response['error']['error_code'], _response['error']['error_msg']))
        return False


def get_vk_response(_method, _params):
    _params.update({'access_token': config.VK_API_TOKEN,
                    'v': config.VERSION
                    })
    while True:
        _response = requests.get('https://api.vk.com/method/' + _method, _params).json()
        try:
            return _response['response']
        except KeyError:
            if response_error(_response):
                continue
            else:
                return False
