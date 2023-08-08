# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7), сохраняя информацию в JSON файл. 
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра. 
# Реализуйте магический метод проверки на равенство пользователей.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

class Range:
    """Validates number from start to stop value."""

    def __init__(self, val, add=None):
        """Takes start and stop args. If no start was given, start = 0"""

        if add is None:
            self.start = 0
            self.stop = val
        else:
            self.start = val
            self.stop = add
    
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value, self.start, self.stop)
        return setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value: float, start, stop):
        if not start <= value <= stop:
            raise ValueError('Wrong value.')
        
class Range_Name:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    @staticmethod
    def validate(name: str):
        if name.isalpha:
            raise ValueError('Wrong name. All characters in the name are alphabetic and there is at least one character.')
        if name.title == name: 
            raise ValueError('Wrong name. Only the first letter should be capitalized.')


class User:

    name = Range_Name()
    user_id = Range(1, 7)

    def __init__(self, name, user_id, level):
        self.name = name
        self.user_id = user_id
        self.level = level
    
    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id
    
    def __repr__(self):
        return f'User({self.name}, {self.user_id}, {self.level})'
    
    def __str__(self):
        return f'Name: {self.name}, ID: {self.user_id}, access level: {self.level}'
    