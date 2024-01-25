from locust import HttpUser, task, between, constant
import random

class ItemsUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_items(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
            "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
            }
        self.client.get('/categories/items', headers=headers)


    @task
    def post_item(self):
        headers = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
            "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
        }
        payload = {
            'name': f'New Item {random.randint(1, 4000)}',
            'price': 20.0
        }
        category_id = 1
        response = self.client.post(f'/categories/{category_id}/items', json=payload, headers=headers)
        assert response.status_code in [201, 409]


    # @task
    # def put_item(self):
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
    #         "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
    #         }
    #     item_id = 1  # replace with a valid item ID
    #     data = {
    #         'name': 'Updated Item',  # replace with a valid updated name
    #         'price': 25.0  # replace with a valid updated price
    #     }
    #     self.client.put(f'/categories/items/{item_id}', json=data, headers=headers)

    # @task
    # def delete_item(self):
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
    #         "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
    #         }
    #     item_id = 1  # replace with a valid item ID
    #     self.client.delete(f'/categories/items/{item_id}', headers=headers)

    
    @task
    def get_cost(self):
        params = {'store_id': 1}  # replace with a valid store ID
        self.client.get('/categories/items/costs', params=params)

    @task
    def post_cost(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
            "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
            }
        data = {
            'items': [
                {'item_id': 1, 'cost': 5.0},  # replace with valid item IDs and costs
                {'item_id': 2, 'cost': 7.0}
            ]
        }
        self.client.post('/categories/items/costs', json=data, headers=headers)

    # @task
    # def update_cost(self):
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
    #         "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
    #         }
    #     item_id = 1  # replace with a valid item ID
    #     data = {'cost': 6.0}  # replace with a valid updated cost
    #     self.client.put(f'/categories/items/costs/{item_id}', json=data, headers=headers)
