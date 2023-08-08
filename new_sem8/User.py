import json

class User:

    def __init__(self, name, user_id, level):
        self.name = name
        self.user_id = user_id
        self.level = level
    
    def read_user():
        while True:
            try:
                with open('users.json', 'r', encoding='utf-8') as f:
                    users = json.load(f)
            except FileNotFoundError:
                users = {}
            user_id, level = None, None
            name = input('Input user name: ')
            is_valid_data = False
            while not is_valid_data:
                user_id, level = (i for i in input('Input spaced ID and LEVEL (1 to 7): ').split())
                if int(level) in range(1, 8):
                    if all(user_id not in v.keys() for k, v in users.items()):
                        is_valid_data = True
                    else:
                        print('ID already exists. Try again.')
                else:
                    is_valid_data = True
            if level not in users:
                users[level] = {}
            users[level][user_id] = name
            with open('users.json', 'w', encoding='utf-8') as f:
                json.dumps(users, f)
                print('User has been added.')

    def __str__(self):
        return f'Name: {self.name}, ID: {self.user_id}, access level: {self.level}'