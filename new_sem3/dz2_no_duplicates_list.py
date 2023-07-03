# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

numbers = [11, 2, 3, 3, 2, 3, 4, 5]
print(f'{numbers = }')

res = []
count = 0
for value in set(numbers):
    if numbers.count(value) > 1:
        res.append(value)

print(f'List of duplicates: {res}')
