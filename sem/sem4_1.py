# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

with open('file_sem4_1.txt', 'w') as file:
    file.write('1 5 465 654 87 41 3')

file = open('file_sem4_1.txt', 'r')
for line in file:
    list = line.split(' ')
    list = [int(x) for x in list]
    print(list)
file.close()

n = [str(max(list)), str(min(list))]

result = ' '.join(n)

print(result)