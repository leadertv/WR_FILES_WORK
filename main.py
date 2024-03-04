def parse_cook_book(filename):
    cook_book = {}

    with open(filename, 'r', encoding='utf8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            ingredient_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredient_count):
                ingredient_data = file.readline().strip().split(' | ')
                ingredient_name, quantity, measure = ingredient_data
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })

            cook_book[dish_name] = ingredients

            file.readline()

    return cook_book


# Считываем данные из файла и формируем словарь с рецептами
print("\n________\nВыводим рецепты из файла recipes.txt как словарь:\n")
cook_book = parse_cook_book('recipes.txt')


# Выводим результат
for dish, ingredients in cook_book.items():
    print(f"{dish}:")
    for ingredient in ingredients:
        print(ingredient)
    print()


def get_item_list_by_dishes(dishes, person_count, cook_book):
    item_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name not in item_list:
                    item_list[ingredient_name] = {'measure': ingredient['measure'],
                                                  'quantity': ingredient['quantity'] * person_count}
                else:
                    item_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count

    return item_list


# Для тестирования функции
# cook_book = {
#     'Омлет': [
#         {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт.'}
#     ],
#     'Утка по-пекински': [
#         {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт.'},
#         {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#         {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#         {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#     'Запеченный картофель': [
#         {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#         {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#         {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
#     ]
# }

# Применяем функцию
item_list = get_item_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 2, cook_book)

print("\n________\nВывод суммированных ингредиентов от количества персон:\n")
# Выводим полученный результат
for ingredient, quantity in item_list.items():
    print(f"{ingredient}: {quantity},")

print("\n________\nВывод в удобном формате:\n")
for ingredient, details in item_list.items():
    print(f"{ingredient}: {details['quantity']} {details['measure']},")
