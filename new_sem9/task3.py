# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

from functools import wraps
from pathlib import Path
import json
from typing import Callable


def deco(func: Callable):
    file_name = f'{func.__name__}.json'
    if Path(file_name).exists():
        with open(file_name, 'r', encoding='utf-8') as f:
            lres = json.load(f)
    else:
        lres = []

    # @wraps(func)
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

if __name__ == '__main__':
    @deco
    def myfunc(*args, **kwargs):
        return args, kwargs


    result = str(myfunc(1, t='one'))
    print(result)

    result = str(myfunc(2, d='two'))
    print(result)