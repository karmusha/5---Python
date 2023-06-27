# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
# дробь делимое делитель частное = fraction dividend divisor quotient

from fractions import Fraction
import math
from typing import List


def check_value() -> List[int]:
    def check_dev(num): # Проверка на наличие /
        for i in num:
            if i == '/':
                return True
        return False

    while True:
        try:
            number: str = input('Введите дробь, например 2/5: ') # Вводим строку
            if check_dev(number): # Если эта строка содержит /
                res = number.split('/') # Парсим строку на список 2х чисел
                res = [eval(i) for i in res]
            else:
                print('Введите дробь заданного формата.')
                continue
        except ValueError:
            print('Это не число.')
            continue
        break
    return res

def reduce_fraction(a, b):
    return a // math.gcd(a, b), b // math.gcd(a, b)

def sum_fractions(fraction1, fraction2) -> List[int]:
    f1_with_common_divisor = [fraction1[0] * fraction2[1], fraction1[1] * fraction2[1]]
    f2_with_common_divisor = [fraction2[0] * fraction1[1], fraction2[1] * fraction1[1]]
    res = [f1_with_common_divisor[0] + f2_with_common_divisor[0], f1_with_common_divisor[1]]
    res = list(reduce_fraction(res[0], res[1]))
    return res

def multiply_fractions(fraction1, fraction2) -> List[int]:
    res = [fraction1[0] * fraction2[0], fraction1[1] * fraction2[1]]
    res = list(reduce_fraction(res[0], res[1]))
    return res

    
fraction1: List[int] = check_value()
fraction2: List[int] = check_value()

sum_result = '/'.join(map(str, sum_fractions(fraction1, fraction2)))
multiply_result = '/'.join(map(str,multiply_fractions(fraction1, fraction2)))

print(f'{sum_result} = {Fraction(fraction1[0], fraction1[1]) + Fraction(fraction2[0], fraction2[1])}')
print(f'{multiply_result} = {Fraction(fraction1[0], fraction1[1]) * Fraction(fraction2[0], fraction2[1])}')
