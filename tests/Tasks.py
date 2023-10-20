class Tasks:
    # Задание 1
    @staticmethod
    def find_average(numbers):
        if not isinstance(numbers, list):
            raise TypeError("Input should be a list.")
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def compare_two_avgs(numbers1, numbers2):
        try:
            avg1 = Tasks.find_average(numbers1)
            avg2 = Tasks.find_average(numbers2)
        except TypeError:
            print(f'Input should be a list.') 
        
        if avg1 > avg2:
            return 'Первый список имеет большее среднее значение'
        if avg2 > avg1:
            return 'Второй список имеет большее среднее значение'
        if avg1 == avg2:
            return 'Средние значения равны'
