# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# Если число составное, то существует хотя бы один делитель, не превосходящий корень из этого числа.
class MaxNumberException(Exception):
    "Raised when the input value is more than MAX_NUMBER"
    pass

MAX_NUMBER = 100000

number = None
while True:
    try:
        number = int(input('Введите число от 0 до 100000: '))
        if number < 0:
            raise ValueError
        if number > MAX_NUMBER:
            raise MaxNumberException
    except ValueError:
        print("Отрицательные числа вводить нельзя.")
        continue
    except MaxNumberException:
        print(f"Числа больше {MAX_NUMBER} вводить нельзя.")
        continue
    except Exception:
        print("Что-то пошло не так")
        continue
    break

if number == 0 or number == 1:
    print(f'Число {number} не являeтся ни простыми, ни составными.')
    exit()

for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        print(f'Число {number} является составным')
        exit()
else: print(f'Число {number} является простым')