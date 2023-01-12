import random

class DataHelper:
    def __init__(self, task_set):
        self.task_set = task_set

    @classmethod
    def post_user_create_payload(self, user):
        payload = {
            "id": random.randint(1000000, 10000000),
            "username": user,
            "firstName": "QA",
            "lastName": "User",
            "email": "qa@qa.com",
            "password": "QWERTY123",
            "phone": "905555555555",
            "userStatus": 1
        }
        f = open("data/users.txt", "a")
        f.write(user + "\n")
        return payload

    @classmethod
    def get_random_user(cls):
        return "userqa" + str(random.randint(1000000, 10000000))

    @classmethod
    def get_user(self):
        users = open('data/users.txt').read().splitlines()
        user = random.choice(users)
        return user
