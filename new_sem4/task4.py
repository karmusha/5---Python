# Функция принимает на вход три списка одинаковой длины:
# - имена str
# - ставка int
# - премия str с указанием процентов вида "10.25%"
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

people = ['Ira', 'Elena', 'Petr']
rate = [100_000, 110_000, 150_000]
bonus = ['10.25%', '12.5%', '5%']


def get_bonus(people, rate, bonus) -> dict:
    # bonus_as_float = list(map(lambda x: float(x.replace('%', '')), bonus))
    return {name: base / 100 * float(comission[:-1]) for name, base, comission in zip(people, rate, bonus)}
    

print(get_bonus(people, rate, bonus))
