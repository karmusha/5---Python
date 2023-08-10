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

# Доработать класс Project
# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

import json
from new_sem13_exceptions.pack13.MyExceptions import AccessException, LevelException
from new_sem13_exceptions.pack13.User import User

class Project:

    def __init__(self, users_list=None):
        if users_list is None:
            self.users_list = []
        self.users_list = users_list
        self.admin = None        

    def __eq__(self, __value: object) -> bool:
        if self.users_list == __value.users_list and self.admin == __value.admin:
            return True

    @classmethod
    def get_users_list_from_json(cls, file_name: str):
        with open(file_name, 'r', encoding='utf-8') as f:
            my_dict: dict = json.load(f, object_hook=lambda d: {k: v for k, v in d.items()})
        users_list = []
        for level, users in my_dict.items():
            for user_id, name in users.items():
                user = User(name, user_id, level)
                users_list.append(user)
        print(users_list)
        return Project(users_list)

    def __enter__(self):
        print('Provide your credentials to access: ')
        while True:
            try:
                name, user_id, level = input('Input user name: '), input('Input user ID: '), input('Input user access level: ')
                break
            except ValueError:
                print('Wrong name or level, try again.')

        user_to_check = User(name, user_id, level)
        # if user_to_check not in self.users_list:
        #     raise AccessExeption(user_to_check.name, user_to_check.id)
        for user in self.users_list:
            if user_to_check == user:
                self.admin = user_to_check
                print(f'{user_to_check} successfully logged in as admin!')
                break
        else:
            raise AccessException(user_to_check.name, user_to_check.user_id)

    def add_user_to_list(self, name: str, user_id: str, level: str):
        if int(level) < int(self.admin.level):
            raise LevelException (level, self.admin.level)
        self.users_list.append(User(name, user_id, level))

    def delete_user_from_list(self, name: str, user_id: str, level: str):
        if int(level) < int(self.admin.level):
            raise LevelException(level, self.admin.level)
        try:
            self.users_list.remove(User(name, user_id, level))
        except ValueError:
            print('No such user in the list.')

    def __exit__(self, ext_type, ext_value, traceback):
        self.file = open('users_res.json', 'w', encoding='utf-8')
        json.dump([repr(user) for user in self.users_list], self.file, ensure_ascii=False) # Вот тут неправильно формируется словарь
        self.file.close()
    
if __name__ == '__main__':

    with Project.get_users_list_from_json('users.json') as p:
        p.add_user_to_list('Vika', '12', '3')
        p.add_user_to_list('Kostya', '13', '3')
        p.delete_user_from_list('Lena', '4', '3')
        print(p.users_list)
