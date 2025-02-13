import requests
from data import Url

class OrderMethods:
    def create_order(self, body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER}', json=body)



    def get_order_list(self):
        response = requests.get(f'{Url.BASE_URL}{Url.ORDER_LIST}')
        return response


