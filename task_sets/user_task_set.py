from locust import TaskSet, task
from helper.data_helper import DataHelper
from scenarios.user_scenarios import UserScenarios

class UserTaskSet(TaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.data_helper = DataHelper(self)
        self.user_scenarios = UserScenarios(self)

    @task(33)
    def get_user(self):
        user = self.data_helper.get_user()
        self.user_scenarios.get_user_info(user)

    @task(33)
    def post_create_user(self):
        user = self.data_helper.get_random_user()
        self.user_scenarios.post_create_user(user)