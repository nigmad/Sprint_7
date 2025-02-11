import allure


class TestOrdersList:
    @allure.title('Test get orders list')
    def test_get_orders_list(self, order_methods):
        response = order_methods.get_order_list()
        assert response.status_code == 200
        response_json = response.json()
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)
        for order in response_json["orders"]:
            assert "id" in order


