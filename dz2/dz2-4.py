# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

n = int(input('Введите число n: '))

list = []
for e in range(-n, n+1):
    list.append(e)
print(list)

first = int(input(f'Введите позицию первого числа в промежутке от 0 до {n*2+1}: '))
if first < 0 or first > n*2+1:
    print('Вы ввели неверную позицию первого числа, попробуйте ещё раз.')
    exit()

second = int(input(f'Введите позицию второго числа в промежутке от 0 до {n*2+1}: '))
if second < 0 or second > n*2+1:
    print('Вы ввели неверную позицию второго числа, попробуйте ещё раз.')
    exit()

def get_prod(list, first, second):
    return list[first] * list[second]

result = get_prod(list, first, second)
print(f'Произведение чисел {list[first]} и {list[second]} = {result}')
