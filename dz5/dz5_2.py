# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def is_simple_number(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False

    return num != 1

def get_multipliers_number(num: int):
    for i in range(1, num+1):
        modulo = num % i
        if modulo == 0 and is_simple_number(i):
            yield i


n = int(input('Введите число от 1 до 100: '))

multipliers = list(get_multipliers_number(n))

print(f'натуральные множители числа {n}: {multipliers}')