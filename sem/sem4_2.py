# Найдите корни квадратного уравнения Ax2 + Bx + C = 0 с помощью математических формул нахождения корней квадратного уравнения. Вводим из файла.

with open('file_sem4_2.txt', 'w') as file:
    file.write(input('Введите значение А: ') + '\n')
    file.write(input('Введите значение B: ') + '\n')
    file.write(input('Введите значение C: ') + '\n')

list = []

file = open('file_sem4_2.txt', 'r')
for line in file:
    list.append(float(line))
print(list)
file.close()

a = list[0]
b = list[1]
c = list[2]

discriminant = b**2 - 4*a*c
print('Дискриминант = ' + str(discriminant))
if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))