# Создайте декоратор с параметром. 
# Параметр - целое число, количество запусков декорируемой функции.

def count(num):
    def deco(func):
        res = []
        def wrapper(*args, **kwargs):
            for i in range(1, num+1):
                res.append(func(*args, **kwargs))
                print(f'Fuc run {i} times.')
            return res
            # return [func(*args, **kwargs) for _ in range(num)]
        return wrapper
    return deco

if __name__ == '__main__':
    @count(4)
    def sum(a, b):
        return a + b

    print(sum(2, 2))
