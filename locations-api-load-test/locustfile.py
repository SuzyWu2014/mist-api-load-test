from locust import HttpLocust, TaskSet, task
from config import *


class UserBehavior(TaskSet):

    @task(1)
    def request_static_urls(self):
        for url in URLS:
            self.client.get(url,
                verify=False,
                auth=(USERNAME, PASSWORD)
                )


class ApiUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 9000
