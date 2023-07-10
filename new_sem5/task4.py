# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трём, программа должна выводит слово "Fizz".
# Вместо чисел, кратных пяти, - слово "Buzz".
# Если число кратно и трём, и пяти, программы выводит слово "FizzBuzz".
# Превратите решение в генераторное выражение, лучше многострочное (почему?).

gen1 = ('FizzBuzz' if num % (3 * 5) == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in range(0, 101))
gen2 = ('Fizz' * (not n % 3) + 'Buzz' * (not n % 5) or n for n in range(0, 101))

def gen3():
    for i in range(0,101):
        if i % (3 * 5) == 0:
            yield 'FizzBuzz'
        elif i % 5 == 0:
            yield 'Buzz'
        elif i % 3 == 0:
            yield 'Fizz'
        else:
            yield i

print(*gen1)
print(*gen2)
print(*gen3())

