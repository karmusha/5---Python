# Пользователь вводит число от 1 до 999.
# Используя операции с числами, сообщите, что введено: цифра, двузначное или трёхзначное число.
# Для одной цифры верните её квадрат, например 5 - 25
# Для двузначного числа - произведение цифр, например 30 - 0
# Для трёхзначного числа - его зеркальное отображение, например, 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

def check_value():
    number = None
    while True:
        number = input('Введите число от 1 до 999: ')
        if number.isdecimal() and MIN_N < (res := int(number)) < MAX_N:
            return res
    print("Ошибка ввода числа")


MIN_N = 0
MAX_N = 1000
ONE_DIGIT = 10
TWO_DIGITS = 100

n = check_value()

result = 0
number_type = ''
while True:
    if n // ONE_DIGIT == 0:
        number_type = 'Цифра'
        result = n ** 2
    elif n // TWO_DIGITS == 0:
        number_type = 'Двузначное число'
        result = (n // ONE_DIGIT) * (n % ONE_DIGIT)
    else:
        number_type = 'Трёхзначное число'
        result = n % ONE_DIGIT * TWO_DIGITS + n // ONE_DIGIT % ONE_DIGIT * ONE_DIGIT + n // TWO_DIGITS
    break

print(number_type, result)
