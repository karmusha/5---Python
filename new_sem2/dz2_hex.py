# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX_BASE = 16

def convert_number_to_str(number, base) -> str:
    letters = 'abcdef'
    res = []
    while number > 0:
        number, modulo = divmod(number, base)
        if modulo > 9:
            letter_id = modulo - 10
            modulo = letters[letter_id]
        res.append(str(modulo))
    return ''.join(res[::-1])

number = int(input('Введите число: '))

print('0x' + convert_number_to_str(number, HEX_BASE))
print(hex(number))
