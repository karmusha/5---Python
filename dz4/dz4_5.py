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
from collections import Counter

def parse_formula(file_path: str):
    with open(file_path, mode='r', encoding='utf-8') as f: # Открываем файл на чтение
        for line in f:
            line = line.strip() # Удаляем пробелы из строки
        
            if line in ['', '\n', '\r', '\t', None]: # Пропускаем пустые и всякие дурацкие строки
                continue
            
            res = split_elements(line) # Разбиваем многочлен на отдельные элементы
            res = filter(empty_filtration, res) # На всякий случай пропускаем пустые строки и элементы
            res = map(element_to_tuple, res) # Возвращаем кортеж из коэффециента и степени (в виде строки)
            res = map(parse_element, res) # # Возвращаем кортеж из коэффециента и степени (в виде интовых значений)
            # res = filter(filter_zero_coefficient, res) #Убираем пустые и none значения

            return res

def formula_to_str(res):
    res = enumerate(res)
    res = map(map_x, res)
    res = map(map_coefficient, res)
    res = map(map_sign, res)
    res = ' '.join(res) + ' = 0'

    return res

def formula_sum(res_1, res_2):
    res = {}
    for k1, v1 in res_1:
        for k2, v2 in res_2:
            if k1 == k2:
                res = k1, v1 + v2
    yield res


res_1 = parse_formula('dz4_5_1.txt')
res_2 = parse_formula('dz4_5_2.txt')
# res = chain(res_1, res_2)s
res_1 = dict(res_1)
res_2 = dict(res_2)
# res = enumerate(formula_sum(res_1, res_2))

res_1 |= res_2                                          #  результирующий словарь

def sum_dict(dictionary):
    for dictionary in resultdict:                                     # пробегаем по списку словарей
        for key in dictionary:                               # пробегаем по ключам словаря
            try:
                resultdict[key] += dictionary[key]        # складываем значения
            except KeyError:                                    # если ключа еще нет - создаем
                resultdict[key] = dictionary[key]
    return resultdict   
print(sum_dict(res_1))

# a = (
#     {'Петя': 6, 'Вася': 8, 'Дима': 11, 'Юля': 3}, 
#     {'Петя': 5, 'Вася': 36, 'Дима': 4, 'Юля': 8}, 
#     {'Петя': 54, 'Вася': 21, 'Дима': 22, 'Юля': 39}, 
#     {'Петя': 61, 'Вася': 48, 'Дима': 71, 'Юля': 73})
# c = Counter().fromkeys()
# for d in res_1:
#     c.update(d)

# ----------------------------------------
# formula_to_file_write = formula_to_str(res)

# with open('dz4_5.txt', mode='w', encoding='utf-8') as f:
#     f.write(formula_to_file_write)



# with open('dz4_5_1.txt', mode='r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip()

#         if line in ['', '\n', '\r', '\t', None]:
#             continue
    
#         res1 = split_elements(line)
#         res1 = filter(empty_filtration, res1)
#         res1 = map(element_to_tuple, res1)
#         res1 = map(parse_element, res1)
#         res1 = filter(filter_zero_coefficient, res1)
#         res1 = enumerate(res1)
#         res1 = map(map_x, res1)
#         res1 = map(map_coefficient, res1)
#         res1 = map(map_sign, res1)
#         res1 = map(map_str, res1)
#         res1_line = zip()
#         res1_print = ' '.join(res1) + ' = 0'
