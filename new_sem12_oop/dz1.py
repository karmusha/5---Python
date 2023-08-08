# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.

# * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).

# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
import itertools

class Range_Note:
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
        
class Range:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    @staticmethod
    def validate(name: str):
        if name.isalpha and name.title == name: 
            raise ValueError('Wrong name.')

class Student:

    last_name = Range()
    fisrt_name = Range()
    middle_name = Range()
    test_note = Range_Note(100)
    note = Range_Note(2, 5)

    def __init__(self, last_name, first_name, middle_name):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        with open('lessons.csv', 'r', encoding='utf-8', newline='') as f:
            csv_file = csv.reader(f)
            lessons = []
            for line in csv_file:
                lessons.append(*line)
        self.lessons = lessons
        self.test_notes = {key: [] for key in self.lessons}
        self.all_notes = {key: [] for key in self.lessons}

        self.average_test_notes: dict = self.get_average_test_notes(self.test_notes)
        self.average_note: dict = self.get_average_note(self.all_notes)

    def add_note(self):
        lesson = Student.lesson_choice(self.lessons)
        self.note = int(input('Input note from 2 to 5: '))
        match self.all_notes.get(lesson):
            case None: self.all_notes.update({lesson: self.note})
            case value: value.append(self.note)
    

    def lesson_choice(list_of_lessons):
        Student.print_list_of_lessons(list_of_lessons)
        choice = int(input(f'Choose the number of the lesson: ')) # добавить обработку значений вне диапазона
        for num, lesson in enumerate(list_of_lessons, start=1):
            if choice == num:
                return lesson
        return ''
    

    def get_average_note(self, all_notes: dict):
        res: list = []
        if len(all_notes.values()) != 0:
            res = list(itertools.chain(*all_notes.values()))
        return Student.get_avg(res)


    def print_list_of_lessons(lessons):
        for num, val in enumerate(lessons, start=1): # добавить обработку пустые строчки
            print(f'{num} - {val}')

    def add_test_note(self):
        lesson = Student.lesson_choice(self.lessons)
        self.test_note = int(input('Input note from 0 to 100: '))
        match self.test_notes.get(lesson):
            case None: self.test_notes.update({lesson: self.test_note})
            case value: value.append(self.test_note)

    def get_average_test_notes(self, test_notes: dict):
        res = {}
        for key, value in test_notes.items():
            average_note = Student.get_avg(value)
            res.update({key: average_note})
        return res
        
    @staticmethod
    def get_avg(list_of_notes):
        if len(list_of_notes) == 0:
            return 0
        else:
            return sum(list_of_notes)/len(list_of_notes)


    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}:\n \
                test_notes = {self.test_notes},\n \
                all_notes = {self.all_notes},\n \
                средний балл по тестам = {self.get_average_test_notes(self.test_notes)},\n \
                средний балл по оценкам всех предметов = {self.get_average_note(self.all_notes)}'
    
    def __repr__(self) -> str:
        return self.__str__()



if __name__ == '__main__':
    s1 = Student('Ivanov', 'Ivan', 'Ivanovich')
    s1.add_test_note()
    s1.add_test_note()
    s1.add_test_note()
    s1.add_note()
    s1.add_note()
    s1.add_note()

    print(f'{s1 = }')