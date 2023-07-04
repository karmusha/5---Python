# Напишите функцию для транспонирования матрицы

mat = [[1, 2, 3],
       [44, 55, 66],
       [777, 888, 999],
       [1010, 1111, 1212]] 

print("Your matrix: ")
for i in mat:
    print(i)

def transpose_matrix(matrix):
    trans_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            trans_matrix[b][a] = matrix[a][b]

    print("A transposed matrix: ")
    for i in trans_matrix:
        print(i)

transpose_matrix(mat)