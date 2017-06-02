# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

# mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# a = [x**3 for x in mass if (x % 3 == 0) & (x % 4 == 0)]
#
# print(a)




# _user_list = ['f', 'a', 'b', 'c']
# _friends = ['b', 'a', 'd', 'e']
#
# _result = list(set(_user_list) - set(_friends))
#
# print(_result)


# def uppsercase_and_revers(text):
#     return text[::-1].upper()
#
# print(uppsercase_and_revers('Hello World'))

# a = '12345'
# b = list(map(lambda i: c += int(i), list(a)))
# print(b)

# a = input('Enter number: ')
#
#
# def sum_and_mult(_numbers):
#     _sum = sum(map(lambda i: int(i), list(_numbers)))
#     _mult = 1
#     for i in list(_numbers):
#         _mult *= int(i)
#     return _sum, _mult
#
# print(sum_and_mult(a))


def count_word_and_sentence(_string):
    print('Слов: ', len(_string.split()))
    print('Предложений: ', _string.count('.'))
count_word_and_sentence("Тестовое строка. В ней ровно десять слов и два предложения.")