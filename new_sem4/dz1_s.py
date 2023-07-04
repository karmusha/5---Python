# Создайте несколько переменных, заканчивающихся и не оканчивающихся на "s".
# Напишите функцию, которая при запуске заменяет содержимое переменных, оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

names = ['Ira', 'Elena', 'Petr']
companies = {'Nokia': [100, 500], 'Lowa': [800, 100], 'Ararat': [-800, 100],}
rate = [100_000, 110_000, 150_000]
a = 5
s = -10
cas, da, etuple = 1.01, 'ogogo', (2, 48)

def replace_vars_with_s_ending():
    z = list(map(lambda x : x if x[0] not in '_' else None, globals().keys()))
    print(z)
    for var_name in z:
        if var_name and len(var_name) > 1 and var_name[-1] == 's':
            replaced_var_name = var_name[:-1]
            globals()[replaced_var_name] = globals()[var_name]

            globals()[var_name] = None
            print(f'{replaced_var_name} = {globals()[replaced_var_name]}')

replace_vars_with_s_ending()

z = list(map(lambda x : x if x[0] not in '_' else None, globals().keys()))
print(z)