# Начальная сумма равна нулю.
# Допустимые действия: пополнить, снять, выйти
# Сумма попоплнения и снятия кратны 50 у.е.
# Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третьей операции пополнения или снятия начистяются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

import sys

def menu(amount):
    count = 0
    while True:
        try:
            print('---MENU---\n'
            '1 - Deposit\n'
            '2 - Withdraw\n'
            '3 - Exit\n')
            if amount > 5000000.00:
                amount -= amount * WEALTH_TAX_PERSENT / 100
                print(f'You paid wealth {WEALTH_TAX_PERSENT}% tax, now you have {amount} RUB\n------')
            else:
                print(f'You have {amount} RUB\n-----')
            choice = int(input('Choose action: '))
            match choice:

                case 1: # Пополнение
                    deposit = float(input('How much money do your want to deposit?\n'))
                    if deposit % MIN_DEPOSIT_OR_WITHDRAW == 0:
                        amount += deposit
                        count += 1
                    else:
                        print(f"Put another sum. It shoud be a multiple of {MIN_DEPOSIT_OR_WITHDRAW} RUB.")
                        continue

                case 2: # Снятие
                    min_amount = MIN_DEPOSIT_OR_WITHDRAW + MIN_WITHDRAW_RATE
                    if amount == 0:
                        print("You don't have money on your account.")
                        continue
                    if amount < min_amount:
                        print(f'You cannot dithdraw. You need at lease {min_amount} RUB on your account for this operation.')
                        continue

                    withdraw = float(input(f'How much do you want to withdraw? Use a multiple of {MIN_DEPOSIT_OR_WITHDRAW} RUB.\n'))
                    withdraw_fee = withdraw * PERSENT_FOR_WITHDRAW / 100 # Процент за снятие - 1,5% от суммы снятия
                    if  withdraw_fee < MIN_WITHDRAW_RATE: # но не менее 30
                        withdraw_fee = MIN_WITHDRAW_RATE
                    if  withdraw_fee > MAX_WITHDRAW_RATE: # и не более 600 у.е.
                        withdraw_fee = MAX_WITHDRAW_RATE
                    
                    max_amount = amount + withdraw_fee # Нельзя снять больше, чем на счёте (включая % за операцию)
                    if withdraw > max_amount:
                        print('You cannot withdraw more than you have on your account including withdrawal fee.\n'
                            f'You can withdraw maximum {max_amount} RUB.')
                        continue
                    if withdraw % MIN_DEPOSIT_OR_WITHDRAW == 0:
                        print(f'You have withdrawed {withdraw} RUB.\n'
                            f'Your comission for this operation is {withdraw_fee} RUB.')
                        amount -= withdraw + withdraw_fee
                        count += 1
                    else:
                        print(f"Put another sum. It shoud be a multiple of {MIN_DEPOSIT_OR_WITHDRAW} RUB.")
                        continue

                case 3: # Выход
                    print('Goodbye!')
                    sys.exit()
                case _: # Выход
                    print('Try another choice.\n')
                    continue
            if count == 3:
                print(f'You have got {THREE_PERSENT}% comissions ({amount * THREE_PERSENT / 100} RUB) onto your account\n-----')
                amount += amount * THREE_PERSENT / 100
                count = 0
        except ValueError:
            print('You can input numbers only.\nTry again.')
            continue
        except Exception:
            print('Something wend wrong.\nTry again.')
            continue
            


MIN_DEPOSIT_OR_WITHDRAW = 50.0 # Сумма попоплнения и снятия кратны 50 у.е.
PERSENT_FOR_WITHDRAW = 1.5 # Процент за снятие - 1,5% от суммы снятия
MIN_WITHDRAW_RATE = 30.0 # но не менее 30 и не более 600 у.е.
MAX_WITHDRAW_RATE = 600.0 # и не более 600 у.е.
WEALTH_TAX_PERSENT = 10.0 # При превышении суммы в 5 млн вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
THREE_PERSENT = 3.0 # После каждой третьей операции пополнения или снятия начистяются проценты - 3%

amount = 0.0
menu(amount)
