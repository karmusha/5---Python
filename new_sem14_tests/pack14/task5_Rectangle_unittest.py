# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, 
# а также вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр. 
# Напишите 3-7 тестов unittest для данного класса.

import unittest
from task1 import str_replace

    # >>> str_replace('hello world')
    # 'hello world'
    # >>> str_replace('HELLO world')
    # 'hello world'
    # >>> str_replace('hello world!!!')
    # 'hello world'
    # >>> str_replace('helloй world')
    # 'hello world'
    # >>> str_replace('HELLOй world!!!')
    # 'hello world'

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

class TestStringReplace(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(3, 5)

    def test_perimeter(self):
        self.assertEqual(Rectangle(3, 5).perimeter(), self.rectangle.perimeter())

    def test_square(self):
        self.assertEqual(Rectangle(3, 5).square(), self.rectangle.square())

    
if __name__ == '__main__':
    unittest.main(verbosity=2)