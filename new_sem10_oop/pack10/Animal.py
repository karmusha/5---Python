# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Animal:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f'Имя: {self.name}'

class Fish(Animal):

    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_special_info(self):
        return f'Глубина обитания: {self.depth} м'


class Bird(Animal):

    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings
    
    def get_special_info(self):
        return f'Размах крыльев: {self.wings} м'


class Mammal(Animal):

    def __init__(self, name, coat):
        super().__init__(name)
        self.coat = coat
    
    def get_special_info(self):
        return f'Длина шерсти: {self.coat} мм'
    

if __name__ == '__main__':
    fish = Fish('Neo', 10)
    bird = Bird('Woody', 3)
    mammal = Mammal('Bunny', 6)

    print(fish.get_name())
    print(fish.get_special_info())

    print(bird.get_name())
    print(bird.get_special_info())
    
    print(mammal.get_name())
    print(mammal.get_special_info())