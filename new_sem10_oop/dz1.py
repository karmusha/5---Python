# Доработаем задачи 5-6. Создайте класс-фабрику. 
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. 
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

import inspect
from pack10.Animal import Fish, Bird, Mammal

class Fabric:

    @classmethod
    def create_animal_from_type(cls, animal_type: type):
        res = inspect.getfullargspec(animal_type.__init__)
        res = dict(map(lambda arg: (arg, input(f'please input {arg}: ')), res.args[1:]))
        res = animal_type(**res)
        return res

if __name__ == '__main__':
    new_fish = Fabric.create_animal_from_type(Fish)
    print(f'You created: {type(new_fish).__name__}')
    print(new_fish.get_name())
    print(new_fish.get_special_info())

    new_bird = Fabric.create_animal_from_type(Bird)
    print(f'You created: {type(new_bird).__name__}')
    print(new_bird.get_name())
    print(new_bird.get_special_info())

    new_mammal = Fabric.create_animal_from_type(Mammal)
    print(f'You created: {type(new_mammal).__name__}')
    print(new_mammal.get_special_info())
    print(new_mammal.get_name())
