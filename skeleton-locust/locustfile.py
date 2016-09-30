from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task(2)
    def request_example1(self):
        urls = []
        for url in urls:
            self.client.get(url,
                    verify=False,
                    auth=("username", "password")
                    )

    @task(5)
    def request_example2(self):
        url = "https://example.com/"
        params = []
        token = ""
        for param in params:
            self.client.get(url + param,
             name=url,
             headers={'Authorization': token}
             )


class ApiUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000
