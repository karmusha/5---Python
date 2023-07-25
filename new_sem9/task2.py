# Задание №2. Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint

def guess_number(func):
    start = 1
    stop_num = 100
    stop_try = 10
    def wrapper(num: int, try_num: int):
        if not start <= num <= stop_num:
            print('Вы ввели неверное число. Число от 1 до 100 будет сгенерировано автоматически.')
            num = randint(start, stop_num+1)
        if not start <= try_num <= stop_try:
            print('Вы ввели неверное число. Количество попыток будет от 1 до 10 будет сгенерировано автоматически.')
            try_num = randint(start, stop_try+1)
        res = func(num, try_num)
        return res
    return wrapper

if __name__ == '__main__':
    @guess_number
    def tries(num: int, try_num: int):
        print(f'Угадайте, какое число загадал Вася. У вас {try_num} попыток.')
        for i in range(1, try_num+1):
            choice = int(input('Input number: '))
            if choice == num:
                return f'Ура! Вы угадали c {i} попытки, Вася загадал число {num}.'
            else:
                continue
        return f'Блин! Вася загадал число {num}, а Вы не угадали.'


    number = int(input('Input the number to guess from 1 to 100: '))
    try_number = int(input('Input the number of tries from 1 to 10: '))
    res = tries(number, try_number)
    print(res)
