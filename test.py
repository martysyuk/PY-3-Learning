# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

a = [x**3 for x in mass if (x % 3 == 0) & (x % 4 == 0)]

print(a)