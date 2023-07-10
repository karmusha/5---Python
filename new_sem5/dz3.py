# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

n = 0

def gen_fibonacci(n):
    if n == 0:
        yield 0
        n += 1
    if n == 1 or n == 2:
        yield 1
        n += 1
    else:
        yield (n-1) + (n-2)
        n+= 1

for i in range(0, 8):
    print(next(gen_fibonacci(i)))
