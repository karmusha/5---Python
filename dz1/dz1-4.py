# --- 4 ---
# Напишите программу, которая по заданному номеру четверти показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Введите номер четверти от 1 до 4: '))
if 1 < num > 4:
    print('Вы ввели неверный номер четверти. Попробуйте ещё раз.')
else:
    if num == 1:
        print(f'В {num} плоскости x > 0 and y > 0')
    elif num == 2:
        print(f'В {num} плоскости x < 0 and y > 0')
    elif num == 3:
        print(f'В {num} плоскости x < 0 and y < 0')
    else:
        print(f'В {num} плоскости x > 0 and y < 0')