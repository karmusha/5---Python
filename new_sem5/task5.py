# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с 2.
# Для проверки числа на простоту, используйте правило: 
# число является простым, если оно нацело делится только на себя и на единицу.


def gen(number):
    start = 2
    yield start
    cnt = 1
    while cnt < number:
        start += 1
        for i in range(2, int(start ** 0.5) + 1):
            if start % i == 0:
                break
        else:
            cnt += 1
            yield start

print(*gen(30))
