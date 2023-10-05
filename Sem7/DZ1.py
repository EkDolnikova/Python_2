# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

from pathlib import Path


def group_renaming(
        final_name: str = "_test",
        number_of_digits: int = 2,
        original_extension: str = "txt",
        final_extension: str = "tst",
        scope: tuple = (0, None)
):
    p = Path(Path().cwd())
    count = 0
    for obj in p.iterdir():
        if obj.is_file():
            new_file = ""
            _name, _ext = obj.name.split('.')
            if _ext == original_extension:
                count += 1
                new_file = ''.join([
                    _name[scope[0]:scope[1]],
                    final_name,
                    str(count).rjust(number_of_digits, "0"),
                    '.',
                    final_extension
                ])
                # print(new_file)
                obj.rename(new_file)


if __name__ == '__main__':
    group_renaming(number_of_digits=4, scope=(0, 3))

import os
from os import listdir, rename, path, getcwd

#
# def group_rename_files(dest_name, num_digits, src_ext, dest_ext, name_range=None):
#     # Получаем список файлов в текущем каталоге
#     files = os.listdir()
#     # Фильтруем только файлы с нужным расширением
#     files = [f for f in files if os.path.isfile(f) and f.endswith(src_ext)]
#
#     # Проверяем, есть ли диапазон сохраняемого оригинального имени
#     if name_range:
#         files = [f[name_range[0] - 1:name_range[1]] for f in files]
#
#     # Создаем счетчик для порядкового номера
#     count = 1
#
#     # Переименовываем каждый файл
#     for file in files:
#         # Генерируем новое имя файла
#         new_file_name = dest_name + str(count).zfill(num_digits) + dest_ext
#         # Переименовываем файл
#         os.rename(file, new_file_name)
#         count += 1
#
#
# group_rename_files("new_file_", 4, ".txt", ".jpg", [3, 6])



# __all__ = ['group_rename']
#
# def group_rename(begin_extention, final_extention, range_of_begin_sym=[0, 0], final_name="", len_count=2):
#     count = 1
#     for file in listdir(getcwd()):
#         if path.isfile(file) and file.split(".")[-1] == begin_extention:
#             old_chars = ""
#             max_limit = min(max(range_of_begin_sym), len(file.split(".")[0]))
#             min_limit = min(range_of_begin_sym)
#             if min_limit >= max_limit:
#                 min_limit = max_limit
#             elif min_limit < 0:
#                 min_limit = 0
#             for i in range(min_limit, max_limit):
#                 old_chars = old_chars+file[i]
#             len_zero = max(0, len_count - len(str(count)))
#             new_name = old_chars + final_name + len_zero * \
#                 "0" + str(count) + "." + final_extention
#             rename(file, new_name)
#             count += 1
#
#
# if __name__ == "__main__":
#     group_rename("txt", "csv", [200, 100], "final")