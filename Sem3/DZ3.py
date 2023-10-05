# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

# stuff = {'matches': 1,
#          'cup': 2,
#          'tent': 10,
#          'ration': 5,
#          'spare shoes': 3}
# def backpack_capacity(capacity: int, stuff: dict) -> list[str]:
#     packaging_option = []
#     summary = []
#     for key, value in stuff.items():
#         if value <= capacity:
#             capacity -= value
#             packaging_option.append(key)
#     return packaging_option
# print(backpack_capacity(15, stuff))

data = {"Спички": 1,
        "Фонарик": 1,
        "Котелок": 1,
        "Аптечка": 2,
        "Консервы": 5,
        "Спальник": 3,
        "Вода": 3,
        "Палатка": 5
        }
all_size = float(input("Введите грузоподъёмность рюкзака : "))

print(f"Список (вещи : их вес) - {data}")

weight = 0
stock_lst =[]
for key, value in data.items():
    weight += value

if weight > all_size:
    size = all_size
    weight = 0
    for key, value in data.items():
        if value <= size:
            size -= value
            weight += value
            stock_lst.append(key)

    surplus = []
    for elem in data:
        if elem not in stock_lst:
            surplus.append(elem)
    print(f"Поместилось в рюкзак {stock_lst}, общий вес - {weight:.1f}. Не поместилось {surplus}")

else:
    print(f"Вместимость рюкзака ({all_size}) больше общего веса ({weight:.1f}). Ничего не осталось")