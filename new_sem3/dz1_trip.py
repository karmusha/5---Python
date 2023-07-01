# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

people_and_things: dict = {'Ira': ('sleeping bag', 'cup', 'plate', 'sandals', 'glasses'),
                     'Eva': ('sleeping bag', 'cup', 'flashlight', 'camera', 'plate'),
                     'Petr': ('sleeping bag', 'cup', 'flashlight', 'tent', 'sandals', 'sandals'),
                     }

print(f'{", ".join(people_and_things.keys())} went on a trip.')

things_all_took = set()
all_things = set()
unique_thing = ''

for key in people_and_things:
    for element in people_and_things[key]:
        all_things.add(element)
print(f'They took the following things: {", ".join(all_things)}.\n')


for item in all_things:
    res  = map(lambda x: item in x, people_and_things.values())
    if all(res):
        things_all_took.add(item)
    
    res = map(lambda x: x[0] if item in x[1] else None, people_and_things.items())
    res = filter(lambda x: True if x else False, res)
    res = list(res)
    if (len(res) == 1):
        print(f'Only {res[0]} took {item}.')
    
    res = map(lambda x: x[0] if item not in x[1] else None, people_and_things.items())
    res = filter(lambda x: True if x else False, res)
    res = list(res)
    if (len(res) == 1):
        print(f'{res[0]} took no {item}.')
    
print(f'\nEveyone took the following things: {", ".join(things_all_took)}.')
