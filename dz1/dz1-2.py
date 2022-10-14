# --- 2 ---
# # Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(0, 1):
    for y in range(0, 1):
        for z in range(0, 1):
            set_1 = not (x or y or z)
            set_2 = not x and not y and not z

if set_1 == set_2:
    print('Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат.')
else:
    print('Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z не истинно.')
