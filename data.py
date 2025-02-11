class Url:
    BASE_URL = 'http://qa-scooter.praktikum-services.ru'
    COURIER_CREATE = '/api/v1/courier'
    COURIER_LOGIN = '/api/v1/courier/login'
    CREATE_ORDER = '/api/v1/orders'
    ORDER_LIST = '/api/v1/orders'

class DataForOrder:
    CREATE_ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}


class DataForCreateCourier:
    CREATE_COURIER_BODY = {
    "login": "agagaga",
    "password": "1234",
    "firstName": "saske"
}


class DataForAuth:
    CREATE_LOGIN_BODY = {
    "login": "agagaga",
    "password": "1234"
}