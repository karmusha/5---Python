# Доработаем задачи 3 и 4. Создайте класс Project, содержащий артибуты - список пользователей проекта и админ проекта.
# Класс имеет следующие методы: 
# - классовый метод загрузки данных из JSON файла (из 2 задачи 8го семинара) 
# - метод входа в систему - требует указать имя и id пользователя. Далее метод создаёт пользователя и проверяет,
#                           есть ли он в списке пользователей проекта. Если в списке его нет, то вызывается исключение доступа.
#                           Если пользователь присутсвует в списке пользователей проекта, то пользователь, который входит,
#                           получает его уровень доступа и становится администратором.
# - метод добавления пользователя в список пользователей. Если уровень пользователя меньше, чем ваш уровень, 
#                           вызывайте исключение уровня доступа.
# - метод удаления пользователя из списка пользователей проекта.
# - метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера.

import json
from MyExceptions import AccessException, LevelException
import User

class Project:

    def __init__(self, users_list=None):
        if users_list is None:
            self.users_list = []
        self.users_list = users_list
        self.admin = None        

    @classmethod
    def get_users_list_from_json(cls, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            my_dict = json.load(f, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
        users_list = []
        for level, users in my_dict.items():
            for user_id, name in users.items():
                user = User(name, user_id, level)
                users_list.append(user)
        return Project(users_list)

    def login(self):
        print('Provide your credentials to access: ')
        while True:
            try:
                name, level = input('Input user name: '), int(input('Input user ID: '))
                break
            except ValueError:
                print('Wrong name or level, try again.')

        user_to_check = User(name, level)
        # if user_to_check not in self.users_list:
        #     raise AccessExeption(user_to_check.name, user_to_check.id)
        for user in self.users:
            if user_to_check == user:
                self.admin = user_to_check
                print(f'{user_to_check} successfully logged in as admin!')
                break
        else:
            raise AccessException(user_to_check.name, user_to_check.user_id)

    def add_user_to_list(self, name, user_id, level):
        if level < self.admin.level:
            raise LevelException (level, self.admin.level)
        self.users_list.append(User(name, user_id, level))

    def delete_user_from_list(self, name, user_id, level):
        if level < self.admin.level:
            raise LevelException
        try:
            self.users_list.remove(User(name, user_id, level))
        except ValueError:
            print('No such user in the list.')

    def __enter__():
        pass
    
    def __exit__(self, ext_type, ext_value, traceback):
        self.file = open('users.json', 'w', encoding='utf-8')
        json.dump([repr(user) for user in self.users_list], self.file, ensure_ascii=False)
        self.file.close()
    
if __name__ == '__main__':
    pass
