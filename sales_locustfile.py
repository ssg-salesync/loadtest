from locust import HttpUser, task, between, constant

class SalesUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_sales(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "",
            "X-CSRF-TOKEN": ""
            }
        self.client.get('/sales/', headers=headers)

    @task
    def post_sale(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "",
            "X-CSRF-TOKEN": ""
            }
        data = {
            'table_no': 1,
            'total_price': 50.0,
            'payment_type': 'card'
        }
        self.client.post('/sales/', json=data, headers=headers)



    @task
    def get_daily_sales(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "",
            "X-CSRF-TOKEN": ""
            }
        params = {'store_id': 1, 'date': '2022-01-23'}  # replace with valid values
        self.client.get('/sales/daily', params=params, headers=headers)

    @task
    def get_period_sales(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "",
            "X-CSRF-TOKEN": ""
            }
        params = {'store_id': 1, 'start': '2022-01-01', 'end': '2022-01-31'}  # replace with valid values
        self.client.get('/sales/period', params=params, headers=headers)

