# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

full_path = 'C:/Users/karmu/Desktop/sales.txt'
                       

def get_file_path_name_ext(full_path) -> tuple:
    temp_name, ext = full_path.split('.')
    path, name = temp_name.rsplit('/', 1)
    return path, name, ext


print(get_file_path_name_ext(full_path))
