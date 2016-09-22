from locust import HttpLocust, TaskSet, task
from config import *


class UserBehavior(TaskSet):

    @task(1)
    def requests_static_urls(self):
        for url in static_urls:
            self.client.get(url, verify=False, auth=(
                username, password))


class ApiUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 9000
