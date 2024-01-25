from locust import HttpUser, between, task, tag
import random
import json

class MyUser(HttpUser):
    wait_time = between(1, 2)
    
    # 직접 입력할 토큰 값
    # access_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0"
    # csrf_token = "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"

    # 예제 주문 데이터
    example_order = {
        "store_id": 1,
        "table_no": 1,
        "carts": [
            {"item_id": 1, "quantity": 1},
            {"item_id": 2, "quantity": 1}
        ]
    }

    @task
    @tag("orders")
    def create_order(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
            "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
        }

        response = self.client.post('/orders/', json=self.example_order, headers=headers)
        assert response.status_code == 200
        assert response.json()["result"] == "success"

    @task
    @tag("orders")
    def get_unpaids(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
            "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
        }

        response = self.client.get('/orders/unpaids', headers=headers)
        assert response.status_code == 200

    @task
    @tag("orders")
    def get_unpaids_by_table(self):
        table_no = random.randint(1, 8)  # 랜덤한 테이블 번호
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
            "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
        }

        response = self.client.get(f'/orders/unpaids/{table_no}', headers=headers)
        assert response.status_code == 200

    # @task
    # @tag("orders")
    # def pay_order(self):
    #     # 결제할 테이블 번호
    #     # table_no = random.randint(1, 8)
    #     table_no = 1
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTkwMDAzNSwianRpIjoiYzA4MzRiYjAtNmRmZC00MzczLTlmYTktM2Q5YmIyZjk4MTQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcwNTkwMDAzNSwiZXhwIjoxNzA4NDkyMDM1fQ.41qawHivs_LRtr9bwzC3Q4Lmkb4A2mYVnVtLqGPi4x0",
    #         "X-CSRF-TOKEN": "IjFkZGU0ZDhjZmQ2NGZmYzBmZWI5MWIxODA4NWRlOWEwODlkOTFjZTYi.Za34Aw.Jz9gu9h4gw0SQKymY8LctPB_PUI"
    #     }

    #     # 결제 요청 데이터
    #     pay_data = {
    #         "store_id": 1,
    #         "table_no": table_no
    #     }

    #     response = self.client.put('/orders/paid', json=pay_data, headers=headers)
    #     if response.status_code == 200:
    #         assert response.json()["result"] == "success"
    #         assert response.json()["table_no"] == table_no
    #     elif response.status_code == 400:
    #         assert response.json()["result"] == "failed"
    #         assert "존재하지 않는 주문" in response.json()["message"]
    #     else:
    #     # 다른 상태 코드가 반환된 경우 처리 방법을 추가해야 합니다.
    #         self.fail(f"Unexpected status code: {response.status_code}")

    @task
    @tag("orders")
    def get_orders_per_date(self):
        headers = {
            "Content-Type": "application/json",
        }

        params = {
            "store_id": 1,
            "date": "2024-01-25"
        }

        response = self.client.get('/orders/daily', params=params, headers=headers)
        assert response.status_code == 200

    @task
    @tag("orders")
    def get_sales_per_period(self):
        headers = {
            "Content-Type": "application/json",
        }

        params = {
            "store_id": 1,
            "start": "2024-01-25",
            "end": "2024-01-25"
        }

        response = self.client.get('/orders/period', params=params, headers=headers)
        assert response.status_code == 200
