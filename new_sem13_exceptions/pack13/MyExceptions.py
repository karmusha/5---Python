# Создайте класс с базовым исключением и дочерние классыисключения: 
# ошибка уровня, 
# ошибка доступа.


class BasicException(Exception):
    pass

class LevelException(BasicException):

    def __init__(self, user_level, admin_level):
        self.user_level = user_level
        self.admin_level = admin_level

    def __str__(self) -> str:
        return f"Access denied. User level {self.user_level} should be more than {self.admin_level}."

class AccessException(BasicException):

    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id

    def __str__(self) -> str:
        return f"Access denied. No user with name {self.user_name} or id {self.user_id}."

