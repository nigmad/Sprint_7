import allure

from data import DataForCreateCourier, DataForAuth



class TestCreateCourier:
    @allure.title('Test Successful courier creation')
    def test_create_courier(self, courier_methods, generate_courier_fixture):
        # Courier creation
        courier_data = generate_courier_fixture
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 201

        # Courier deletion for database clean up
        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 200
        login_response_json = login_response.json()
        courier_id = login_response_json.get("id")
        assert courier_id
        delete_response = courier_methods.delete_courier(courier_id)
        assert delete_response.status_code == 200


    @allure.title('Test impossible to create two couriers with the same login')
    def test_create_duplicate_courier(self, courier_methods):
# Create first courier
        courier_data = DataForCreateCourier.CREATE_COURIER_BODY
        create_response_1 = courier_methods.create_courier(courier_data)
        assert create_response_1.status_code == 201
# Create second courier with the same data
        create_response_2 = courier_methods.create_courier(courier_data)
        assert create_response_2.status_code == 409
#Deletion for database cleanup
        login_data = DataForAuth.CREATE_LOGIN_BODY
        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 200

        login_response_json = login_response.json()
        courier_id = login_response_json.get("id")
        assert courier_id

        delete_response = courier_methods.delete_courier(courier_id)
        assert delete_response.status_code == 200



    @allure.title('Test creating courier without login field')
    def test_create_courier_without_login(self, courier_methods, generate_courier_fixture):
        courier_data = generate_courier_fixture
        del courier_data["login"]
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 400
        response_json = create_response.json()
        assert response_json.get("message") == "Недостаточно данных для создания учетной записи"
        # In case If the courier is created then we need to delete him from database
        if create_response.status_code == 201:
            courier_id = create_response.json().get("id")
            delete_response = courier_methods.delete_courier(courier_id)
            assert delete_response.status_code == 200


    @allure.title('Test creating courier without password field')
    def test_create_courier_without_password(self, courier_methods, generate_courier_fixture):
        courier_data = generate_courier_fixture
        del courier_data["password"]
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 400
        response_json = create_response.json()
        assert response_json.get("message") == "Недостаточно данных для создания учетной записи"
        # In case If the courier is created then we need to delete him from database
        if create_response.status_code == 201:
            courier_id = create_response.json().get("id")
            delete_response = courier_methods.delete_courier(courier_id)
            assert delete_response.status_code == 200

    @allure.title('Test creating courier without firstName field')
    def test_create_courier_without_firstName(self, courier_methods, generate_courier_fixture):
        courier_data = generate_courier_fixture
        del courier_data["firstName"]
        create_response = courier_methods.create_courier(courier_data)

        assert create_response.status_code == 400
        response_json = create_response.json()
        assert response_json.get("message") == "Недостаточно данных для создания учетной записи"

        if create_response.status_code == 201:
            courier_id = create_response.json().get("id")
            delete_response = courier_methods.delete_courier(courier_id)
            assert delete_response.status_code == 200




    @allure.title('Test Right response code for courier creation')
    def test_right_response_code_creation_courier(self, courier_methods, generate_courier_fixture):
        # Courier creation
        courier_data = generate_courier_fixture
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 201

        # Courier deletion for data base clean up
        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 200
        login_response_json = login_response.json()
        courier_id = login_response_json.get("id")
        assert courier_id
        delete_response = courier_methods.delete_courier(courier_id)
        assert delete_response.status_code == 200

    @allure.title('Test Right response body {"ok":true} for courier creation')
    def test_right_response_body_creation_courier(self, courier_methods, generate_courier_fixture):
        # Courier creation
        courier_data = generate_courier_fixture
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.json() == {"ok": True}

        # Courier deletion for database clean up
        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        login_response = courier_methods.login_courier(login_data, timeout=10)
        assert login_response.status_code == 200
        login_response_json = login_response.json()
        courier_id = login_response_json.get("id")
        assert courier_id
        delete_response = courier_methods.delete_courier(courier_id)
        assert delete_response.status_code == 200

