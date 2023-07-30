# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

# Создайте класс Матрица. Добавьте методы для: 
# - вывода на печать, 
# - сравнения, (если равны: одинаковый размер, количество элементов)
# - сложения, (если они равны)
# - *умножения матриц (если кол-во столбцов одной мартицы равно кол-ву строк другой матрицы)

class Matrix:
    """Класс Матрица. Создаётся из списка списков."""


    def __init__(self, matrix):
        self.matrix = matrix
    
    def __str__(self):
        """Вывод матрицы на печать для пользователя."""


        return '[' + ']\n['.join('\t'.join(map(str, row)) for row in self.matrix) + ']'
    
    def __getitem__(self, index):
        return self.matrix[index]
    
    def matrix_size(self):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        return rows, columns

    def get_high(self):
        return len(self.matrix[0])

    def get_weight(self):
        return len(self.matrix)

    def check_matrix_equality(self, other):
        """
        Проверяет мартицы одинаковость размерностей
            :param self: Первая матрица
            :param other: Вторая матрица
    
            :return: True or False
        """
    
        if self.get_high() == other.get_high() and self.get_weight() == other.get_weight():
            return True
        
        return False

    def __eq__(self, other):
        """Сравнение мартиц одинавовой размерности на равенство"""
    
        if self.check_matrix_equality(other):
            res = zip(self.matrix, other)
            res = map(lambda x: x[0] == x[1], res)
            return all(res)

        return False
    
    def __add__(self, other):
        """Сложение мартиц одинавовой размерности"""

        if not self.check_matrix_equality(other):
            return 'Нельзя сложить матрицы разных размерностей'
        
        result = []
        numbers = []
        for i in range(self.get_weight()):
            for j in range(self.get_high()):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        
        return Matrix(result)

    def __mul__(self, other):
        """Умножение мартиц (длина одной матрицы должна быть равна ширине другой матрицы)"""

        if self.get_high() != other.get_weight():
            return 'Нельзя перемножить такие матрицы'
        
        result = []
        for i in range(self.get_weight()):
            res = []
            for j in  range(other.get_weight()):
                el, m = 0, 0
                for k in range(self.get_high()):
                    m = self[i][k] * other[k][j]
                    el += m
                res.append(el)
            result.append(res)
        return Matrix(result)
        

if __name__ == '__main__':
    m1 = Matrix([
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
    ])

    m2 = Matrix([
        [10, 10, 10],
        [20, 20, 20],
        [30, 30, 30]
    ])

    m3 = Matrix([
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
    ])

    print(m1)
    print(m2)
    print(m3)

    print(f'{m1 == m2 = }')
    print(f'{m1 == m3 = }')

    print(f'Сложение:\n{m1 + m2}')
    print(f'Умножение:\n{m1 * m2}')
