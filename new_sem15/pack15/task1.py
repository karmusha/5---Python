# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл. 
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='sem15_1.log', level=logging.ERROR)
logger = logging.getLogger('__name__')

def dev(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error('Devision by zero is not allowed.')
        return float('inf') if a > 0 else float('-inf')
    
print(dev(1, 0))
