# Домашнее задание второго урока.
# Выполнил Мартысюк Илья, группа PY-3

# Сбор данных о заказах
orders = []
names = []
amount = []
budget = float(input('Введите Ваш общий бюджет: '))
while True:
    orderName = input('Введите название: ')
    orderSum = float(input('Введите стоимость: '))
    amtOrders = float(input('Введите количество: '))
    orders.append(orderSum)
    names.append(orderName)
    amount.append(amtOrders)
    addMore = input('Добавить еще один заказ (y/n)?: ')
    if addMore == 'y' or addMore == 'Y':
        continue
    else:
        break

# Подсчет налогов

totalOrderTaxes = 0
totalOrderCost = 0

print('\nТраты с налогами:')
print('Название | Сумма | Налог | Кол-во ')
for order, name, amt in zip(orders, names, amount):
    if name == 'Iphone':
        tax = 0.10
    elif name == 'Еда':
        tax = 0.02
    elif name == 'Медикаменты':
        tax = 0.0
    else:
        tax = 0.04

    orderTax = order * tax
    totalOrderTaxes += orderTax * amt
    totalOrderCost += order * amt

    print(name, ' | ', order, '$ |', orderTax, '$ |', amt)

print('\nОбщая стоимсоть товаров {}$'.format(totalOrderCost))
print('Общая сумма налогов {}$'.format(totalOrderTaxes))
print('Общая сумма заказа с налогами {}$'.format(totalOrderCost + totalOrderTaxes))

# Вывод списка дорогих покупок

print('\nСписок покупок дороже 50$')
for i in range(len(orders)):
    if orders[i] > 50:
        print(names[i], ' - ', orders[i], '$')

# Проверка перерасхода бюджета
if totalOrderCost > budget:
    print('Мы вышли за рамки бюджета на ', totalOrderCost - budget, '$')
