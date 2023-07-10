# Создайте из строки словарь, где ключ - символ, а значение - код символа.
# При создании словаря используйте преобразование в одну строку.

from itertools import islice

string = 'This is my string.'

dictionary = {letter: ord(letter) for letter in set(string)}

print(dictionary)

# Сохранить инетатор словаря.
# Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

iterator = iter(dictionary.items())

for _ in range(5):
    print(next(iterator))

# print(*islice(iterator, 5), sep='\n')
