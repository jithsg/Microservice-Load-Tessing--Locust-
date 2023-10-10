from locust import HttpUser, task, between

class FruitUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_fruit(self):
        self.client.get("/")

