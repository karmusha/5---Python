from functools import reduce


numbers = [1, 2, 3, 1, 2, 3]
print(f'{numbers = }')
       
new_numbers = []

for i in numbers:
    if i not in new_numbers:
        new_numbers.append(i)

print (f'{new_numbers = }')

new_numbers_from_keys = list(dict.fromkeys(numbers))
print (f'{new_numbers_from_keys = }')

new_numbers_to_set = list(set(numbers))
print (f'{new_numbers_to_set = }')

new_numbers_with_for = [x for i, x in enumerate(numbers) if i == numbers.index(x)]
print (f'{new_numbers_with_for = }')


new_numbers_with_lambda = reduce(lambda l, x: l if x in l else l + [x], numbers, [])
print (f'{new_numbers_with_lambda = }')
