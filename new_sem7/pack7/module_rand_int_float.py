from random import randint, uniform

START, END = -100, 100


def rand_int_float(file_name, lines_number):
    with open(file_name, mode='a', encoding='utf-8') as f:
        for _ in range(lines_number):
            f.write(f'{randint(START, END)}:{uniform(START, END)}\n')


if __name__ == '__main__':
    rand_int_float('new_sem7.txt', 5)