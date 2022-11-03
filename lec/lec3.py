# --- lambda() ---
print("--- lambda() ---")

# def sum(x, y):
#     return x+y

sum = lambda x, y: x + y

def mult(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    return op(a, b)

# calc(sum, 4, 5)
calc(lambda x, y: x + y, 4, 5)

# --- List Comprehentions ---
print("--- list comprehentions ---")

list0 = []
for i in range(1, 21):
    if (i % 2 == 0):
        list0.append(i)

# [exp for item in iterable]
list0 = [i for i in range(1, 21)]
print(list0) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# [exp for item in iterable (if conditional)]
list0 = [i for i in range(1, 21) if i % 2 == 0]
print(list0) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# с кортежем
list0 = [(i, i) for i in range(1, 21) if i % 2 == 0]
print(list0) # [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]

# с функцией

def f(x):
    return x**3

list0 = [f(i) for i in range(1, 21) if i % 2 == 0]
print(list0) # [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]

# [exp <if conditional> for item in iterable (if conditional)]

with open('lec3.txt', 'w') as file:
    file.write('1 2 3 5 8 15 23 38')

path = 'lec3.txt'
file = open(path, 'r')
list0 = file.read() # Формируем список из файла, считывая элементы, разделённые пробелом
file.close()

string = '1 2 3 5 8 15 23 38'.split()
# Можно переделать строку в список
print(string)
print(type(string))

list2 = list0.split(' ')
print(list2)
print(type(list2))

def select(f, col): # Типа урезанная версия функции map()
    return [f(x) for x in col]

def where(f, col): # Типа функция filter()
    return [x for x in col if f(x)]

res = select(int, list2) 
res = where(lambda x: not x % 2, res) # Получаем список только четных чисел
res = select(lambda x: (x, x**2), res) # Получаем кортеж числа и его квадрата

print(res)

# --- map() ---
print("--- map() ---")

li = [i for i in range(1, 20)]
print(li)

li = list(map(lambda x: x+10, li))
print(li)

print("Введите элементы первого списка через запятую")
# data1 = map(int, input().split(','))

# for e in data1:
#     print(e)
# print("---")

# for e in data1:
#     print(e)

# Второй раз по мапе пробежаться нельзя, так как это итератор. Чтобы пробегаться по многу раз, нужно оберунуть это в list, как сделано ниже.

print("Введите элементы второго списка через пробел")
# data2 = list(map(int, input().split()))


# --- filter() ---
print("--- filter() ---")

data3 = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data3))
print(res)


print("--- Преобразуем код: ---")
data3 = '1 2 3 2 56 45 78 456'.split()

res = list(map(int, data3))
res = filter(lambda x: not x % 2, res) # Получаем список только четных чисел
res = list(map(lambda x: (x, x**2), res)) # Получаем кортеж числа и его квадрата
print(res)

# --- zip() --- пробегается по минимальному входящему набору
print("--- zip() ---")

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data4 = list(zip(users, ids, salary))
print(data4)

# --- enumarate() --- возращает итератор с кортежами
print("--- enumarate() ---")

data5 = list(enumerate(['Kazan', 'Barnaul', 'Moskow', 'Omsk']))
print(data5)
