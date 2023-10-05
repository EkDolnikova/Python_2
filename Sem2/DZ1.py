# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

decimal_number = int(input("Введите число в десятичной системе: "))
hexadecimal_digits = "0123456789ABCDEF"  # Строка с шестнадцатеричными цифрами
hexadecimal_number = ""

while decimal_number > 0:
    remainder = decimal_number % 16  # Получаем остаток от деления на 16
    hexadecimal_digit = hexadecimal_digits[remainder]  # Получаем шестнадцатеричную цифру
    hexadecimal_number = hexadecimal_digit + hexadecimal_number  # Добавляем цифру в начало шестнадцатеричного числа
    decimal_number //= 16  # Выполняем целочисленное деление на 16

print("Шестнадцатеричное число:", hexadecimal_number)

# Использование встроенной функции:
number = 245
print(f'Встроенная функция hex -> \t\t{hex(number)}')

