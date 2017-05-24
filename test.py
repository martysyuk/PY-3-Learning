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


_user_list = ['f', 'a', 'b', 'c']
_friends = ['b', 'a', 'd', 'e']

_result = list(set(_user_list) - set(_friends))

print(_result)
