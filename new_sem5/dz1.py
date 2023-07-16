# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

full_path = 'C:/Users/karmu/Desktop/sales.txt'
                       

def get_file_path_name_ext(full_path) -> tuple:
    *path, name = path.rsplit('/', 1)
    return *path, *name.split('.')


print(get_file_path_name_ext(full_path))
