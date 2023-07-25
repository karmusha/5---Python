# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# - декораторами для сохранения параметров,
# - декоратором контроля значений и
# - декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from task2 import guess_number
from task3 import deco
from task4 import count

@count(2)
@guess_number
@deco
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
