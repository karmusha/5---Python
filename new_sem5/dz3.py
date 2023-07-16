# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def gen_fibonacci(n):
    f1, f2 = 0, 1
    for _ in range(n):
        f1, f2 = f2, f1 + f2
    yield f1


for i in range(8):
    print(next(gen_fibonacci(i)))
