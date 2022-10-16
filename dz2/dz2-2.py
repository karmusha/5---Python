# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число n, больше 0: '))

if n <=0:
    print('Вы ввели неверное число. Попробуйте другое.')
    exit()

def get_factorial(n):
        if n == 1:
            return n
        else:
            return n*get_factorial(n-1)

list = []
for i in range(0, n):
    list.append(get_factorial(i+1))

print(list)

