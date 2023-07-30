# Создайте класс Моя Строка, где:
# будут доступны все возможности str 
# дополнительно хранятся имя автора строки и время создания (time.time)

import time

class MyString(str):
    """Класс хранит имя автора строки и время создания."""

    def __new__(cls, value, author_name):
        instance = super().__new__(cls, value)
        instance.value = value
        instance.author_name = author_name
        instance.start_time = time.time()
        return instance
    
    def __str__(self):
        """Метод представления для пользователя с информацией об авторе, собственно строке и времени ее создания."""

        return f'Name: {self.author_name}, string: {self.value}, time: {self.start_time}'

    def __repr__(self):
        """Метод представления для разработчика для создания экземпляра из консоли в виде MyString(string, 'author_name')."""
        
        return f'MyString({self.value}, "{self.author_name}")'
    
    
s1 = MyString(1, 'Alex')
print(s1)
print(repr(s1))

print(f'Documentation:\n{MyString.__doc__}')
