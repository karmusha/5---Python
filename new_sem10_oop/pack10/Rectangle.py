# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

# Добавьте возможность сложения и вычитания. 
# При этом должен создаваться новый экземпляр прямоугольника. 
# Складываем и вычитаем периметры, а не длинну и ширину. 
# При вычитании не допускайте отрицательных значений.

# Добавьте сравнение прямоугольников по площади 
# Должны работать все шесть операций сравнения

class Rectangle:
    
    def __init__(self, width, length=None):
        self.width = width
        self.length = length
        if length is None:
            self.length = width


    def perimeter(self):
        return 2 * (self.width + self.length)
    
    def square(self):
        return self.width * self.length

    def __add__(self, other):
        res_perimeter = self.perimeter() + other.perimeter()
        new_length = self.length + other.length
        new_width = res_perimeter / 2 - new_length
        return Rectangle(new_length, new_width)
    
    def __sub__(self, other):
        res_perimeter = self.perimeter() - other.perimeter()
        coeff = self.lenght / other.length # Коэффициент непонятно, как посчитать
        new_length = self.length * coeff
        new_width = res_perimeter / 2 - new_length
        if res_perimeter is 0:
            raise Exception
        else:
            res_perimeter =  abs(res_perimeter)
        return Rectangle(new_length, new_width)
    
    def __eq__(self, other):
        return self.square() == other.square()
    
    def __gt__(self, other):
        return self.square() > other.square()
    
    def __ge__(self, other):
        return self.square() >= other.square()

        
    
if __name__ == '__main__':
    rectangle1 = Rectangle(10, 15)
    rectangle2 = Rectangle(10)
    print(f'{rectangle1.perimeter() = }')
    print(f'{rectangle1.square() = }')
    print(f'{rectangle2.perimeter() = }')
    print(f'{rectangle2.square() = }')

    print(rectangle1 == rectangle2)
    print(rectangle1 != rectangle2)
    print(rectangle1 > rectangle2)
    print(rectangle1 < rectangle2)
    print(rectangle1 >= rectangle2)
    print(rectangle1 <= rectangle2)
