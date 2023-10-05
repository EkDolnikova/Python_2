# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой
# строки отсортированный по убыванию.

def text_ord(n:str)->list[int]:
    d = set()
    for el in n:
        d.add(ord(el))
    return sorted(list(d), reverse=True)

n = input()
print(text_ord(n))