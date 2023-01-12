from locust import HttpUser, between
from task_sets.user_task_set import UserTaskSet

class PetstoreUser(HttpUser):
    wait_time = between(1, 2)
    tasks = {
        UserTaskSet
}