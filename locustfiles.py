from locust import TaskSet, User, task, HttpUser, constant
from app.api import ApiRequests


class LoggedUser(HttpUser):
    min_wait = 5000
    max_wait = 60000

    tasks = {
        ApiRequests: 1,
    }
