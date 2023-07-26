# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

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
    
if __name__ == '__main__':
    rectangle1 = Rectangle(10, 5)
    rectangle2 = Rectangle(10)
    print(f'{rectangle1.perimeter() = }')
    print(f'{rectangle1.square() = }')
    print(f'{rectangle2.perimeter() = }')
    print(f'{rectangle2.square() = }')

