# Создайте генератор чётных чисел от нуля до 100.
# Из последовательности исключите числа, сумма цифр которых равна 8.
# Решение в одну строку.

# res = [i for i in range(0, 101) if i % 2 == 0 and (i // 10 + i % 10 != 0)]
res = [i for i in range(0, 101)
       if i % 2 == 0
            and sum(map(int, list(str(i)))) !=8]

# res = [i for i in range(0, 101, 2) if sum(map(int, list(str(i)))) !=8]
print(res)


