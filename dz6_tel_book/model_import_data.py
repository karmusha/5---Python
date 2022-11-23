from pathlib import Path

path = Path(__file__)

last_name = ''
first_name = ''
patronymic_name = ''
tel = ''

def import_from_console():
    global last_name, first_name, patronymic_name
    global tel
    last_name, first_name, patronymic_name = tuple(map(str, input('Введите ФИО через пробел: ').split(' ')))
    tel = str(input('Введите телефон: '))
    yield last_name, first_name, patronymic_name, tel

def import_from_file(file):
    global last_name, first_name, patronymic_name
    global tel
    with open(file, mode='r', encoding='utf-8') as f:
        for line in f:
            last_name, first_name, patronymic_name, tel = tuple(map(str, line.split(' ')))
            tel = str(tel).strip('\n') # Удаляем \n из строки
            yield last_name, first_name, patronymic_name, tel

def add_data():
    global last_name, first_name, patronymic_name
    global tel
    where = input('Откуда вы хотите внести данные в телефонную книгу? Введите f, если из файла, или введите c, если из консоли: ')
    if where == 'f':
        file = input('Введите название файла, из которого хотите импортировать данные, с расширением. Файл должен располагаться в той же папке, что и текущий файл.\n')
        file = path.parent.joinpath(file)
        return import_from_file(file)
    if where == 'c':
        return import_from_console()

def add_to_txt():
    file_txt = path.parent.joinpath('tel_book.txt')
    with open(file_txt, mode='a', encoding='utf-8') as func:
        res = add_data()
        res = map(lambda x: ' '.join(x) + '\n', res)
        func.writelines(res)
        func.write('\n')
