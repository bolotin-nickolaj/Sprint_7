import pytest
import allure
from api_scooter import ScooterApi
from url import Urls
from data import DataTest

class TestNewOrder:

    url = Urls.order

    @allure.title("Создание заказа")
    @pytest.mark.parametrize('order_data', DataTest.new_order_data)
    def test_is_track_exists(self, order_data):
        scooter_api = ScooterApi()
        response = scooter_api.post(self.url, order_data)
        assert response.status_code == 201
        assert 'track' in response.text
