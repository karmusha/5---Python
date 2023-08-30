# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. 
# Превратите функции в методы класса.
# Задачи должны решаться через вызов методов экземпляра.


from random import randint, sample

class RandomName:

    def random_name_to_file(self, file_name, lines_number):
        with open(file_name, mode='a', encoding='utf-8') as f:
            for _ in range(lines_number):
                f.write(f'{self.create_random_name()}\n')

    def create_random_name(self):
        vowels = 'aeiouy'
        cons = 'bcdfghjklmnpqrstvwxz'
        n1 = sample(vowels+cons, randint(4,8))
        name = ''.join(n1)
        if any(letter in name for letter in vowels):
            return name.capitalize()

if __name__ == '__main__':
    res = RandomName()
    res.random_name_to_file('new_sem77.txt', 3)
