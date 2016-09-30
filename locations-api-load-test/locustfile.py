from locust import HttpLocust, TaskSet, task
from config import *


class UserBehavior(TaskSet):

    @task(1)
    def request_static_urls(self):
        urls = set(["/api/v0/locations/arcgis",
            "/api/v0/locations/combined",
            "/api/v0/locations/dining",
            "/api/v0/locations/extension"])
        for url in urls:
            self.client.get(url,
                verify=False,
                auth=(username, password)
                )


class ApiUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 9000
