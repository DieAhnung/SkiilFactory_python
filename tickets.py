price = 0
discount = 10
number_of_tickets = int(input("Введите количество билетов: "))
for i in range(int(number_of_tickets)):
    age = int(input("Введите возраст: "))
    if age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    elif age > 25:
        price += 1390
print("Итоговая стоимость билетов (без учета скидки): ", price)
if number_of_tickets > 3:
    price = price-(price*discount/100)
print("общая стоимость покупки: ", int(price))
