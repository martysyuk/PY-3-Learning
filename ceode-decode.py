# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

# Кодирование MD5, лучший способ шифрования на сегодня sha512

import hashlib

code = hashlib.md5(b'Hello World!')
print(code.hexdigest())

input_code = input('Введи строку для кодирования: ')
decode = hashlib.md5(input_code.encode())
print(decode.hexdigest())


# Кодирование и декодирование в другие кодировки и бинарную строку
s = 'Привет!'
s1 = s.encode('utf-8')
print(s1)

s2 = s1.decode('utf-8')
print(s2)
