from locust import HttpUser, between, task, tag
import random
import json

class MyUser(HttpUser):
    wait_time = between(1, 2)
    
    # 직접 입력할 토큰 값
    # access_token = ""
    # csrf_token = ""

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
            "Authorization": "",
            "X-CSRF-TOKEN": ""
        }

        response = self.client.post('/orders/', json=self.example_order, headers=headers)
        assert response.status_code == 200
        assert response.json()["result"] == "success"

    @task
    @tag("orders")
    def get_unpaids(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "",
            "X-CSRF-TOKEN": ""
        }

        response = self.client.get('/orders/unpaids', headers=headers)
        assert response.status_code == 200

    @task
    @tag("orders")
    def get_unpaids_by_table(self):
        table_no = random.randint(1, 8)  # 랜덤한 테이블 번호
        headers = {
            "Content-Type": "application/json",
            "Authorization": "",
            "X-CSRF-TOKEN": ""
        }

        response = self.client.get(f'/orders/unpaids/{table_no}', headers=headers)
        assert response.status_code == 200

   
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
