# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import sys


def deposit(balance: float, transactions: list, **options) -> float:
    min = options['MIN_DEPOSIT_OR_WITHDRAW']
    deposit = float(input('How much money do your want to deposit?\n'))
    if deposit % min == 0:
        balance += deposit
        transactions.append(deposit)
        return balance
    print(f"Put another sum. It shoud be a multiple of {min} RUB.")
    return None

def withdrawal(balance: float, transactions: list, **options) -> float:
    min_dep = options['MIN_DEPOSIT_OR_WITHDRAW']
    min_wit_rate = options['MIN_WITHDRAW_RATE']
    max_wit_rate = options['MAX_WITHDRAW_RATE']
    persent = options['PERSENT_FOR_WITHDRAW']
    
    min_amount = min_dep + min_wit_rate
    if balance == 0:
        print("You don't have money on your account.")
        return None
    if balance < min_amount:
        print(f'You cannot dithdraw. You need at lease {min_amount} RUB on your account for this operation.')
        return None

    withdraw = float(input(f'How much do you want to withdraw? Use a multiple of {min_dep} RUB.\n'))
    withdraw_fee = withdraw * persent / 100 # Процент за снятие - 1,5% от суммы снятия
    if  withdraw_fee < min_wit_rate: # но не менее 30
        withdraw_fee = min_wit_rate
    if  withdraw_fee > max_wit_rate: # и не более 600 у.е.
        withdraw_fee = max_wit_rate

    max_amount = balance + withdraw_fee # Нельзя снять больше, чем на счёте (включая % за операцию)
    if withdraw > max_amount:
        print('You cannot withdraw more than you have on your account including withdrawal fee.\n'
            f'You can withdraw maximum {max_amount} RUB.')
        return None
    if withdraw % min_dep == 0:
        print(f'You have withdrawed {withdraw} RUB.\n'
            f'Your comission for this operation is {withdraw_fee} RUB.')
        balance -= withdraw + withdraw_fee
        transactions.append(withdraw)
        return balance
    
    print(f"Put another sum. It shoud be a multiple of {min_dep} RUB.")
    return None

def menu(options):
    balance = 0.0
    count = 0
    transactions: list = []
    
    while True:
        try:
            print('---MENU---\n'
            '1 - Deposit\n'
            '2 - Withdraw\n'
            '3 - Exit\n')
            if balance > 5000000.00:
                wealth = options['WEALTH_TAX_PERSENT']
                balance -= balance * wealth / 100
                print(f'You paid wealth {wealth}% tax, now you have {balance} RUB\n------')
            else:
                print(f'You have {balance} RUB\n-----')
            choice = int(input('Choose action: '))
            match choice:
                case 1: # Пополнение
                    res = deposit(balance, transactions, **options)
                    if not res:
                        continue

                    balance = res
                    count += 1
                case 2: # Снятие
                    res = withdrawal(balance, transactions, **options)
                    if not res:
                        continue

                    balance = res
                    count += 1
                case 3: # Выход
                    print(f'{transactions = }')
                    print('Goodbye!')
                    sys.exit()
                case _: # Выход
                    print('Try another choice.\n')
                    continue
            if count == 3:
                three_persent = options['THREE_PERSENT']
                print(f'You have got {three_persent}% comissions ({balance * three_persent / 100} RUB) onto your account\n-----')
                balance += balance * three_persent / 100
                count = 0
        except ValueError:
            print('You can input numbers only.\nTry again.')
            continue
        except Exception:
            print('Something wend wrong.\nTry again.')
            continue


menu({
'MIN_DEPOSIT_OR_WITHDRAW': 50.0, # Сумма попоплнения и снятия кратны 50 у.е.
'PERSENT_FOR_WITHDRAW': 1.5, # Процент за снятие - 1,5% от суммы снятия
'MIN_WITHDRAW_RATE': 30.0, # но не менее 30 и не более 600 у.е.
'MAX_WITHDRAW_RATE': 600.0, # и не более 600 у.е.
'WEALTH_TAX_PERSENT': 10.0, # При превышении суммы в 5 млн вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
'THREE_PERSENT': 3.0, # После каждой третьей операции пополнения или снятия начистяются проценты - 3%
})
