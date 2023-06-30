# Создайте вручную кортеж, содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ - тип элемента,
# значение - список элементов данного типа.

import pprint

my_tuple = ('t1', 't2'), 1, 2, 3, 10.0, 20.0, 30.0, 'hi', 'hello', {33, 44}, {55, 66}, ['list1', 'list2'], 7.5+1J, {1: 'eins', 2: 'zwei'}, True, False, ('t3', 't4')

my_dictionary = {}

for item in my_tuple:
    if type(item) not in my_dictionary:
        my_dictionary[type(item)] = []
    my_dictionary[type(item)].append(item)
    # my_dictionary.setdefault(type(item), []).append(item)

pp = pprint.PrettyPrinter(depth=10)

pp.pprint(my_dictionary)
