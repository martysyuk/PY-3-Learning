# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

import osa
import re


def temp_convert(file_path, to_unit):
    temp_case = {'C': 'degreeCelsius',
                 'F': 'degreeFahrenheit',
                 'Ra': 'degreeRankine',
                 'Re': 'degreeReaumur',
                 'K': 'kelvin'
                 }
    url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.Client(url)
    try:
        with open(file_path, 'r') as file:
            line = file.readline()
            while line:
                temp = ''.join(re.findall(r'\d+', line))
                temp_format = ''.join(re.compile('[^a-zA-Z ]').sub('', line).split())
                try:
                    from_unit = temp_case[temp_format]
                    to_unit_convert = temp_case[to_unit]
                    response = client.service.ConvertTemp(Temperature=temp, FromUnit=from_unit,
                                                          ToUnit=to_unit_convert)
                    print('{}{} = {}C'.format(temp, temp_format, round(response)))
                except KeyError:
                    print('Неизвестный формат температуры')
                line = file.readline()
    except FileNotFoundError:
        print('Файл не найден')

temp_convert('temps.txt', 'C')
