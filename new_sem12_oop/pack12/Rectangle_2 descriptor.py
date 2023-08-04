# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных). 
# Используйте декораторы свойств.
# Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Range:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value):
        if value <= 0: 
            raise ValueError('Lenght below zero is not allowed.')


class Rectangle:

    width = Range()
    length = Range() 
    
    def __init__(self, width, length=None):
        self.width = width
        if length is None:
            self.length = width
        else:
            self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)
    
    def square(self):
        return self.width * self.length
        
    
if __name__ == '__main__':
    rectangle1 = Rectangle(1)
    
    print(f'{rectangle1.perimeter() = }')
    print(f'{rectangle1.square() = }')
    