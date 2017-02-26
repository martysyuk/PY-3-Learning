# Домашнее задание третьего урока.
# Выполнил Мартысюк Илья, группа PY-3

warm_country_list = set()
sea_country_list = set()
visum_country_list = set()
budget_ok_country_list = set()

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
    if country_info['sea']:
        sea_country_list.add(country_name)
    if country_info['warm']:
        warm_country_list.add(country_name)
    if country_info['visum']:
        visum_country_list.add(country_name)
    if (budget / country_info['exRate']) >= (country_info['dayBill'] * trip_lenght):
        budget_ok_country_list.add(country_name)


def warm_and_sea_list():
    warm_and_sea = set()
    if len(sea_country_list) >= len(warm_country_list):
        for sea in sea_country_list:
            if (sea in warm_country_list) & (sea in budget_ok_country_list):
                warm_and_sea.add(sea)
    else:
        for warm in warm_country_list:
            if (warm in sea_country_list) & (warm in budget_ok_country_list):
                warm_and_sea.add(warm)

    return warm_and_sea


def visum_and_budget():
    vis_and_bud = set()
    if len(visum_country_list) >= len(budget_ok_country_list):
        for visum in visum_country_list:
            if visum in budget_ok_country_list:
                vis_and_bud.add(visum)
    else:
        for budget in budget_ok_country_list:
            if budget in warm_country_list:
                vis_and_bud.add(budget)

    return vis_and_bud



get_country_lists()

print('Теплые страны с морем: {}'.format(warm_and_sea_list()))
print('Страны находятся в Шенгене: {}'.format(visum_and_budget()))
