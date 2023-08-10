# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

from new_sem13_exceptions.pack13.Project import Project
from new_sem13_exceptions.pack13.User import User

import pytest

@pytest.fixture()
def res():
    return [User('Ira', '1', '1'), User('Vova', '2', '1'), \
                User('Mila', '3', '2'), User('Lena', '4', '3'), \
                User('Rita', '5', '3'), User('Petr', '6', '4'), \
                User('Gena', '7', '5'), User('Borya', '8', '5'), \
                User('Sergei', '9', '6'), User('Vasya', '10', '7'), User('Olga', '11', '7')]

def test_get_users_list_from_json(res):
    assert Project.get_users_list_from_json('users.json') == Project(res)


def test_add_user_not_initialized_admin(res: list):
    r = Project(res)
    with pytest.raises(AttributeError) as ex:
        r.add_user_to_list('Lara', '12', '7')
    
def test_delete_user_not_initialized_admin(res: list):
    r = Project(res)
    with pytest.raises(AttributeError) as ex:
        r.delete_user_from_list('Lara', '12', '7')
