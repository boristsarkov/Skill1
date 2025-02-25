
import json

with open("orders_july_2023.json", "r") as my_file:
    translator = json.load(my_file)
max_price = 0
max_order = ''
# цикл по заказам
print('1. Какой номер самого дорого заказа за июль?')
for order_num, orders_data in translator.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price} рублей')

print()
print('2. Какой номер заказа с самым большим количеством товаров?')
max_order = ''
max_quantity = 0
for order_num, orders_data in translator.items():
    quantuty = orders_data['quantity']

    if quantuty > max_quantity:
        max_order = order_num
        max_quantity = quantuty

for orders, orders_data in translator.items():
    if orders_data['quantity'] == max_quantity:
        print(f'Заказ с номером {orders} имеет самое большое количество заказов = {max_quantity}')

print()
print('3. В какой день в июле было сделано больше всего заказов?')

max_order = ''
max_quantity = 0
date_set = set()
for order_num, orders_data in translator.items():
    quantuty = orders_data['quantity']

    if quantuty > max_quantity:
        max_order = order_num
        max_quantity = quantuty
for orders, orders_data in translator.items():
    if orders_data['quantity'] == max_quantity:
        date_set.add(orders_data['date'])
sorted_date_set = sorted(date_set)
for dates in sorted_date_set:
    print(f'В дату {dates} совершено самое большое количество заказов')

print()
print('4. Какой пользователь сделал самое большое количество заказов за июль?')
max_order = ''
max_quantity = 0
user_id_set = set()
for order_num, orders_data in translator.items():
    quantuty = orders_data['quantity']
    if quantuty > max_quantity:
        max_order = order_num
        max_quantity = quantuty
for orders, orders_data in translator.items():
    if orders_data['quantity'] == max_quantity:
        user_id_set.add(orders_data['user_id'])
for user_ides in user_id_set:
    print(f'Пользователь {user_ides} совершил самое большое количество заказов за июль')

print()
print('5. У какого пользователя самая большая суммарная стоимость заказов за июль?')
max_order = ''
max_quantity = 0
summ_price = []
sum_orders = 0
max_price = 0
for order_num, orders_data in translator.items():
    quantuty = orders_data['quantity']
    price = orders_data['price']
    summ_orders = quantuty * price
    summ_price.append(summ_orders)
    max_price = max(summ_price)

print(f'У пользователя ID №{orders_data["user_id"]} самая максимальная сумарная стоимость заказов')

print()
print('6. Какая средняя стоимость заказа была в июле?')
middle_price = 0
empty_price_list = []
for orders_data in translator.values():
    empty_price_list.append(orders_data['price'])
middle_price = sum(empty_price_list) / len(empty_price_list)
print(f'Средняя стоимость товаров в июле = {middle_price:.2f} рублей')

print()
print('7. Какая средняя стоимость заказа в июле?')

empty_quantity_list = []
empty_price_list = []
middle_price = 0
for orders_data in translator.values():
    empty_price_list.append(orders_data['price'])
    empty_quantity_list.append(orders_data['quantity'])
middle_price = sum(empty_price_list) / sum(empty_quantity_list)
print(f'Средняя стоимость товаров в июле = {middle_price:.2f} рублей')


