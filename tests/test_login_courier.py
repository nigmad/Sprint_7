import allure


class TestLoginCourier:
    @allure.title('Test Successful courier login')
    def test_login_courier(self, courier_methods, generate_courier_fixture):
        # Courier creation
        courier_data = generate_courier_fixture
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 201

        # Courier login
        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 200
        login_response_json = login_response.json()
        courier_id = login_response_json.get("id")
        assert courier_id
        # deletion for database clean up
        delete_response = courier_methods.delete_courier(courier_id)
        assert delete_response.status_code == 200

    @allure.title('Test login with missing login field')
    def test_login_missing_login(self, courier_methods, generate_courier_fixture):
        login_data = {
            "password": generate_courier_fixture["password"]
        }

        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 400
        response_json = login_response.json()
        assert response_json.get("message") == "Недостаточно данных для входа"

    @allure.title('Test login with missing password field')
    def test_login_missing_password(self, courier_methods, generate_courier_fixture):
        login_data = {
            "login": generate_courier_fixture["login"],
            "password": ""
        }

        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 400
        response_json = login_response.json()
        assert response_json.get("message") == "Недостаточно данных для входа"

    @allure.title('Test login with both login and password missing')
    def test_login_missing_both_fields(self, courier_methods):
        login_data = {
            "login": "",
            "password": ""
        }

        login_response = courier_methods.login_courier(login_data, timeout=10)

        assert login_response.status_code == 400
        response_json = login_response.json()
        assert response_json.get("message") == "Недостаточно данных для входа"

    @allure.title('Test login with empty field')
    def test_login_empty_field(self, courier_methods, generate_courier_fixture):
        fields_to_check = ['login', 'password']

        for field in fields_to_check:
            login_data = {key: generate_courier_fixture.get(key) if key != field else "" for key in fields_to_check}

            login_response = courier_methods.login_courier(login_data, timeout=10)

            assert login_response.status_code == 400

            response_json = login_response.json()
            assert response_json.get("message") == "Недостаточно данных для входа"

    @allure.title('Test login with non-existent user')
    def test_login_with_non_existent_user(self, courier_methods):

        login_data = {
            "login": "noneuser",
            "password": "0000"
        }

        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 404
        response_json = login_response.json()
        assert response_json.get("message") == "Учетная запись не найдена"


    @allure.title('Test successful login returns id')
    def test_successful_login_returns_id(self, courier_methods, generate_courier_fixture):
        courier_data = generate_courier_fixture
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 201

        # Courier login
        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 200
        login_response_json = login_response.json()
        courier_id = login_response_json.get("id")
        assert courier_id
        print(f"Courier ID: {courier_id}")

        # deletion for database clean up
        delete_response = courier_methods.delete_courier(courier_id)
        assert delete_response.status_code == 200
