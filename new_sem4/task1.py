# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def unique_codes (string) -> list:
    unique_list = []
    for i in string:
        unique_list.append(ord(i))
    return sorted(unique_list, reverse=True)

string = input('Input text: ')
print(unique_codes(string))