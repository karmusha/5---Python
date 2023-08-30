# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import os
from random import uniform, randint


def find_quadratic_from_csv(func):
    dic_res = {}
    def wrapper():
        with open('dz_new_sem9.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                func_res = func(*row) # допилить
                dic_res.update({row : func_res})
        return dic_res
    return wrapper


def deco(func):
    file_name = 'dz_new_sem9.json'
    lres = []

    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        res = {'args': args,
               'kwargs': kwargs,
               'result': func_res,}
        lres.append(res)
        with open(file_name, 'w', encoding='utf-8') as f1:
             json.dump(lres, f1, indent=2)
        return func_res
    return wrapper


def quadratic_formula(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        res = 'Корней нет'
    elif discriminant == 0:
        x = -b / (2 * a)
        res = str(x)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        res = str(x1) + str(x2)
    return res

def main():
    print('Start')

    def gen_numbers():
        with open('dz_new_sem9.csv', 'w', newline='') as f:
            writer_object = csv.writer(f)
            for _ in range(randint(100, 1000)):
                line = [uniform(1, 20) for __ in range(3)]
                quadratic_formula()
                writer_object.writerow(line)
    return gen_numbers
    

if __name__ == '__main__':
    main()