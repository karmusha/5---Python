# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты: 
# - возврат строки без изменений 
# - возврат строки с преобразованием регистра без потери символов 
# - возврат строки с удалением знаков пунктуации 
# - возврат строки с удалением букв других алфавитов 
# - возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import pytest

from task1 import str_replace

def test_1():
    assert str_replace('hello world') == 'hello world', 'Test 1 failed'

def test_2():
    assert str_replace('HELLO world') == 'hello world', 'Test 2 failed'

def test_3():
    assert str_replace('hello world!!!') == 'hello world', 'Test 3 failed'

def test_4():
    assert str_replace('helloй world') == 'hello world', 'Test 4 failed'

def test_5():
    assert str_replace('HELLOй world!!!') == 'hello world', 'Test 5 failed'
    
if __name__ == '__main__':
    pytest.main(['-v'])