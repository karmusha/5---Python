import pytest
from Tasks import Tasks
  
def test_find_average():
    assert Tasks.find_average([10, 20, 30, 40, 50]) == 30
    assert Tasks.find_average([]) == 0
    assert Tasks.find_average([5]) == 5

    with pytest.raises(TypeError):
        Tasks.find_average('Not a list')

def test_compare_two_avgs():
    num1 = [1, 2, 3, 4, 5]
    num2 = [10, 20, 30, 40, 50]
    num3 = [50, 40, 30, 20, 10]
    assert Tasks.compare_two_avgs(num2, num1) == 'Первый список имеет большее среднее значение', 'Test 1 failed'
    assert Tasks.compare_two_avgs(num1, num3) == 'Второй список имеет большее среднее значение', 'Test 2 failed'
    assert Tasks.compare_two_avgs(num2, num3) == 'Средние значения равны', 'Test 3 failed'
    assert Tasks.compare_two_avgs(num1, []) == 'Первый список имеет большее среднее значение', 'Test 4 failed'

    with pytest.raises(TypeError):
        Tasks.compare_two_avgs(num1, 'Not a list')

if __name__ == '__main__':
    pytest.main(['-v'])
