# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точнсть вычислений должна составлять не менее 42 знаков после запятой.

from decimal import Decimal, getcontext
import math
 
getcontext().prec = 50

D = int(input('Add number: '))

S = Decimal(math.pi * ((D ** 2)/4))
L = Decimal(math.pi * D)

print(f'Square of the circle = {S}')
print(f'Length of circumference of a circle = {L}')
