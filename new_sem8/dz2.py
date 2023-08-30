# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle

with open('data.csv', mode='r') as f:
    for row in f:
        row = pickle.dumps(row)
        row = str(row, encoding='latin1')
        print(row)
