# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('dz5_1.txt', mode='w', encoding='utf-8') as file:
    file.writelines('абв, удклкт, вдлаабв, аб, 111\n')
    file.writelines('екерр, rабв, абваб, 321\n')

def has_no_abv(element):
    for symbol in element:
        if symbol == 'а':
            continue
        if symbol == 'б':
            continue
        if symbol == 'в':
            return False
    return True 

path = 'dz5_1.txt'
file = open(path, mode='r', encoding='utf-8')
for line in file:
    res = line.split(', ') # ['абв', 'удклкт', 'вдлаабв', 'аб', '111\n']
    new_list = list(filter(has_no_abv, res)) # ['удклкт', 'аб', '111\n']

    with open('dz_5_1_result.txt', mode='a', encoding='utf-8') as rf:
        new_list = ', '.join(new_list)
        rf.writelines(new_list)
        
file.close()
