# Напишите функцию, которая генерирует псевдоимена. 
# ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, 
# среди которых обязательно должны быть гласные. 
# ✔Полученные имена сохраните в файл.

from pack7 import module_random_names as mrn

mrn.random_name_to_file('new_sem77.txt', 3)