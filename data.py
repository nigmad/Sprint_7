


class Url:
    BASE_URL = 'http://qa-scooter.praktikum-services.ru'
    COURIER_CREATE = '/api/v1/courier'
    COURIER_DELETE = '/api/v1/courier'
    COURIER_LOGIN = '/api/v1/courier/login'
    CREATE_ORDER = '/api/v1/orders'
    ORDER_LIST = '/api/v1/orders'


class ServerResponseMessage:
    COURIER_CREATED = {'ok': True}
    COURIER_CREATION_MISSING_FIELD = 'Недостаточно данных для создания учетной записи'
    LOGIN_ALREADY_USED = 'Этот логин уже используется'
    COURIER_DELETED = {'ok': True}
    COURIER_NOT_DELETED = 'Недостаточно данных для удаления курьера'
    COURIER_LOGIN = {'id': {id}}
    COURIER_LOGIN_MISSING_FIELD = 'Недостаточно данных для входа'
    COURIER_LOGIN_NONEXISTENT = 'Учетная запись не найдена'

    ORDER_CREATED = {'track': {id}}

    ORDER_LIST = {'orders': [{list}]}





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



class DataForAuth:
    CREATE_LOGIN_BODY = {
    "login": "agagaga",
    "password": "1234"
}

    EMPTY_FIELD = ""

    EMPTY_LOGIN_PASSWORD_BODY = {
        "login": "",
        "password": ""
    }

    NONEXISTENT_COURIER_BODY = {
            "login": "noneuser",
            "password": "0000"
        }

