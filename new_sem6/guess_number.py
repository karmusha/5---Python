#  Module 'guess_number'

from random import randint

def guess_number(start, end, tries):
    num = randint(start, end)

    print(f'Угадайте, какое число загадал Вася. У вас {tries} попыток.')

    for i in range(0, tries):
        number = int(input(f'Попытка номер {i+1}.\nВведите число от {start} до {end}: '))
        if number < start or number > end:
            print(f'Вы ввели неверное число. Введите число от {start} до {end}.')
        elif number == num:
            print(f'Ура! Вы угадали, Вася загадал число {num}')
            return True
        elif number < num:
            print('больше')
            continue
        elif number > num:
            print('меньше')
            continue
        
    print(f'Блин! Вася загадал число {num}, а Вы не угадали.')
    return False




if __name__ == '__main__':
    guess_number(1, 10, 5)