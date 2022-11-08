# Создайте программу для игры в ""Крестики-нолики"".
#     1   2   3
#    --- --- ---
# 1 | x | x | x |
#    --- --- ---
# 2 | x | x | x |
#    --- --- ---
# 3 | x | x | x |
#    --- --- ---

import random

def out_green(text):
    print("\033[32m{}".format(text))
    

def print_mas(mas):
    for line in mas:
        print(' | '.join(list(map(str, line)))) # print('Как поменять цвет ' + '\033[96mодного\033[0m' + ' слова?')
        print("\033[0m{}".format('---------'))

def exchange_player_names(player1_name, player2_name):
    temp = player1_name
    player1_name = player2_name
    player2_name = temp
    return player1_name, player2_name

def win_case(mas):
    match (mas):
        case (mas) if mas[0][0] == mas[0][1] == mas[0][2]: return True
        case (mas) if mas[1][0] == mas[1][1] == mas[1][2]: return True
        case (mas) if mas[2][0] == mas[2][1] == mas[2][2]: return True
        case (mas) if mas[0][0] == mas[1][0] == mas[2][0]: return True
        case (mas) if mas[0][1] == mas[1][1] == mas[2][1]: return True
        case (mas) if mas[0][2] == mas[1][2] == mas[2][2]: return True
        case (mas) if mas[0][0] == mas[1][1] == mas[2][2]: return True
        case (mas) if mas[0][2] == mas[1][1] == mas[2][0]: return True
    return False


def hod(player_number, player_name, mas):
    if player_number == 1:
        sign_name = 'крестик'
        sign = 'x'
    if player_number == 2:
        sign_name = 'нолик'
        sign = 'o'
    
    while True:
        try:
            i, j = tuple(map(int, input(f'{player_name}, ваш ход. Введите через запятую номер строки и столбика, куда хотите поставить {sign_name}.\n').split(",")))
            if (i, j) == (0, 0):
                print('No')
                continue
            i -= 1
            j -= 1
            if mas[i][j] == 'x' or mas[i][j] == 'o':
                print('Здесь уже занято. Попробуйте другое поле.')
                continue
            mas[i][j] = sign    
        except ValueError:
            print('Вы ввели неверно. Попробуйте ещё раз.')
            continue
        except IndexError:
            print('Вы ввели неверно. Попробуйте ещё раз.')
            continue
        break
    return mas

# --- Жеребьевка ---

# input('Сначала жеребьёвка, у кого выпадет большее число, тот ходит первым и ставит крестики. Нажмите Enter.')
# player1_name = input('Игрок 1, введите своё имя:\n')
# player2_name = input('Игрок 2, введите своё имя:\n')

player1_name = 'Karma'
player2_name = 'Sergey'

while True:
    random_number1 = random.randint(1,6)
    random_number2 = random.randint(1,6)
    if random_number1 != random_number2:
        break

print(f'{player1_name}, вам выпало {random_number1}.')
print(f'{player2_name}, вам выпало {random_number2}.')

if random_number1 > random_number2:
    first_player = 1
    second_player = 2
    print(f'{player1_name}, вы ходите первым.')
else:
    first_player = 2
    second_player = 1
    player1_name, player2_name = player2_name, player1_name
    print(f'{player1_name}, вы ходите первым.')

player_name = player1_name

# --- Game ---   

print(f'Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики). Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает. Первый ход делает игрок, ставящий крестики.')

mas = [
    [' ', ' ', ' '], 
    [' ', ' ', ' '], 
    [' ', ' ', ' ']]

print_mas(mas)

while not win_case(mas):
    player_number = first_player
    mas = hod(player_number, player_name, mas)
    print_mas(mas)
    player_name, player2_name = player2_name, player_name
    first_player, second_player = second_player, first_player

print(f'{player_name}, вы выиграли!')

print('Спасибо за игру!\n')
input('Нажмите любую клавишу, чтобы выйти.')


