"""The module tests the tasks of finding the avarage of the list
    and the comparing of avarages of two lists."""
import pytest
from Tasks import Tasks

def test_find_average():
    """Test function of finding the average of the list of numbers"""

    assert Tasks.find_average([10, 20, 30, 40, 50]) == 30
    assert Tasks.find_average([]) == 0
    assert Tasks.find_average([5]) == 5

    with pytest.raises(TypeError):
        Tasks.find_average('Not a list')

def test_compare_two_avgs():
    """Test function of finding the bigger average from two lists of numbers.
        Raises the TypeError, if the user input not a list."""

    num1 = [1, 2, 3, 4, 5]
    num2 = [10, 20, 30, 40, 50]
    num3 = [50, 40, 30, 20, 10]
    assert Tasks.compare_two_avgs(num2, num1) == 'Первый список имеет большее среднее значение'
    assert Tasks.compare_two_avgs(num1, num3) == 'Второй список имеет большее среднее значение'
    assert Tasks.compare_two_avgs(num2, num3) == 'Средние значения равны'
    assert Tasks.compare_two_avgs(num1, []) == 'Первый список имеет большее среднее значение'

    with pytest.raises(TypeError):
        Tasks.compare_two_avgs(num1, 'Not a list')

if __name__ == '__main__':
    pytest.main(['-v'])
