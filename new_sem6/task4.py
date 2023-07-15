# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

# Создайте пакет с всеми модулями, которые вы создали за время занятия. 
# Добавьте в __init__ пакета имена модулей внутри дандер __all__. 
# В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.

def _check_leap_year(year):
    return not year % 4 != 0 or year % 100 != 0 or year % 400 != 0

def task_date(date: str):
    day, month, year = map(int, date.split('.'))
    if not 0 < year < 10000 or not 0 < month < 13 or not 0 < day < 32:
        return False
    if month not in [4, 6, 9, 11] and day > 30:
        return False
    
    leap = _check_leap_year(year)
    if leap and month == 2 and day > 29:
        return False
    if not leap and month == 2 and day > 28:
        return False
    return True

max_day = 0

dmy = input('Input date im format DD.MM.YYYY: ')

print(task_date(dmy))