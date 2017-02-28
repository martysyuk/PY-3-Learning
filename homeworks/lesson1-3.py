# Домашнее задание третьего урока.
# Выполнил Мартысюк Илья, группа PY-3

sea_and_warm_countries = set()
visa_countries = set()
budget_ok_countries = set()

countries = {
  'Thailand': {'sea': True,
               'visum': False,
               'warm': True,
               'dayBill': 10,
               'exRate': 2},
  'Germany':  {'sea': False,
               'visum': True,
               'warm': False,
               'dayBill': 100,
               'exRate': 65},
  'England':  {'sea': True,
               'visum': True,
               'warm': False,
               'dayBill': 100,
               'exRate': 100},
  'Poland':   {'sea': False,
               'visum': True,
               'warm': False,
               'dayBill': 100,
               'exRate': 30},
  'Greece':   {'sea': True,
               'visum': False,
               'warm': True,
               'dayBill': 100,
               'exRate': 50},
  'Franca':   {'sea': True,
               'visum': True,
               'warm': True,
               'dayBill': 100,
               'exRate': 65},
  'China':    {'sea': False,
               'visum': True,
               'warm': True,
               'dayBill': 500,
               'exRate': 6}
  }

budget = float(input('Введите Ваш бюджет на путешествие: '))
trip_lenght = int(input('Введите продолжительность путешествия (дней): '))


def get_country_lists():
  for country_name, country_info in countries.items():
    if country_info['sea'] & country_info['warm']:
        sea_and_warm_countries.add(country_name)
    if country_info['visum']:
        visa_countries.add(country_name)
    if (budget / country_info['exRate']) >= (country_info['dayBill'] * trip_lenght):
        budget_ok_countries.add(country_name)


get_country_lists()
done_list = ((sea_and_warm_countries | visa_countries) & budget_ok_countries)

print('По Вашим критериям подходят: {}'.format(done_list))
