# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списковархивов 
# list-архивы также являются свойствами экземпляра 

# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    """Класс Архив, который хранит пару свойств. Например, число и строку."""
    
    _instance = None

    def __new__(cls, *args):
        """pattern Singleton"""

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_numbers = []
            cls._instance.archive_strings = []
        else:
            cls._instance.archive_numbers.append(cls._instance.number)
            cls._instance.archive_strings.append(cls._instance.string)
        return cls._instance
            
    def __init__(self, number, string):
        self.number = number
        self.string = string

    def __str__(self):
        """for user"""

        return f'{self.number}, {self.string}, {self.archive_numbers}, {self.archive_strings}'
    
    def __repr__(self):
        """for developer"""

        return f'Archive({self.number}, "{self.string}")'
    

    
one = Archive(1, 'one')
print(one)
two = Archive(2, 'two')
print(two)
three = Archive(3, 'three')
print(three)
print(repr(one))

print(f'Documentation:\n{Archive.__doc__}')
help(Archive)
