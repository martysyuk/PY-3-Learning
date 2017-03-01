# Домашнее задание по уроку 2-1
# «Открытие и чтение файла, запись в файл»
# Выполнил Мартысюк Илья PY-3

cook_book = dict()
# 'Омлет': {
#     'name': 'Омлет',
#     'ingridients': [
#         {'product': 'Яйца', 'quantity': 2, 'unit': 'шт'},
#         {'product': 'Молоко', 'quantity': 50, 'unit': 'мл'},
#         {'product': 'Помидор', 'quantity': 100, 'unit': 'г'},
#     ]
# }


def cook_book_open():
    ingridients = list()
    with open('lesson2-1.txt', 'r', encoding='UTF8') as f:
        line = f.readline()
        while line:
            dish_name = line.rstrip()
            ingridients_count = int(f.readline())
            cook_book.update({dish_name: {'name': dish_name, 'ingridients': []}})

            for i in range(ingridients_count):
                ingridients.append(f.readline().rstrip().split(' | '))

            for i in range(ingridients_count):
                cook_book[dish_name]['ingridients'] += [{'product': ingridients[i][0],
                                                                   'quantity': int(ingridients[i][1]),
                                                                   'unit': ingridients[i][2]}]

            line = f.readline()
            ingridients = list()


def get_shop_list_by_dishes(dishes, people_count):
    shop_list = {}
    for dish in dishes:
         for ingridient in dish['ingridients']:
            new_shop_item = dict(ingridient)
            # пересчитали ингрединты по количеству людей
            new_shop_item['quantity'] = new_shop_item['quantity'] * people_count
            if new_shop_item['product'] not in shop_list:
                shop_list[new_shop_item['product']] = new_shop_item
            else:
                shop_list[new_shop_item['product']]['quantity'] += new_shop_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for key, shop_list_item in shop_list.items():
        print("{product} {quantity} {unit}".format(**shop_list_item))


def create_shop_list(people_count, first_dish, second_dish, third_dish):
    # получить блюда из кулинарной книги
    dish1 = cook_book[first_dish]
    dish2 = cook_book[second_dish]
    dish3 = cook_book[third_dish]
    dishes = [dish1, dish2, dish3]
    # заполнили список покупок
    shop_list = get_shop_list_by_dishes(dishes, people_count)
    # Вывести список покупок
    print_shop_list(shop_list)


print('Выберите первое блюдо: ')
first_dish = input()
print('Выберите второе блюдо: ')
second_dish = input()
print('Выберите третье блюдо: ')
third_dish = input()
print('На сколько человек?')
people_count = int(input())

cook_book_open()

print('\nСписок покупок: ')
create_shop_list(people_count, first_dish, second_dish, third_dish)
