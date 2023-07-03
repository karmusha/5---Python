# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


import itertools as it

MAX_WEIGHT = 15000
MIN_THINGS_TO_TAKE = 9

things_for_trip: dict = {'sleeping bag': 1120,
                     'dish': 400,
                     'camera': 1500,
                     'tent': 3500,
                     'traking shoes': 1500,
                     'big pot': 558,
                     'food': 5000,
                     'snacks': 3250,
                     'clothes': 3100,
                     'knife': 235,
                     'guittar': 3000,
                     'hookah': 3400,
                     }

list_of_things = [key for key in things_for_trip.keys()]
print(list_of_things)

combinations = []
for r in range(MIN_THINGS_TO_TAKE, len(list_of_things) + 1):
    for combination in it.combinations(list_of_things, r):
        combinations.append(combination)

things = []

for combination in combinations:
    combination_str  = map(str, combination)
    weight = 0
    for item in combination_str:
        item_weight = things_for_trip.get(item)
        weight += item_weight
    if weight <= MAX_WEIGHT:
        print(f'You can take: {combination}.')
    else: continue
