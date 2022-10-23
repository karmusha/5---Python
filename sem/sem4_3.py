# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

one = abs(int(input('Введите первое число: ')))
two = abs(int(input('Введите второе число: ')))

def get_lcd(one, two):
    i = 1
    j = 1
    prod_one = one*i
    prod_two = two*j
    while prod_one != prod_two:
        if prod_one < prod_two:
            i+=1
            prod_one = one*i
        elif prod_one > prod_two:
            j+=1
            prod_two = two*j
    return prod_two

result = get_lcd(one, two)
print(f'Наименьшее общее кратное чисел {one} и {two} равно {result}.')