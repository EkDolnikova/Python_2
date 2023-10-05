# Функция принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def mu_f(names: [str], salarys: [int], bonuses: [str]) -> dict[str, float | int]:
    result = {}
    for name, salary, bonus in zip(names, salarys, bonuses):
        result[name] = salary + salary * (float(bonus[:-1]) / 100)
    return result


n = ["Иван", "Николай", "Пётр", "Харитон"]
s = [125_000, 96_000, 109_000, 100_000]
a = ['10%', '25.5%', '13.3%', '42.73%']
print(mu_f(n, s, a))
