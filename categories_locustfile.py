from locust import HttpUser, between, task
import random

class MyUser(HttpUser):
    wait_time = between(1, 2)
    
    # access_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0"
    # csrf_token = "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
    
    @task
    def get_categories(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
            "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
        }
        response = self.client.get('/categories/', headers=headers)
        assert response.status_code == 200
        assert 'categories' in response.json()
        assert 'store_id' in response.json()

    @task
    def post_category(self):
        headers = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
            "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
        }
        payload = {
            'name': f'New Category {random.randint(1, 4000)}',
        }
        response = self.client.post('/categories/', json=payload, headers=headers)
        assert response.status_code in [201, 409]

    # @task
    # def put_category(self):
    #     # 존재하는 카테고리 ID를 사용하여 수정하는 코드
    #     category_id = 5  # 수정할 카테고리 ID를 사용하도록 수정
    #     headers = {
    #         'Content-Type': 'application/json',
    #         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
    #         "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
    #     }
    #     payload = {
    #         'name': f'Modified Category {random.randint(1, 100)}',
    #     }
    #     response = self.client.put(f'/categories/{category_id}', json=payload, headers=headers)
    #     assert response.status_code in [201, 404, 409]

    # @task
    # def delete_category(self):
    #     # 존재하는 카테고리 ID를 사용하여 삭제하는 코드
    #     category_id = 5  # 삭제할 카테고리 ID를 사용하도록 수정
    #     headers = {
    #         'Content-Type': 'application/json',
    #         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
    #         "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
    #     }
    #     response = self.client.delete(f'/categories/{category_id}', headers=headers)
    #     assert response.status_code in [200, 404]


