import requests
from data import Url

class CourierMethods:
    def create_courier(self, payload):
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_CREATE}', json=payload)


    def delete_courier(self, courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.COURIER_DELETE}/{courier_id}')

    def login_courier(self, login_data, timeout):
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_data, timeout=timeout)
        return response


    def get_courier_id_by_login(self, login, password):
        login_data = {'login': login,
                  'password': password
                  }
        response = requests.get(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_data, timeout=10)
        if response.status_code == 200:
            response_json = response.json()
            courier_id = response_json.get('id')
            return courier_id



