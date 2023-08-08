# Создайте функцию аналог get для словаря. 
# Помимо самого словаря функция принимает ключ и значение по умолчанию. 
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение. 
# Реализуйте работу через обработку исключений.

def get_value(mydict, key, value='Key not found.'):
    try:
        return mydict[key]
    except KeyError:
        return value
    
dirs = {
        'video': ['avi', 'mkv'],
        'text': ['txt', 'pdf', 'docx'],
        'image': ['jpeg', 'png'],
    }

print(get_value(dirs, 't'))
print(get_value(dirs, 'text'))
