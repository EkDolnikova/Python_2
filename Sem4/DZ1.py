# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transpose_(lst: list) -> list:
    return [list(lst) for lst in zip(*lst)]


matrix = [[1, 2, 3, 20],
          [4, 5, 6, 21],
          [7, 8, 9, 22]]

new_matrix = transpose_(matrix)

print(*matrix, sep= '\n')
print()
print(*new_matrix, sep= '\n')