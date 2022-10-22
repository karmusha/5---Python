# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 5, 6]
print(list)

def get_prod_of_pairs(list):
    prod_list = []
    count = len(list)
    for i in range(0, count):
        j = count - i - 1
        if j<i:
            break
        prod = list[i] * list[j]
        prod_list.append(prod)
    return prod_list

sum_list = get_prod_of_pairs(list)
print(sum_list)