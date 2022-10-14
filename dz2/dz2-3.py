# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:*

#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

n = int(input('Введите число n (длину списка): '))
n_list = {}

def get_number_of_subsequence(n):
    return (1 + 1 / n) ** n

def fillin_n_list(n_list, n):
    for i in range(n):
        value = float(round(get_number_of_subsequence(i+1),2))
        n_list[i+1] = value

fillin_n_list(n_list, n)
print(n_list)

def get_values_sum(n_list, n):
    values_sum = 0
    for i in range(n):
        values_sum = values_sum + n_list[i+1]
    return values_sum

result = get_values_sum(n_list, n)
print(result)
