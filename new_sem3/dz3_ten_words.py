# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import re

s = ('pyclbr — Python module browser support\n'
    'Source code: Lib/pyclbr.py\n'
    'The pyclbr module provides limited information about the functions, classes, and methods defined in a Python-coded module. The information is sufficient to implement a module browser. The information is extracted from the Python source code rather than by importing the module, so this module is safe to use with untrusted code. This restriction makes it impossible to use this module with modules not implemented in Python, including all standard and optional extension modules.pyclbr.readmodule(module, path=None)\n'
    'Return a dictionary mapping module-level class names to class descriptors. If possible, descriptors for imported base classes are included. Parameter module is a string with the name of the module to read; it may be the name of a module within a package. If given, path is a sequence of directory paths prepended to sys.path, which is used to locate the module source code.\n'
    'This function is the original interface and is only kept for back compatibility. It returns a filtered version of the following.\n'
    'pyclbr.readmodule_ex(module, path=None)\n'
    'Return a dictionary-based tree containing a function or class descriptors for each function and class defined in the module with a def or class statement. The returned dictionary maps module-level function and class names to their descriptors. Nested objects are entered into the children dictionary of their parent. As with readmodule, module names the module to be read and path is prepended to sys.path. If the module being read is a package, the returned dictionary has a key "__path__" whose value is a list containing the package search path.\n'
    'New in version 3.7: Descriptors for nested definitions. They are accessed through the new children attribute. Each has a new parent attribute.\n'
    'The descriptors returned by these functions are instances of Function and Class classes. Users are not expected to create instances of these classes.\n'
    'Function Objects\n'
    'Class Function instances describe functions defined by def statements. They have the following attributes:\n'
    'Function.file\n'
    'Name of the file in which the function is defined.\n'
    'Function.module\n'
    'The name of the module defining the function described.\n'
    'Function.name\n'
    'The name of the function.\n'
    'Function.lineno\n'
    'The line number in the file where the definition starts.\n'
    'Function.parent\n'
    'For top-level functions, None. For nested functions, the parent.\n'
    'New in version 3.7.\n'
    'Function.children\n'
    'A dictionary mapping names to descriptors for nested functions and classes.\n'
    'New in version 3.7.\n'
    'Function.is_async\n'
    'True for functions that are defined with the async prefix, False otherwise.\n'
    'New in version 3.10.\n'
    'Class Objects\n'
    'Class Class instances describe classes defined by class statements. They have the same attributes as Functions and two more.\n'
    'Class.file\n'
    'Name of the file in which the class is defined.\n'
    'Class.module\n'
    'The name of the module defining the class described.\n'
    'Class.name\n'
    'The name of the class.\n'
    'Class.lineno\n'
    'The line number in the file where the definition starts.\n'
    'Class.parent\n'
    'For top-level classes, None. For nested classes, the parent.\n'
    'New in version 3.7.\n'
    'Class.children\n'
    'A dictionary mapping names to descriptors for nested functions and classes.\n'
    'New in version 3.7.\n'
    'Class.super\n'
    'A list of Class objects which describe the immediate base classes of the class being described. Classes which are named as superclasses but which are not discoverable by readmodule_ex() are listed as a string with the class name instead of as Class objects.\n'
    'Class.methods\n'
    'A dictionary mapping method names to line numbers. This can be derived from the newer children dictionary, but remains for back-compatibility.')

s2 = re.sub('[\d]+','', re.sub('[^\w]+',' ', s)) # Не учитываем знаки препинания и цифры.
s2 = s2.lower().split(' ') # Не учитываем регистр и разбиваем на список.
s2 = list(filter(lambda x: x != '', s2)) # Фильтруем список, убирая пустые значения

dictionary = {}
for word in s2: # Заносим все слова в словарь, где ключ - слово, значение - количество повторений этого слова в тексте.
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary.update({word: 1})

sorted_dictionary_by_values = sorted(dictionary.items(), key=lambda x:x[1], reverse=True) # Сортируем по убыванию по значениям
print(f'10 most used words in this text: {(list(map(lambda i: i[0], sorted_dictionary_by_values)))[0:10]}') # И переносим первые 10 ключей из словаря в список.


