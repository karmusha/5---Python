# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

allow_list = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9
}

result = 0

f = input('Введите число: ')
for i in f:
    for key, value in allow_list.items():
        if i == key:
            result += value
        
print(result)