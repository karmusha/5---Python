# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число. 
# Обрабатывайте не числовые данные как исключения.

def get_number(text):
    while True:
        try:
            number = float(input(text))
        except ValueError:
            print(f'This is not the number: {text}. Please try again.')
        else:
            return int(number) if number.is_integer() else number

num = get_number('Input any number: ')
print(num)
