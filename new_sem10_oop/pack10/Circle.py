# Создайте класс окружность. Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

import math

class Circle:

    def __init__(self, raduis):
        self.radius = raduis

    def length(self):
        return 2 * math.pi * self.radius
    
    def square(self):
        return math.pi * self.radius ** 2
    
    @classmethod
    def from_length(cls, length):
        return cls(length / 2 / math.pi)
    
    @classmethod
    def from_square(cls, square):
        return cls((square / math.pi) ** 0.5)

if __name__ == '__main__':
    circle1 = Circle(10)
    circle2 = Circle.from_length(62)
    circle3 = Circle.from_square(314)    
    print(f'{circle1.length() = }')
    print(f'{circle1.square() = }')
    print(f'{circle2.length() = }')
    print(f'{circle2.square() = }')
    print(f'{circle3.length() = }')
    print(f'{circle3.square() = }')
