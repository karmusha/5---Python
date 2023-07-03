# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ Unicode, а значением - его порядковый номер из диапазона, границами которого являются введенные числа.
# Границы диапазона учитывать.

nums = '48 57'

def symbols_and_codes(nums) -> dict:
    start, end = sorted(map(int, nums.split()))
    return {chr(i): i for i in range(start, end+1)}

print(symbols_and_codes(nums))