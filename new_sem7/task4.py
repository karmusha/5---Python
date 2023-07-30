# Создайте функцию, которая создаёт файлы с указанным расширением. 
# Функция принимает следующие параметры: 
#   - расширение 
#   - минимальная длина случайно сгенерированного имени, по умолчанию 6 
#   - максимальная длина случайно сгенерированного имени, по умолчанию 30 
#   - минимальное число случайных байт, записанных в файл, по умолчанию 256 
#   - максимальное число случайных байт, записанных в файл, по умолчанию 4096 
#   - количество файлов, по умолчанию 42 
#   - Имя файла и его размер должны быть в рамках переданного диапазона.


# Создайте новую функцию которая генерирует файлы с разными расширениями. 
# Расширения и количество файлов функция принимает в качестве параметров. 
# Количество переданных расширений может быть любым. 
# Количество файлов для каждого расширения различно. 
# Внутри используйте вызов функции из прошлой задачи.

import os
from random import choices, randint
import string


def create_file(extention, min_length=6, max_length=30, min_bytes=256, max_bytes=4096, file_numbers=42):
    folder_name = 'task4.files' 

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    for _ in range(file_numbers):
        file_name = ''.join(choices(string.ascii_lowercase, k=randint(min_length, max_length)))
        with open(f'{folder_name}/{file_name}.{extention}', 'wb') as f:
            f.write(os.urandom(randint(min_length, max_length)))

def gen_files(**kwargs):
    for key, value in kwargs.items():
        create_file(extention=key, file_numbers=value)

if __name__ == '__main__':
    gen_files(bin=2, txt=2)