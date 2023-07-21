# ✔Напишите функцию, которая открывает на чтение созданные 
#   в прошлых задачах файлы с числами и именами. 
# ✔Перемножьте пары чисел. В новый файл сохраните имя и произведение: 
# ✔если результат умножения отрицательный, 
#   сохраните имя записанное строчными буквами и произведение по модулю 
# ✔если результат умножения положительный, 
#   сохраните имя прописными буквами и произведение округлённое до целого. 
# ✔В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
# ✔При достижении конца более короткого файла, возвращайтесь в его начало.

from pack7 import module_open_files as mof

file1 = 'new_sem7.txt'
file2 = 'new_sem77.txt'
file_res = 'new_sem7_mult.py'

mof.file_processing(file1, file2, file_res)