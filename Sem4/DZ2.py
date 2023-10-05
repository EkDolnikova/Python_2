# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}

import collections.abc

def reverse_items(**kwargs):
    res_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, collections.abc.Hashable):
            res_dict[value] = key
        else:
            res_dict[str(value)] = key
    return res_dict


rev_dict = reverse_items(join=25, Hello=2.4, Str='world', lst=[1, 2, 3], set_item={1,2,7,9, 'list'})
print(rev_dict)