import User

class Project:

    @staticmethod
    def get_users_list(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            my_dict = json.load(f, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
        users_list = []
        for level, users in my_dict.items():
            for user_id, name in users.items():
                user = User(name, user_id, level)
                users_list.append(user)
        return users_list