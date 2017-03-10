# -*- coding: UTF-8 -*-
# Домашнее задание по уроку 2-2
# «Работа с разными форматами данных»
# Выполнил Мартысюк Илья PY-3

import codecs
import json
import pprint

with codecs.open('./lesson2-2/newsfr.json', encoding="iso8859_5") as news:
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(json.load(news))
