# На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл. 
# Напишите аналогичный декоратор, но внутри используйте модуль logging.
# Сохраняйте в лог файл раздельно:
# - уровень логирования
# - дату события
# - имя функции (не декоратора)
# - аргументы вызова
# - результат

import logging

FORMAT = '{asctime} - {levelname:<5} - {funcName} -> {lineno}: {msg}'

logging.basicConfig(filename='sem15_2.log',
                    level=logging.INFO,
                    encoding='utf-8',
                    format=FORMAT,
                    style='{')
logger = logging.getLogger('__name__')

def loggenerator(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        logging.info(f'function {func.__name__} was called with arguments {a, b, c} with result {res}.')
        return res
    return wrapper


@loggenerator
def discriminant (a, b, c):
    d = b ** 2 - 4 * a * c
    match d:
        case d if d < 0:
            res = None
        case d if d == 0:
            res = -b / (2 * a)
        case d if d > 0:
            x1 = (-b + (d ** 0.5)) / (2 * a)
            x2 = (-b - (d ** 0.5)) / (2 * a)
            res = (x1, x2)
    return res
    
print(discriminant(1, 55, 5.5))