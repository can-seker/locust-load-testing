from helper.data_helper import DataHelper

class UserScenarios:
    def __init__(self, task_set):
        self.task_set = task_set

    def get_user_info(self, user):
        self.task_set.client.get("/v2/user/"+user, name="/v2/user/")

    def post_create_user(self, user):
        self.task_set.client.post("/v2/user", name="/v2/user", json=DataHelper.post_user_create_payload(user))
