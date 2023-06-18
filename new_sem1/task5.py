# Нарисовать в консоли ёлочку, спросив у пользователя количество рядов
#     *    4/1
#    ***   3/1+2
#   *****  2/3+2
#  ******* 1/5+2
# *********0/7+2

from colorama import Fore

rows = int(input('Введите количество рядов: '))

for i in range(rows):
    if i % 2 == 0:
        sym = Fore.GREEN + '*'
    else:
        sym = Fore.RED + '*'
    print(' ' * (rows - (i + 1)) + sym * (i * 2 + 1))
