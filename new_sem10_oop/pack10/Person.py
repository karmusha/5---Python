# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор. 
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

class Person:

    def __init__(self, lname, fname, pname, age):
        self.lname = lname
        self.fname = fname
        self.pname = pname
        self.__age = age
    
    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.lname} {self.fname} {self.pname}'
    
if __name__ == '__main__':
    person1 = Person('Ivanov', 'Petr', 'Igorevich', 25)
    print(person1.full_name())
    person1.birthday()

    print(person1.__dict__)
