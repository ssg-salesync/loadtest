from locust import HttpUser, task, between, constant
import random

class ItemsUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_items(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "",
            "X-CSRF-TOKEN": ""
            }
        self.client.get('/categories/items', headers=headers)


    @task
    def post_item(self):
        headers = {
            'Content-Type': 'application/json',
            "Authorization": "",
            "X-CSRF-TOKEN": ""
        }
        payload = {
            'name': f'New Item {random.randint(1, 4000)}',
            'price': 20.0
        }
        category_id = 1
        response = self.client.post(f'/categories/{category_id}/items', json=payload, headers=headers)
        assert response.status_code in [201, 409]



    
    @task
    def get_cost(self):
        params = {'store_id': 1}  # replace with a valid store ID
        self.client.get('/categories/items/costs', params=params)

    @task
    def post_cost(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "",
            "X-CSRF-TOKEN": ""
            }
        data = {
            'items': [
                {'item_id': 1, 'cost': 5.0},  # replace with valid item IDs and costs
                {'item_id': 2, 'cost': 7.0}
            ]
        }
        self.client.post('/categories/items/costs', json=data, headers=headers)
