# Посчитайте сумму чётных чисел от 1 до n исключая кратные e.
# Использвуте while и if.
# Попробуйте разные значения e и n.

n, e, sum = 8, 3, 0

count = 1
while count <= n:
    if count % 2 == 0 and count % e != 0:
        sum += count
    count += 1

print(sum)