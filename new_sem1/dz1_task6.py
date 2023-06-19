# Выведите в консоль таблицу умножения от 2*2 до 9*10 как на школьной тетради

print('Таблица умножения'.center(60))

for i in range(1, 11):
    for k in range(2, 6):
        print(f'{k} * ' + f'{i}'.rjust(2) + ' = ' + f'{i * k}\t'.rjust(3), end=' ')
    print('')

print('')

for i in range(1, 11):
    for k in range(6, 10):
        print(f'{k} * ' + f'{i}'.rjust(2) + ' = ' + f'{i * k}\t'.rjust(3), end=' ')
    print('')  

print('Всё!'.center(60))