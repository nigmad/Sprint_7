import pytest

from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods
from generators import generate_order_body, register_new_courier_and_return_login_password


@pytest.fixture()
def order_methods():
    return OrderMethods()


@pytest.fixture()
def courier_methods():
    return CourierMethods()


@pytest.fixture()
def generate_order_fixture():
    order_body = generate_order_body()
    yield order_body


@pytest.fixture()
def generate_courier_fixture():
    courier_data = register_new_courier_and_return_login_password()
    return {
        "login": courier_data["login"],
        "password": courier_data["password"],
        "firstName": courier_data["firstName"]
    }







