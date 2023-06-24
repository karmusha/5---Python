# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функцию bin и oct используйте для проверки своего результата.

BINARY_BASE = 2
OCT_BASE = 8

def convert_number_to_str(number, base) -> str:
    res = []
    while number > 0:
        number, modulo = divmod(number, base)
        res.append(str(modulo))
    return ''.join(res[::-1])

number = int(input('Введите число: '))

print('0b' + convert_number_to_str(number, BINARY_BASE))
print(bin(number))

print('0b' + convert_number_to_str(number, OCT_BASE))
print(oct(number))