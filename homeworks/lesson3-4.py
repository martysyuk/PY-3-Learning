# -*- coding: UTF-8 -*-
"""
Authon: Martysyuk Ilya
E-Mail: martysyuk@gmail.com
"""

import osa
import re


def load_data(file_path):
    return_data = list()
    try:
        with open(file_path, 'r') as file:
            print('Читаем данные из файла {}'.format(file_path))
            line = file.readline()
            while line:
                return_data.append(line.split())
                line = file.readline()
        return return_data
    except FileNotFoundError:
        print('Файл {} не найден!'.format(file_path))
        return None


def temp_convert(file_path, to_unit):
    temp_case = {'C': 'degreeCelsius',
                 'F': 'degreeFahrenheit',
                 'Ra': 'degreeRankine',
                 'Re': 'degreeReaumur',
                 'K': 'kelvin'
                 }
    url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.Client(url)
    average_temp = 0
    data = load_data(file_path)
    for convert in data:
        try:
            from_unit = temp_case[convert[1]]
            to_unit_convert = temp_case[to_unit]
            response = client.service.ConvertTemp(Temperature=convert[0], FromUnit=from_unit, ToUnit=to_unit_convert)
            average_temp += round(response)
        except KeyError:
            print('Неизвестный формат температуры')
    return round(average_temp / len(data))


def trip_lenght(file_path, to_unit):
    metric_case = {'as': 'Angstroms',
                   'nm': 'Nanometers',
                   'min': 'Microinch',
                   'Mc': 'Microns',
                   'ml': 'Mils',
                   'mm': 'Millimeters',
                   'cm': 'Centimeters',
                   'in': 'Inches',
                   'li': 'Links',
                   'sp': 'Spans',
                   'ft': 'Feet',
                   'c': 'Cubits',
                   'v': 'Varas',
                   'y': 'Yards',
                   'm': 'Meters',
                   'fms': 'Fathoms',
                   'r': 'Rods',
                   'ch': 'Chains',
                   'fl': 'Furlongs',
                   'cl': 'Cablelengths',
                   'km': 'Kilometers',
                   'mi': 'Miles',
                   'ncm': 'Nauticalmile',
                   'l': 'League',
                   'ncl': 'Nauticalleague'
                   }
    url = 'http://www.webservicex.net/length.asmx?WSDL'
    client = osa.Client(url)
    data = load_data(file_path)
    summa = 0
    for convert in data:
        try:
            metric = float(convert[1].replace(',', ''))
            from_unit = metric_case[convert[2]]
            to_unit_convert = metric_case[to_unit]
            response = client.service.ChangeLengthUnit(LengthValue=metric, fromLengthUnit=from_unit,
                                                       toLengthUnit=to_unit_convert)
            summa += round(response)
        except KeyError:
            print('Неизвестный формат температуры')
    return str(summa) + to_unit


print('Средняя температура {} градусов цельсия\n'.format(temp_convert('temps.txt', 'C')))
print('Суммарное растояние путешествия {}\n'.format(trip_lenght('travel.txt', 'km')))
