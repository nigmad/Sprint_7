import allure
import pytest

from data import DataColors


class TestCreateOrder:
    @pytest.mark.parametrize('color', [[DataColors.FIRST_COLOR], [DataColors.SECOND_COLOR]])
    @allure.title('Test Successful order creation with color BLACK or GREY')
    def test_success_order_select_one_color(self, generate_order_fixture, order_methods, color):
        order_body = generate_order_fixture
        order_body['color'] = color
        order = order_methods.create_order(order_body)
        assert order.status_code == 201
        response_json = order.json()
        assert 'track' in response_json

    @allure.title('Test Successful order creation with both BLACK and GREY color')
    def test_success_order_select_both_colors(self, generate_order_fixture, order_methods):
        order_body = generate_order_fixture
        order_body['color'] = [DataColors.FIRST_COLOR, DataColors.SECOND_COLOR]
        order = order_methods.create_order(order_body)
        assert order.status_code == 201
        response_json = order.json()
        assert 'track' in response_json

    @allure.title('Test Successful order creation without specifying color')
    def test_success_order_without_color(self, generate_order_fixture, order_methods):
        order_body = generate_order_fixture
        order_body.pop('color', None)
        order = order_methods.create_order(order_body)
        assert order.status_code == 201
        response_json = order.json()
        assert 'track' in response_json

    @allure.title('Test Successful order creation contains track in response body')
    def test_success_order_track_in_response(self, generate_order_fixture, order_methods):
        order_body = generate_order_fixture
        order = order_methods.create_order(order_body)
        assert order.status_code == 201
        track = order.json().get('track')
        assert order.json()['track'] == track






