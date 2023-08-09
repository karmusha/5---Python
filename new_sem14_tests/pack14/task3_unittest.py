# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты: 
# - возврат строки без изменений 
# - возврат строки с преобразованием регистра без потери символов 
# - возврат строки с удалением знаков пунктуации 
# - возврат строки с удалением букв других алфавитов 
# - возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
import unittest
from task1 import str_replace

    # >>> str_replace('hello world')
    # 'hello world'
    # >>> str_replace('HELLO world')
    # 'hello world'
    # >>> str_replace('hello world!!!')
    # 'hello world'
    # >>> str_replace('helloй world')
    # 'hello world'
    # >>> str_replace('HELLOй world!!!')
    # 'hello world'

class TestStringReplace(unittest.TestCase):

    def test_1(self):
        self.assertEqual(str_replace('hello world'), 'hello world')

    def test_2(self):
        self.assertEqual(str_replace('HELLO world'), 'hello world')

    def test_3(self):
        self.assertEqual(str_replace('hello world!!!'), 'hello world')

    def test_4(self):
        self.assertEqual(str_replace('helloй world'), 'hello world')

    def test_5(self):
        self.assertEqual(str_replace('HELLOй world!!!'), 'hello world')
    
if __name__ == '__main__':
    unittest.main(verbosity=2)