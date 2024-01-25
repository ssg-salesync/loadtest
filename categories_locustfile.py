from locust import HttpUser, between, task
import random

class MyUser(HttpUser):
    wait_time = between(1, 2)
    
    # access_token = ""
    # csrf_token = ""
    
    @task
    def get_categories(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "",
            "X-CSRF-TOKEN": ""
        }
        response = self.client.get('/categories/', headers=headers)
        assert response.status_code == 200
        assert 'categories' in response.json()
        assert 'store_id' in response.json()

    @task
    def post_category(self):
        headers = {
            'Content-Type': 'application/json',
            "Authorization": "",
            "X-CSRF-TOKEN": ""
        }
        payload = {
            'name': f'New Category {random.randint(1, 4000)}',
        }
        response = self.client.post('/categories/', json=payload, headers=headers)
        assert response.status_code in [201, 409]

   


