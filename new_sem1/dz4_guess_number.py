# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRY_NUMBER = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print('Угадайте, какое число загадал Вася. У вас 10 попыток.')

count = 0
while count < TRY_NUMBER:
    count += 1
    number = int(input(f'Попытка номер {count}.\nВведите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    
    if number == num:
        print(f'Ура! Вы угадали, Вася загадал число {num}')
        exit()
    elif number < num:
        print('больше')
        continue
    elif number > num:
        print('меньше')
        continue
        
    if number < LOWER_LIMIT or number > UPPER_LIMIT:
        (f'Числа меньше {LOWER_LIMIT} и больше {UPPER_LIMIT} вводить нельзя.')
        continue
    break

print(f'Блин! Вася загадал число {num}, а Вы не угадали.')
