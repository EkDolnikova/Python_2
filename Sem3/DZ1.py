# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]

my_list = [1, 1, 2, "a", "a", 2, 2, 3, 3, 3, 3, 4, 4, 5, 6]
new_list = []
for el in my_list:
    count_el = my_list.count(el)
    if count_el > 1 and el not in new_list:
        new_list.append(el)
print(my_list)
print(new_list)