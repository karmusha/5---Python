# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок

from random import randint
from dz1_chess import check

def gen_randomly(n):
    x = []
    y = []

    def validate(nx, ny):
        for k in range(0, len(x)):
            if (nx == x[k] and ny == y[k]) or (nx == y[k] and ny == x[k]):
                print(f"{nx} {ny} занято другой фигурой, пробую еще раз")
                return False
        
        return True

    for i in range(1, n+1):
        w = False
        while not w:
            new_x, new_y = randint(1, n), randint(1, n)
            w = validate(new_x, new_y)
        
        x.append(new_x)
        y.append(new_y)

    return x, y


if __name__ == "__main__":
    ex = False
    res: set[tuple] = set()

    while not ex:
        rand = gen_randomly(8)
        if check(rand[0], rand[1]):
            res.add(rand)
        
        ex = len(res) >= 4

    print(res)