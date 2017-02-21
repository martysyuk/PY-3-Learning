# Домашнее задание по первому уроку (с корректировками).
# Выполнил Мартысюк Илья, группа PY-3

print('Калькулятор Шенгенской визы\n')

euro = 65
print('Курс на сегодня: ', euro, ' рублей за 1€')

haveMoney = float(input('Ваш бюджет (€):'))
flyCost = float(input('Стоимость перелета (€)'))
tripLenght = float(input('Дительность поездки:'))

tripDailyСosts = []

dayMoney = (haveMoney - flyCost) / tripLenght
dayMoneyRub = dayMoney * euro

print('Ваш бюджет на день составляет ', dayMoney,
      ' € (', dayMoneyRub, ' рублей).')

totalMoney = haveMoney - flyCost
i = 0
while i < tripLenght:
  loseMoneyToday = float(input('\nСколько Вы потратили в ' +
                                str(i) + ' день (€): '))
  tripDailyСosts.append(loseMoneyToday)
  totalMoney = totalMoney - loseMoneyToday
  totalMoneyRub = totalMoney * euro
  i = i + 1
  if loseMoneyToday > dayMoney:
    print('\n!!! ВНИМАНИЕ !!! Вы перерасходовали дневной бюджет.')

  if totalMoney >= 0:
    print('\nУ Вас осталось ', totalMoney, '€ (', totalMoneyRub, 'р.).')
  else:
    print('Вы перерасходовали бюджет на ', abs(totalMoney),
          '€ (', abs(totalMoneyRub), 'р.)')

print('\nВаши расходы за все путешествие составили:')

i = 0
totalTripCost = 0
while i < tripLenght:
  print('День ' + str(i+1) + ': ' + str(tripDailyСosts[i]) + '€ (' +
        str(tripDailyСosts[i] * euro) + 'р.)')
  totalTripCost = totalTripCost + tripDailyСosts[i]
  i = i + 1

print('Итого Вами потрачено: ' + str(totalTripCost) + '€ (' +
      str(totalTripCost * euro) + 'р.)')
