# 5) Реализуйте алгоритм перемешивания списка.
import random

list = [1, 2, 3, 4, 5]
print(list)

def sort_list(list):
    for i in range(0, (len(list)-1)):
        r = random.randint(0, (len(list)-1))
        temp = list[i]
        list[i] = list[r]
        list[r] = temp
    return list
sort_list(list)
print(list)