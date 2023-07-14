# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
n = 8

def gen(n):
    x = []
    y = []

    def validate(nx, ny):
        for k in range(0, len(x)):
            if (nx == x[k] and ny == y[k]) or (nx == y[k] and ny == x[k]):
                return False
        
        return True
    for i in range(1, n+1):
        w = False
        while not w:
            new_x, new_y = [int(s) for s in input(f"введите координаты {i} ферзя ").split()]
            if new_x >= 1 and new_x <= n and new_y >= 1 and new_y <= n:
                w = True
            else:
                print(f"пожалуйста введите координаты от 1 до {n}")

            w = validate(new_x, new_y)
            if not w:
                print("Занято другой фигурой, введите другие координаты")
        
        x.append(new_x)
        y.append(new_y)

    return x, y

def check(x: list, y: list):
    cross = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                cross = False

    return cross


if __name__ == "__main__":
    x, y = gen(n)
    if check(x, y):
        print(f"не бьют друг друга")
    else:
        print(f"бьют друг друга")
