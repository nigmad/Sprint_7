import allure
import data


class TestCreateCourier:
    @allure.title('Test Successful courier creation')
    def test_create_courier(self, courier_methods, generate_courier_fixture, cleanup_courier):
        courier_data = generate_courier_fixture
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 201
        assert create_response.json() == data.ServerResponseMessage.COURIER_CREATED


    @allure.title('Test impossible to create two couriers with the same login')
    def test_create_duplicate_courier(self, courier_methods, generate_courier_fixture, cleanup_courier):

        courier_data_1 = generate_courier_fixture
        create_response_1 = courier_methods.create_courier(courier_data_1)
        assert create_response_1.status_code == 201
        assert create_response_1.json() == data.ServerResponseMessage.COURIER_CREATED

        courier_data_2 = courier_data_1.copy()
        create_response_2 = courier_methods.create_courier(courier_data_2)
        assert create_response_2.status_code == 409
        assert create_response_2.json() == data.ServerResponseMessage.LOGIN_ALREADY_USED



    @allure.title('Test creating courier without login field')
    def test_create_courier_without_login(self, courier_methods, generate_courier_fixture, cleanup_courier):
        courier_data = generate_courier_fixture
        del courier_data["login"]
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 400
        response_json = create_response.json()
        assert response_json.get("message") == data.ServerResponseMessage.COURIER_CREATION_MISSING_FIELD


    @allure.title('Test creating courier without password field')
    def test_create_courier_without_password(self, courier_methods, generate_courier_fixture, cleanup_courier):
        courier_data = generate_courier_fixture
        del courier_data["password"]
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 400
        response_json = create_response.json()
        assert response_json.get("message") == data.ServerResponseMessage.COURIER_CREATION_MISSING_FIELD


    @allure.title('Test creating courier without firstName field')
    def test_create_courier_without_firstName(self, courier_methods, generate_courier_fixture, cleanup_courier):
        courier_data = generate_courier_fixture
        del courier_data["firstName"]
        create_response = courier_methods.create_courier(courier_data)

        assert create_response.status_code == 400
        response_json = create_response.json()
        assert response_json.get("message") == data.ServerResponseMessage.COURIER_CREATION_MISSING_FIELD




    @allure.title('Test Right response code for courier creation')
    def test_right_response_code_creation_courier(self, courier_methods, generate_courier_fixture, cleanup_courier):
        courier_data = generate_courier_fixture
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.status_code == 201


    @allure.title('Test Right response body {"ok":true} for courier creation')
    def test_right_response_body_creation_courier(self, courier_methods, generate_courier_fixture, cleanup_courier):
        courier_data = generate_courier_fixture
        create_response = courier_methods.create_courier(courier_data)
        assert create_response.json() == data.ServerResponseMessage.COURIER_CREATED



