# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите десятичное число: '))

def invert_list(source_list):
    target_list = []
    for i in range(0, (len(source_list))):
        target_list.append(source_list[(len(source_list)-1-i)])
    return target_list

def get_binar_number(number):
    temp = number
    pre_result = []
    while temp>0:
        pre_result.append(temp%2)
        temp = int(temp/2)
    result = invert_list(pre_result)
    return result

binar_number = get_binar_number(number)
print(binar_number)