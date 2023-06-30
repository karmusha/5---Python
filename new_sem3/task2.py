# Пользователь вводит данные. Сделать проверку данных и преобразовать, если возможно, в один из вариантов:
# - Целое положительное число
# - Вещественное положительное или отрицательное число
# - Строку в нижнем регистре, если в строке есть хотя бы одна заглавная
# - Строку в верхнем регистре в остальных случаях
# * обработку исключений использовать нельзя

string = input('Input string: ')

if string.isdecimal():
    string = int(string)
elif string.replace('.', '').replace('-', '').isdecimal() and string.count('.') == 1 and string.count('-') <=1 \
    and string[-1] != '.' and string [1:].count('-') == 0:
    string = float(string)
elif string != string.lower():
    string = string.lower()
else:
    string = string.upper()

print(f'{string} - {type(string)}')
