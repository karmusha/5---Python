# Создайте класс Сотрудник. Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# - шестизначный идентификационный номер
# - уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from Person import Person

class Employee(Person):
    
    def __init__(self, lname, fname, pname, age, id):
        super().__init__(lname, fname, pname, age)
        self.id = id
        self.level = sum(int(i) for i in str(self.id)) % 7

    def id(self):
        return self.id

if __name__ == '__main__':
    worker = Employee('Lenkova', 'Irina', 'Osipovna', 30, 255255)
    print(worker.__dict__)
