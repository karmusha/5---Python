# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def check_value():
    number = None
    while True:
        try:
            number = int(input('Введите число: '))
            if number < 0:
                raise ValueError
        except ValueError:
            print("Ошибка ввода числа")
            continue
        except Exception:
            print("Что-то пошло не так")
            continue
        break
    return number


a = check_value()
b = check_value()
c = check_value()

if a + b > c and b + c > a and a + c > b:
    print('Треугольник существует')
else:
    print('Такого треугольника не существует')
    exit(0)

if a == b == c:
    print('Это равносторонний треугольник')
elif a == b or a == c or b == c:
    print('Это равнобедренный треугольник')
else:
    print('Треугольник разносторонний')
