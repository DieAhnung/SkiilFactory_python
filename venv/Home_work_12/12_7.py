money = int(input("Введите сумму: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = per_cent.items()

for key, value in per_cent.items():

    deposit = round((value * money) / 100)

    print(deposit)

# m_dep = max(deposit)
# print("Максимальная сумма, которую вы можете заработать" + m_dep )

