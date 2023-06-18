def check_value():
    number = None
    while True:
        try:
            number = int(input('Введите год: '))
            if number < 0:
                raise ValueError
        except ValueError:
            print("Ошибка ввода числа")
            continue
        except Exception:
            print("Что-то пошло не так")
            continue
        break
    return number


year = check_value()
gregorian, four, hundred, four_hundred = 1582, 4, 100, 400

if year < gregorian or year % four != 0 or year % hundred == 0 and year % four_hundred != 0:
    print('Обычный')
else:
    print('Високосный')
