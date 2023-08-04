# Создайте класс-генератор. 
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step. 
# Если переданы два параметра, считаем step=1. 
# Если передан один параметр, также считаем start=1.

class GenFactorial:

    def __init__(self, start, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if stop is None:
            self.stop, self.start = self.start, 1

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.start <= self.stop:
            factorial = self._factorial(self.start)
            self.start += self.step
            return factorial
        raise StopIteration
    
    def _factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self._factorial(n-1)

if __name__ == '__main__':

    f = GenFactorial(8)
    for i in f:
        print(i)


    
