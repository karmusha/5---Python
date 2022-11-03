# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import Random
from dz5_common import *

def get_formula_elements(k: int):
    rand = Random()
    for i in reversed(range(0, k+1)):
        coefficient: float = rand.randint(-100, 100)
        yield (coefficient, i)

def get_demo_elements():
    yield (0, 5)
    yield (0, -1)
    yield (25, -4)
    yield (1, 3)
    yield (-84, 2)
    yield (0, 1)
    yield (25, 0)

# get_elements()          -> (0, 5), (25, 4),             (-1, 3)
# filter_zero_coefficient ->         (25, 4),             (-1, 3)
# enumerate               ->         (0, (25, 4)),        (1, (-1, 3))
# map_x                   ->         (0, 25, 4, 'x^4'),   (1, -1, 3, 'x^3')
# map_coefficient         ->         (0, 25, 4, '25x^4'), (1, -1, 3, 'x^3')
# map_sign                ->         (0, 25, 4, '25x^4'), (1, -1, 3, '- x^3')
# map_str                 ->         '25x^4'            ,            '- x^3'
# join                    ->         '25x^4 - x^3 = 0'

k = int(input("Введите коэффициент: "))

# res = get_demo_elements()
res = get_formula_elements(k)
res = filter(filter_zero_coefficient, res)
res = enumerate(res)
res = map(map_x, res)
res = map(map_coefficient, res)
res = map(map_sign, res)
res = map(map_str, res)
res = ' '.join(res) + ' = 0'

print(res)