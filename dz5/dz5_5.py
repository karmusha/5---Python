# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0


# original           -> 5x³ + x² - 13x + 53 = 0
# split_elements     -> '5x³',  '+x²',  '-13x',   '+53'
# parse_element      -> (5, 3), (1, 2), (-13, 1), (53, 0)

from itertools import chain
from dz5_common import *

def parse_formula(file_path: str):
    with open(file_path, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
        
            if line in ['', '\n', '\r', '\t', None]:
                continue
            
            res = split_elements(line)
            res = filter(empty_filtration, res)
            res = map(element_to_tuple, res)
            res = map(parse_element, res)
            res = filter(filter_zero_coefficient, res)

            return res

def formula_sum(formula: tuple[int, int]):
    pass

def formula_to_str(res):
    res = enumerate(res)
    res = map(map_x, res)
    res = map(map_coefficient, res)
    res = map(map_sign, res)
    res = ' '.join(res) + ' = 0'

    return res

res_1 = parse_formula('dz5_5_1.txt')
res_2 = parse_formula('dz5_5_2.txt')
res = chain(res_1, res_2)
res = formula_sum(res)

print(res)

formula_to_file_write = formula_to_str(res)

with open('dz5_5.txt', mode='w', encoding='utf-8') as f:
    f.write(formula_to_file_write)



with open('dz5_5_1.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()

        if line in ['', '\n', '\r', '\t', None]:
            continue
    
        res1 = split_elements(line)
        res1 = filter(empty_filtration, res1)
        res1 = map(element_to_tuple, res1)
        res1 = map(parse_element, res1)
        res1 = filter(filter_zero_coefficient, res1)
        res1 = enumerate(res1)
        res1 = map(map_x, res1)
        res1 = map(map_coefficient, res1)
        res1 = map(map_sign, res1)
        res1 = map(map_str, res1)
        res1_line = zip()
        res1_print = ' '.join(res1) + ' = 0'
