# --- Selection sort ---
# [6, 15, 2, 9, -3]
# MIN = 6
# 6 < 15
# 6 > 2, MIN = 2
# ...
# [-3, 6, 15, 2, 9]
# ... 6, 15, 2, 9]
# MIN = 6
# 6 < 15
# 6 > 2, MIN = 2
# ...
# [-3, 2, 6, 15, 9]

from random import randint

def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]
 
 
a = []
for i in range(10):
    a.append(randint(1, 99))
 
print(a)
sel_sort(a)
print(a)

