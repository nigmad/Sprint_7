import allure
import data
from helper import modify_login_body_for_empty_fields


class TestLoginCourier:
    @allure.title('Test Successful courier login')
    def test_login_courier(self, courier_methods, generate_courier_fixture, cleanup_courier):
        courier_data = generate_courier_fixture
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 201
        assert create_response.json() == data.ServerResponseMessage.COURIER_CREATED

        login_response = courier_methods.login_courier(courier_data, timeout=10)
        assert login_response.status_code == 200
        login_response_json = login_response.json()
        courier_id = login_response_json.get("id")
        assert courier_id



    @allure.title('Test login with missing login field')
    def test_login_missing_login(self, courier_methods, generate_courier_fixture):
        login_data = {
            "login": data.DataForAuth.EMPTY_FIELD,
            "password": generate_courier_fixture["password"]
        }

        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 400
        response_json = login_response.json()
        assert response_json.get("message") == data.ServerResponseMessage.COURIER_LOGIN_MISSING_FIELD

    @allure.title('Test login with missing password field')
    def test_login_missing_password(self, courier_methods, generate_courier_fixture):
        login_data = {"login": generate_courier_fixture["login"],
        "password": data.DataForAuth.EMPTY_FIELD}

        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 400
        response_json = login_response.json()
        assert response_json.get("message") == data.ServerResponseMessage.COURIER_LOGIN_MISSING_FIELD

    @allure.title('Test login with both login and password missing')
    def test_login_missing_both_fields(self, courier_methods):
        login_data = data.DataForAuth.EMPTY_LOGIN_PASSWORD_BODY

        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 400
        response_json = login_response.json()
        assert response_json.get("message") == data.ServerResponseMessage.COURIER_LOGIN_MISSING_FIELD

    @allure.title('Test login with empty field')
    def test_login_empty_field(self, courier_methods, generate_courier_fixture):
        fields_to_check = ['login', 'password']
        modified_bodies = modify_login_body_for_empty_fields(fields_to_check, generate_courier_fixture)

        login_data_1 = modified_bodies[0]  # Данные с пустым логином
        login_response_1 = courier_methods.login_courier(login_data_1, timeout=10)
        assert login_response_1.status_code == 400
        response_json_1 = login_response_1.json()
        assert response_json_1.get("message") == data.ServerResponseMessage.COURIER_LOGIN_MISSING_FIELD

        login_data_2 = modified_bodies[1]  # Данные с пустым паролем
        login_response_2 = courier_methods.login_courier(login_data_2, timeout=10)
        assert login_response_2.status_code == 400
        response_json_2 = login_response_2.json()
        assert response_json_2.get("message") == data.ServerResponseMessage.COURIER_LOGIN_MISSING_FIELD

    @allure.title('Test login with non-existent user')
    def test_login_with_non_existent_user(self, courier_methods):
        login_data = data.DataForAuth.NONEXISTENT_COURIER_BODY
        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 404
        response_json = login_response.json()
        assert response_json.get("message") == data.ServerResponseMessage.COURIER_LOGIN_NONEXISTENT


    @allure.title('Test successful login returns id')
    def test_successful_login_returns_id(self, courier_methods, generate_courier_fixture, cleanup_courier):
        courier_data = generate_courier_fixture
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 201
        assert create_response.json() == data.ServerResponseMessage.COURIER_CREATED

        login_response = courier_methods.login_courier(courier_data, timeout=10)
        assert login_response.status_code == 200
        login_response_json = login_response.json()
        courier_id = login_response_json.get("id")
        assert courier_id




