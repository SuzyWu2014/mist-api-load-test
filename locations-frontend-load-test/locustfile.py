from locust import HttpLocust, TaskSet, task
from utils import *
import random


class UserBehavior(TaskSet):

    def on_start(self):
        self.token = getAccessToken()
        self.location_ids = getLocationIds()


    @task(1)
    def getLocationsByPage(self):
        page_num = random.choice(range(1, 28))
        url = "/v1/locations?page[number]=%d" % page_num
        self.client.get(url,
         name="getLocationsByPage",
         headers={'Authorization': self.token}
         )

    @task(2)
    def getLocationsById(self):
        url = "/v1/locations/"
        for param in self.location_ids:
            self.client.get(url + param,
             name="getLocationsById",
             headers={'Authorization': self.token}
             )

class ApiUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 100
    max_wait = 5000
