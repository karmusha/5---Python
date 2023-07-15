# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
# Ключ словаря - загадка, значение - список с отгадками. 
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки. 


def guess_function(question: str, replies: list, attempts: int = 100):
    print(f'Отгадайте загадку:\n{question}\nУ вас {attempts} попыток.')

    for i in range(1, attempts+1):
        reply = input(f'Попытка номер {i}.\nВаш ответ: ').lower()
        if reply in replies:
            print(f'Ура! Вы угадали с {i} попытки')
            add_to_guess_dict(question, i, _guess_dict)
            return i
        else:
            print('Вы не угадали.')
            continue

    print('Попытки кончились, Вы не угадали.')
    return 0

def guess_function_main():
    quest = {
        '1': ['1', 'один', 'раз'],
        '2': ['2', 'два'],
        '3': ['3', 'три'],
    }
    for question, replies in quest.items():
        guess_function(question, replies, 3)

def show_dict():
    print(_guess_dict)

def add_to_guess_dict(question, try_no, guess_dict):
    _guess_dict.update({question: try_no})

_guess_dict = {}

if __name__ == '__main__':
    guess_function_main()
