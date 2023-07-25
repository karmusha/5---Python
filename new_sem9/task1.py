# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания, ○от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число
# за указанное число попыток.

def guess_number(number: int, try_number: int):
    print(f'Угадайте, какое число загадал Вася. У вас {try_number} попыток.')

    def tries():
        for i in range(1, try_number+1):
            choice = int(input('Input number: '))
            if choice == number:
                return f'Ура! Вы угадали c {i} попытки, Вася загадал число {number}.'
            else:
                continue
        return f'Блин! Вася загадал число {number}, а Вы не угадали.'
    return tries

num = int(input('Input the number to guess from 1 to 100: '))
num_try = int(input('Input the number of tries from 1 to 10: '))
res = guess_number(num, num_try)
print(res())
