# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""


# Нужные библиотеки для изучерия, чтобы не изобретать колесо.
import multiprocessing
import itertools
import functools
import hashlib
import collections
import tqdm
import urllib
import furl
import pandas

mass = [1, 2, 3, 4, 5, 6, 7, 8, 9]
done = [x for x in mass if (not x % 3) | (x % 4 == 0)]

print(done)
