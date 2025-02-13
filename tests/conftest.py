import pytest

from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods
from generators import generate_order_body, register_new_courier


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
    courier_data = register_new_courier()
    return {
        "login": courier_data["login"],
        "password": courier_data["password"],
        "firstName": courier_data["firstName"]
    }



@pytest.fixture()
def cleanup_courier(request, generate_courier_fixture):

    login = generate_courier_fixture["login"]
    password = generate_courier_fixture["password"]


    def delete_courier_after_test():
        courier_id = CourierMethods().get_courier_id_by_login(login, password)
        CourierMethods().delete_courier(courier_id)

    request.addfinalizer(delete_courier_after_test)











