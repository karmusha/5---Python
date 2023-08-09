# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты: 
# - возврат строки без изменений 
# - возврат строки с преобразованием регистра без потери символов 
# - возврат строки с удалением знаков пунктуации 
# - возврат строки с удалением букв других алфавитов 
# - возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import re
import doctest

def str_replace(text: str) -> str:
    """
    Удаляет из текста все символы кроме букв латинского алфавита и пробелов.
    :param text:
    :return:
    >>> str_replace('hello world')
    'hello world'
    >>> str_replace('HELLO world')
    'hello world'
    >>> str_replace('hello world!!!')
    'hello world'
    >>> str_replace('helloй world')
    'hello world'
    >>> str_replace('HELLOй world!!!')
    'hello world'
    """
    res = re.sub(r'[^a-zA-Z ]+', '', text)
    res = res.lower()
    return res

s = 'HELLOй world!!!'

print(str_replace(s))
doctest.testmod(verbose=True)

