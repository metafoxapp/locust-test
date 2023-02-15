from locust import TaskSet, task, HttpUser
from common.auth import login


class AppSample(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        login(self.client)
        pass

    def on_stop(self):
        pass

    @task(1)
    def meta(self):
        pass
