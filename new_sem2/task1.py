import sys


data = [1, 15.25, 'Fu', '44', True, 1.0+1j, 1, b'\x00\x00\x00']

for i, item in enumerate(data, start=1):
    print(f'№ = {i}, Value = {item}, ID = {id(item)}, Size = {sys.getsizeof(item)}, Hash = {hash(item)}')
    if isinstance(item, int):
        print(f'{item} is integer')
    if isinstance(item, str):
        print(f'{item} is string')



