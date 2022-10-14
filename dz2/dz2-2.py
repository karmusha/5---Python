# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число n: '))


def get_fuctorial(n):
    if n == 1:
        return n
    else:
        return n*get_fuctorial(n-1)


result = get_fuctorial(n)
        
print(f'Сумма чисел от 1 до {n} равна {result}')

