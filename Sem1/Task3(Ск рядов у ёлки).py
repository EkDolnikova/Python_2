# Нарисовать в консоли ёлку спросив у пользователя количество рядов. Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

rows = int(input("Введите число строк :"))
STAR = "*"
SPACE = " "
count_spaces = rows - 1
cout_star = 1
for row in range(rows):
    print(SPACE * count_spaces + STAR * cout_star)
    count_spaces -= 1
    cout_star += 2
