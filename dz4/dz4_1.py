# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# не использовать константу math.pi
import sys

eps: float = 0.000001

i: int = 1
x: float = sys.float_info.max
y: float = 0

while abs(x) >= eps:
    x = 1.0 / (2 * i - 1)
    y += x * (-1 if i % 2 == 0 else 1)

    i += 1

    if i % 100000 == 0:
        print(f'p = {4 * y}')

p = 4 * y
print(4 * y)