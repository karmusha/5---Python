# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


def get_none_repeated_elements(num: str):
    count_elements: dict[str, int] = {}

    for n in num:
        count = count_elements.get(n, 0)
        count += 1
        count_elements.update({n: count})

    return [val for val, count in count_elements.items() if count == 1]

n = input('Введите последовательность цифр одним числом: ')

none_repeated_elements = get_none_repeated_elements(n)


print(f'Список неповторяющихся значений в {n}: {none_repeated_elements}')