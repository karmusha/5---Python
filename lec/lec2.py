# -------- Открытие, добавление и запись в файл --------

with open('file.txt', 'w') as data: 
    data.write('Line 222\n')
    data.write('Line 333\n')
    # в данном случае не нужно вызывать data.close()

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
data.write('Line 2\n')
data.write('Line 3\n')
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

# -------- Импорт функции из другого файла (в текущей папке) --------

from lec1 import get_fuctorial as gf

print(gf(4))

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5)) # !!!!!
print(new_string('!'))    # !!!
print(new_string(4))      # 12 (4 * 3)

# -------- Конкатенация --------

def concatenatio(*params):
    res: str = ''
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(concatetetio(1, 2, 3, 4)) # TypeError: ...

# -------- Рекурсия --------

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34

# -------- Кортежи - неизменяемый список --------

a = (3, 4)
print(a)
print(a[0]) # 3
print(a[-1]) # 4 - c конца

b = (44,) # Кортеж из одного элемента, обязательно поставить запятую

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue

# -------- Словари --------

dictionary = {}
dictionary = \
    {
        'up': 'вверх',
        'left': 'влево',
        'down': 'вниз',
        'right': 'вправо'
    }

print(dictionary) # {'up': 'вверх', 'left': 'влево', 'down': 'вниз', 'right': 'вправо'}
print(dictionary['left']) # влево
# Типы ключей могут отличаться

for k in dictionary.keys():
    print(k)

for v in dictionary.values():
    print(v)

for all in dictionary:
    print(dictionary[all]) #  Получить только значения

del dictionary['up'] # Удаление элемента

for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))


# -------- Множества --------

colors = {'red', 'green', 'blue'} # Это и будет множество
print(type(colors)) # <class 'set'>
print(colors) # {'red', 'blue', 'green'}

colors.add('red') # {'red', 'blue', 'green'}
colors.add('gray') # {'red', 'blue', 'gray', 'green'}
colors.remove('green') # {'red', 'blue', 'gray'}
colors.discard('red') # {'blue', 'gray'}
colors.clear() # set()

set1 = {1, 2, 3, 5, 8}
set2 = {2, 5, 8, 13, 21}
clone = set1.copy() # clone = {1, 2, 3, 5, 8}
union = set1.union(set2) # union = {1, 2, 3, 5, 8, 13, 21} Объединение
intersection = set1.intersection(set2) # intersection = {8, 2, 5} Пересечение
diff1 = set1.difference(set2) # diff1 = {1, 3} Разница
diff2 = set2.difference(set1) # diff2 = {13, 21} Разница

q = set1 \
    .union(set2) \
    .difference(set1.intersection(set2))
print(q) # {1, 21, 3, 13}

frozen = frozenset(set1) # Заморозить множество, чтобы оно стало неизменяемым

# -------- Списки --------

list1 = [1, 2, 3, 4, 5]
list2 = list1

list1[0] = 123
list2[1] = 222

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

print(list1.pop(2)) # Удалить третий элемент нашего списка
print(list1.insert(2, 11)) # Добавить 11 после третьего элемента нашего списка
print(list1.append(453)) # Добавление в конец списка
print(list1)