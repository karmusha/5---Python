# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл
# Для тестированию возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv

# dict_list = [{'one': '111', 'two': '111'},
#           {'one': '222', 'two': '222'},
#           {'one': '333', 'two': '333'},]

def pickle_to_csv(pickle_file: str, csv_file: str):
    pickle_obj = pickle.loads(open(pickle_file, 'rb').read())
    pickle_obj = pickle.dumps(pickle_obj)
    pickle_obj = pickle.loads(pickle_obj)

    with open('data.csv', 'w', newline='') as cf:
        w = csv.writer(cf)
        for i, val in enumerate(pickle_obj):
            if i == 0:
                w.writerow(val.keys())
            w.writerow(val.values())

pickle_to_csv('data.pickle', 'data.csv')
