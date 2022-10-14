# Напишите программе, которая будет принимать на вход число N и выводить числа от -N до N.

n = int(input('Введите число N: '))
print(n)

def get_list_from_minus_N_to_N (n):
    list = range(-n, n+1)
    for i in list:
        print(i)
        
get_list_from_minus_N_to_N(n)

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

drob = float(input('Введите число: '))
result = drob * 10 % 10
print (result)


# Напигите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30).

number = int(input('Введите число: '))
if number % 5 == 0 and number % 10 == 0:
    print('Yes')
elif number % 15 == 0 and number % 30 != 0:
    print('Yes 2')
else:
    print('No')

# Таблица умножения числа

num = int(input('Введите число: '))

for i in range(1,11):
    print(f"{num} * {i} = {num * i}")