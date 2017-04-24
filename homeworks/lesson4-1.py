# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com

Домашка по уроку 4.1
"""

PATH = 'F:/GitHub/Python/PY-3-Learning/homeworks/names/'

years = input('Введите года через запятую: ').split(',')

def top_name(*args):
    if len(args[0]) == 1:
        print('1')
        print(args[0])
    if len(args[0]) > 1:
        print('>1')
        print(args[0])

top_name(years)
