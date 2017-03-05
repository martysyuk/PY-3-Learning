# -*- coding: utf8 -*-

import json

with open('12-7a.json', 'r', encoding='utf8') as f:
    load_data = json.loads(f.read())
    for person in load_data:
        print(person+', {} лет'.format(load_data[person]['Возреаст']))