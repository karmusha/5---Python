# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

def get_ending_bonbons_may_take(bonbons):
    s = str(bonbons)
    if s[-1] == '1': return 'ы'
    else: return ''

def get_bonbons_number(bonbons):
    if bonbons in range(1,28):
        print(f'Вы можете взять от 0 до {bonbons} конфет{get_ending_bonbons_may_take(bonbons)}.')
    while True:
        try:
            bonbons_taken_in_this_round = int(input())
            if bonbons_taken_in_this_round < 1:
                print('За один ход нужно забрать хотя бы 1 конфету.')
                continue
            if bonbons_taken_in_this_round > bonbons:
                print(f'За один ход можно забрать не более чем {bonbons} конфет{get_ending_bonbons_taken(bonbons)}.')
                continue
            if bonbons_taken_in_this_round > 28:
                print('За один ход можно забрать не более чем 28 конфет.')
                continue
        except ValueError:
            print('Вы должны ввести целое число. Попробуйте ещё раз.')
            continue
        break
    return bonbons_taken_in_this_round

def get_ending_bonbons_number_on_table(bonbons):
    if bonbons < 10:
        match bonbons:
            case 1: return 'а'
            case 2: return 'ы'
            case 3: return 'ы'
            case 4: return 'ы'
            case _: return ''
    else:
        s = str(bonbons)
        if s[-2] != '1':
            if s[-1] == '1': return 'а'
            if s[-1] == '2' or s[-1] == '3' or s[-1] == '4':return 'ы'
            else: return ''
        else: return ''

def get_ending_bonbons_taken(bonbons_taken):
    if bonbons_taken < 10:
        match bonbons_taken:
            case 1: return 'у'
            case 2: return 'ы'
            case 3: return 'ы'
            case 4: return 'ы'
            case _: return ''
    else:
        s = str(bonbons_taken)
        if s[-2] != '1':
            if s[-1] == '1': return 'у'
            if s[-1] == '2' or s[-1] == '3' or s[-1] == '4':return 'ы'
            else: return ''
        else: return ''

def get_ending_bonbons_remained(bonbons_taken):
    if bonbons_taken < 10:
        match bonbons_taken:
            case 1: return 'а'
            case 2: return 'ы'
            case 3: return 'ы'
            case 4: return 'ы'
            case _: return ''
    else:
        s = str(bonbons_taken)
        if s[-2] != '1':
            if s[-1] == '1': return 'у'
            if s[-1] == '2' or s[-1] == '3' or s[-1] == '4':return 'ы'
            else: return ''
        else: return ''

def hod(player_number, bonbons, player_name):
    if player_number == 1:
        number = 'Первый'
    if player_number == 2:
        number = 'Второй'
    print(f'{player_name}, ваш ход. Сколько конфет вы возьмёте?')
    bonbons_taken = get_bonbons_number(bonbons)
    
    print(f'{player_name}, вы взяли {bonbons_taken} конфет{get_ending_bonbons_taken(bonbons_taken)}.')

    return bonbons_taken

# --- Game ---   

print(f'Условие задачи: На столе лежит {bonbons} конфет{get_ending_bonbons_number_on_table(bonbons)}. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')

while True:
    try:
        bonbons = int(input('Сколько конфет лежит на вашем столе? Введите число от 30 до 3000: '))
        if bonbons < 29:
            print('Это не ваш стол. Посмотрите на другой стол. Должно быть больше 30 конфет.')
            continue
        if bonbons > 3000:
            print('Это не ваш стол. Посмотрите на другой стол. Должно быть не больше 3000 конфет.')
            continue
    except ValueError:
        print('Вы должны ввести целое число. Попробуйте ещё раз.')
        continue
    break

player1_name = input('Игрок 1, введите своё имя:\n')
player2_name = input('Игрок 2, введите своё имя:\n')

input('Сначала жеребьёвка, у кого выпадет большее число, тот ходит первым. Нажмите Enter.')

while True:
    player1 = random.randint(1,6)
    player2 = random.randint(1,6)
    if player1 != player2:
        break

print(f'{player1_name}, вам выпало {player1}.')
print(f'{player2_name}, вам выпало {player2}.')

if player1 > player2:
    first_player = 1
    second_player = 2
    print(f'{player1_name}, вы ходите первым.')
else:
    first_player = 2
    second_player = 1
    player1_name, player2_name = player2_name, player1_name
    print(f'{player1_name}, вы ходите первым.')

player_name = player1_name

while bonbons > 0:
    player_number = first_player
    bonbons -= hod(player_number, bonbons, player_name)
    if bonbons == 0:
        print(f'На столе не осталось конфет.\n{player_name}, вы выиграли! Заберите все конфеты у другого игрока.')
        break
    else:
        print(f'На столе осталось {bonbons} конфет{get_ending_bonbons_remained(bonbons)}.')
    player_name, player2_name = player2_name, player_name

text = '''
     _   _______________   _       _   _______________   _       _   _______________   _              
    | \ /               \ / |     | \ /               \ / |     | \ /               \ / |
    |  (                 )  |     |  (                 )  |     |  (                 )  |
    |_/ \_______________/ \_|     |_/ \_______________/ \_|     |_/ \_______________/ \_|
'''
print(text)
print('Спасибо за игру!\n')
input('Нажмите любую клавишу, чтобы выйти.')

