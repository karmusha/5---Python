value = None
print(type(value))
a = 123
b = 1.23
print(a)
print(b)
value = 12345
print(type(value))

s = 'qwerty'
print(s) # вывод строки
#comment

s = "hello's world" # если надо использовать одинарную кавычку внутри строки, то снаружи используем двойные кавычки
print(s)
s = 'hello "world"' # и наоборот, если надо использовать двойные кавычки внутри строки, то снаружи используем одинарные кавычки
print(s)
s = 'hello \'world' # Escape последовательности через обратный слэш \
print(s)
# s = 'hello \nworld' # Escape последовательности через обратный слэш \n - переход на новую строку
print(s)

print (a, 'какие-то ещё строки', b, s)
print ('{} - {} - {}'.format(a, b, s)) #форматированный вывод
print ('{1} - {2} - {0}'.format(a, b, s)) #если нужно поменять порядок вывода, пишем индексы переменных в скобках
print (f'{a} - {b} - {s}') #форматированный вывод с интерполяцией


# Логическая переменная
f = True
print(f)

f = False
print(f)

# "Массивы" в Python с помощью списков
list = [1, 2, 3]
print(list)
list = ['1', '2', '3'] # можно любого типа
# list = ['1', '2', 123456, tj3] # можно любого типа, но нежелательно
print(list)

# Ввод и вывод данных
# print, input

print('Введите а')
a = int(input())
print('Введите b')
b = int(input())
print(a, ' + ', b, ' = ', a+b)

# Арифметические операции
# +, -, *, /, %, //, **
# Приоритет операций 
# **, (+), (-), *, /, //, %, +, -
# () Скобки меняют приоритет

r = 1.31231223
t = 3
y = r//t # Деление в целых числах
print(y)
o = r**t # Возведение в степень
print(o)
y = round(r*t, 5) # Чтобы показывалось округлённое число, через запятую указывается количество после запятой
print(y)

# Логические операции
# >, <=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 > 4
print(a)

func = 1
T = 4
x = 2
print(func<T>(x)) # можно также написать (func<T>x)

func2 = 1>2 or 4<6
print(func2) # дизюнкция работает, если одно из высказываний верно

func3 = [1, 2, 3, 4]
print(func3)
print(not 2 in func2)

is_odd = func3[0] % 2 == 0 # лучше записать 'not func3[0] % 2'
print(is_odd)

g = int(input())
h = int(input())
if g > h:
    print(g)
elif g == h:
    print(g)
else:
    print(h)

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит')
print(inverted)

list = [1, 2, 3, 4, 5]
for i in 1, 2, 3, 4, 5:
    print(i**2)

r = range(10) # Задаём range
for i in r: # И выводим его
    print(i)

for i in range(5): # Или можно сразу так вывести
    print(i)

for i in range(2, 5): # Или можно вывести диапазон
    print(i)

for i in range(2, 10, 2): # Или можно вывести диапазон, а третьим аргументом можем задать приращение
    print(i)

for i in 'qwer - ty': # Или можно вывести строку, разбитую на символы
    print(i)

# О строках
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё', 'ЕЩЁ')) # 
print(text[0]) # 'c'
print(text[len(text)-1]) # к
print(text[-5]) # 'б'
print(text[:]) # print(0:len(text)-1)
print(text[:2]) # 'съ'
print(text[6:-18]) # 'ещё этих мягких'
print(text[::6]) # print(0:len(text):6) 'сеикакл'


help(text.inspace) # Если нужна справка


# Введение: списки

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]

numbers = range(1, 6)
print(numbers) # [1, 2, 3, 4, 5]

numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]

for i in numbers:
    i *=2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue'] # red green blue

for e in colors:
    print(e*2) # redred greengreen blueblue

colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # del colors[0] # удалить элемент

# Функции
#def funtcion_name(x):
    # body line 1...
    # optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
