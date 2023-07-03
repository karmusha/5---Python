# Функция получает на вход список чисел.
# Отсортируйте список по убыванию суммы цифр.

nums = [111, 222, 333, 92, 22, 1]

def sum_of_numbers(number):
    s = 0
    while number > 0:
        s += number % 10
        number //= 10
    return s

print(sorted(nums, key=sum_of_numbers, reverse=True))
