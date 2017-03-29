# -*- coding: UTF-8 -*-
"""
Досашнее задание 3-3
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

from pprint import PrettyPrinter as pprint
import requests
from os.path import join, dirname, realpath

API_KEY = 'trnsl.1.1.20170329T070804Z.1af026d5fbe12cb2.49a4b99c28bc72c3e7f75c59a1b4e60e4977efe3'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
files_folder = 'texts'
files_type = '.txt'
to_lang='ru'
texts = dict()
trans_texts = dict()


def translate_it(text, from_lang='en', to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return '\n'.join(json_['text'])


def open_text_file(dir, file_name):
    file_name = file_name + files_type
    load_file = join(dirname(realpath(__file__)), dir, file_name)
    try:
        with open(load_file, 'r') as file:
            return file.read()
    except:
        print('Файла {} не найдено.'.format(load_file))


def save_translate_to_file(lang_to_lang, text, dir):
    file_name = lang_to_lang + files_type
    file_name = join(dirname(realpath(__file__)), dir, file_name)
    try:
        with open(file_name, 'w', encoding='utf8') as file:
            file.write(text)
    except:
        print('Ошибка запипи в файл {}'.format(file_name))


def get_texts(*langs):
    for lang in langs:
        texts.update({lang: open_text_file(files_folder, lang)})


get_texts('de', 'es', 'fr')
for lang in texts:
    print('Переводим текст с {} на {}'.format(lang, to_lang))
    translate_text = translate_it(texts[lang], lang, to_lang)
    lang_to_lang = lang+'-'+to_lang
    trans_texts.update({lang_to_lang: translate_text})
    print('Сохраняем файл с переводом {}{}'.format(lang_to_lang, files_type))
    save_translate_to_file(lang_to_lang, trans_texts[lang_to_lang], files_folder)
