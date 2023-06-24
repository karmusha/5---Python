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
    print('Menu:\n'
          '1 - Deposit\n'
          '2 - Withdraw\n'
          '3 - Exit')
    print(f'You have {amount} RUB')
    choice = int(input('Choose action: '))

    while True:
        match choice:
            case 1: 
                deposit = float(input('How much money do your want to deposit?'))
                amount += deposit
                continue
            case 2:
                min_amount = MIN_DEPOSIT_OR_WITHDRAW + MIN_WITHDRAW_RATE
                max_amount = amount + 1
                if amount == 0:
                    print("You don't have money on your account.")
                    continue
                if amount < min_amount:
                    print(f'You cannot dithdraw. You need at lease {min_amount} RUB on your account for this operation.')
                    continue
                withdraw = float(input('How much do you want to withdraw? Use a multiple of 50 RUB.'))
                if withdraw > max_amount:
                    print('You cannot withdraw more than you have on your account including withdrawal fee.\n'
                          f'You can withdraw maximum {max_amount} RUB.')
                    continue

                if withdraw // MIN_DEPOSIT_OR_WITHDRAW == 0:
                    
                    pass
                else:
                    pass
                    
            case 3:
                print('Goodbye!')
                sys.exit()
    
amount = 0.0
MIN_DEPOSIT_OR_WITHDRAW = 50
PERSENT_FOR_WITHDRAW = 1.5/100
MIN_WITHDRAW_RATE = 30
MAX_WITHDRAW_RATE = 600
WEALTH_TAX_PERSENT = 10 

menu(amount)
