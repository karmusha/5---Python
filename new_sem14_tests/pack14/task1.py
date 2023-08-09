# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов. 
# Возвращается строка в нижнем регистре.

import re
import string

def str_replace(text: str) -> str:
    # res = ''.join(i for i in text if i in string.ascii_letters or i == ' ')
    res = re.sub(r'[^a-zA-Z ]+', '', text)
    res = res.lower()
    return res

s = '1-Hello world!'

print(str_replace(s))