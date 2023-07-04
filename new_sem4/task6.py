# Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину, а если хотя бы одна убыточная, - ложь.

companies = {'Nokia': [100, 500, -700, -1000, -200],
             'Lowa': [800, 100, -50, -150, 20],
             'Ararat': [-800, 100, 500, 2000],
             }


def has_profit(companies_dict):
    # return all(sum(value) > 0 for value in companies_dict.values())
    return all(map(lambda value: sum(value) > 0, companies_dict.values()))
    

print(has_profit(companies))
