# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 - Ответ в данном примере неверный.
# Правильный пример:
# - [1.1, 1.2, 3.1, 5.0, 10.01] => 0.2
#                     ^
# Потому что у пятёрки дробная часть равна нулю.

list = [1.1, 1.2, 3.1, 5.1, 10.01] # Исправила на 5.1, чтобы получить ответ 0.19, как в примере.
print(list)
list_drob = [round(i%1, 2) for i in list]
# Можно не округлять, но для красоты отображения пускай будет так.
 
print(list_drob)

def find_min(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def find_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

def get_difference(list):
    return find_max(list) - find_min(list)

result = get_difference(list_drob)
print(round(result, 2))
