# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных). 
# Используйте декораторы свойств.
# Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Rectangle:

    __slots__ = '_length', '_width'
    
    def __init__(self, width, length=None):
        self.width = width
        self.length = length
        if length is None:
            self.length = width


    def perimeter(self):
        return 2 * (self._width + self._length)
    
    def square(self):
        return self._width * self._length

    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width
    
    @length.setter
    def length(self, length):
        if length > 0:
            self._length = length
        else:
            raise ValueError('Lenght below zero is not allowed.')

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError('Width below zero is not allowed.')
        
    
if __name__ == '__main__':
    rectangle1 = Rectangle(1, 5)
    # rectangle1.length = 23

    print(f'{rectangle1.perimeter() = }')
    print(f'{rectangle1.square() = }')
    