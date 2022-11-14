# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from pathlib import Path

folder = Path(__file__).parent
file_input = folder.joinpath('dz5_4_input.txt')
file_output = folder.joinpath('dz5_4_output.txt')

def rle_compression(line):
    count = 0
    symbol = None
    for i in line:
        if symbol is None:
            symbol = i
            count +=1
            continue
        if i != symbol:
            yield f'{count}{symbol}'
            symbol = i
            count = 1
        else:
            count+=1
    
    if count > 0:
        yield f'{count}{symbol}'

def rle_decompression(line):
    count = ''
    for i in line:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            count += i
        else:
            if count != '':
                yield i*int(count)
            count = ''

def compression(file_input, file_output):
    with open(file_input, mode='r', encoding='utf-8') as f_in:
        with open(file_output, mode='w', encoding='utf-8') as f_out:
            for line in f_in:
                res = rle_compression(line.strip('\n'))
                f_out.writelines(res)
                f_out.write('\n')

def decompression(file_input, file_output):
    with open(file_input, mode='r', encoding='utf-8') as f_in:
        with open(file_output, mode='w', encoding='utf-8') as f_out:
            for line in f_in:
                res = rle_decompression(line.strip('\n'))
                f_out.writelines(res)
                f_out.write('\n')

comp = input('Введите y, если вы хотите запустить алгоритм компрессии.\n')
if comp == 'y':
    compression(file_input, file_output)

decomp = input('Введите y, если вы хотите запустить алгоритм декомпрессии.\n')
if decomp == 'y':
    decompression(file_input, file_output)
