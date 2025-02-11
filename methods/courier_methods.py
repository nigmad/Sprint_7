import requests
from data import Url

class CourierMethods:
    def create_courier(self, payload):
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_CREATE}', json=payload)


    def delete_courier(self, courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.COURIER_CREATE}/{courier_id}')

    def login_courier(self, login_data, timeout):
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_data, timeout=timeout)
        return response

    def get_courier_by_login(self, login):
        params = {'login': login}
        response = requests.get(f'{Url.BASE_URL}{Url.COURIER_LOGIN}/', params=params)
        if response.status_code == 200:
            couriers = response.json()
            if couriers and isinstance(couriers, list):
                return couriers[0]
