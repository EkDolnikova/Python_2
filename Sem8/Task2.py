# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import  json
test = {
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
}
def data(name:str, id:int, lewel:int, file_name):
      try:
          with open(file_name, "r", encoding="utf-8") as f:
              users = json.load(f)
      except FileExistsError:
          users = {1: {},2: {},3: {}, 4: {},5: {},6: {},}
          users[lewel][id] = name
          with open(file_name, "w", encoding="utf-8") as f:
              json.dump(users, f, ensure_ascii=False)

def request(file_name):
    while True:
        name = input("Введите имя:")
        id = input("Введите id:")
        lewel = input("Введите уровень:")
        data(name, id, lewel, file_name)

request("users_new")


