# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# list = []
# def get_random_number(number):
#     return number*number*number % 10

# for i in range(8,25):
#     i = list.append(get_random_number(i+1))
# print(list)


# ------------------------------------------------------------------------------------------
# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# data2 = open('file_sem3.txt', 'r')
# for line in data2:
#     print(line)
#     if '12' in line:
#         print('yes')
# data2.close()

# -------------------------------------------------------------------------------------------
# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем "йцу", ответ: -1
# - список: ["123", "234", "123", "567"], ищем "123", ответ: -1
# - список: [], ищем "123", ответ: -1

list3 = []
list_length = int(input('Введите длину списка: '))

for e in range(list_length):
    list3.append(input('Введите элемент списка: '))
print(list3)

search = input('Введите искомый элемент: ')
print(search)

def search_in_list(list: list, search): # вот эту функцию надо додумать
    match_count = 0

    i = 0
    for value in list:
        if search == value:
            match_count += 1
        
        if match_count == 2:
            return i
        
        i += 1
    
    return -1
        

res = search_in_list(list3, search)
if res == -1:
    print(f'В заданном списке искомый элемент "{search}" не встречается второй раз.')
else:
    print(f'В заданном списке искомый элемент "{search}" встречается второй раз на [{res}] позиции.')

# -------------------------------------------------------------------------------------------
# 4. Написать программу, проверяющую правильность написания выражения со скобками.
# {(())}([]{{[]}}) - правильно
# {[)}(){)) - неправильно, * указать, где ошибка

