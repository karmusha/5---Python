# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    return map(lambda x: list(x), zip(*mat))


mat = [[1, 2, 3],
       [44, 55, 66],
       [777, 888, 999],
       [1010, 1111, 1212]] 

print("Your matrix: ")
for i in mat:
    print(i)

new_mat = transpose_matrix(mat)

print("Your new matrix: ")
for i in new_mat:
    print(i)
       
