# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0


# original           -> 5x³ + x² - 13x + 53 = 0
# split_elements     -> '5x³',  '+x²',  '-13x',   '+53'

# element_to_tuple   -> ('5', '3'), ('1', '2'), ('-13', '1'), ('53', '0')
# parse_element      -> (5, 3), (1, 2), (-13, 1), (53, 0)

# parse_formula      -> (5, 3), (1, 2), (-13, 1), (53, 0)

from dz4_common import *
from itertools import groupby
from pathlib import Path


def parse_file_to_formulas(file_path: str):
    with open(file_path, mode='r', encoding='utf-8') as f: # Открываем файл на чтение
        for line in f:
            line = line.strip() # Удаляем пробелы из строки
            print('read: ' + line)

            if line in ['', '\n', '\r', '\t', None]: # Пропускаем пустые и всякие дурацкие строки
                continue
            
            res = split_elements(line) # Разбиваем многочлен на отдельные элементы
            res = filter(empty_filtration, res) # На всякий случай пропускаем пустые строки и элементы
            res = map(element_to_tuple, res) # Возвращаем кортеж из коэффециента и степени (в виде строки)
            res = map(parse_element, res) # # Возвращаем кортеж из коэффециента и степени (в виде интовых значений)
            
            yield res

def concat_formulas(*iterables):
    for x in iterables:
        for y in x:
            yield y

def sum_coef_by_degree(res):
    def group_key(x):
        return x[0]

    def sum_by_key(x):
        return (
            sum(y[1] for y in x[1]),
            x[0],
        )

    res = sorted(res, key=group_key, reverse=True)      # сортирую элементы по степени
    res = groupby(res, key=group_key)                   # группируем элементы по степени для суммирования коэффициентов
    res = map(sum_by_key, res)                          # суммирую коэффициенты

    return res                                          # (degree, coefficient), (.., ..), ..


def formula_to_str(res):
    res = filter(filter_zero_coefficient, res)
    res = enumerate(res)
    res = map(map_x, res)
    res = map(map_coefficient, res)
    res = map(map_sign, res)
    res = map(map_str, res)
    res = ' '.join(res) + ' = 0'

    return res

# ----------------------------------------

folder = Path(__file__).parent
file1 = folder.joinpath('dz4_5_1.txt')
file2 = folder.joinpath('dz4_5_2.txt')

res = concat_formulas(                      # объединяю все формулы в одну
    *parse_file_to_formulas(file1),
    *parse_file_to_formulas(file2)
)
res = sum_coef_by_degree(res)               # суммирую коэффициенты с одинаковыми степенями
res = formula_to_str(res)                   # формирую формулу в виде строки

print('-----------')
print('sum: ' + res)

file_res = folder.joinpath('dz4_5_res.txt')
with open(file_res, mode='w', encoding='utf-8') as f:
    f.write(res)


