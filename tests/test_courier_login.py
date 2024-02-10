import pytest
import allure
from api_scooter import ScooterApi
from url import Urls
from data import DataTest


class TestloginCourier:
    url = Urls.courier_login

    # для авторизации нужно передать все обязательные поля;
    # если какого-то поля нет, запрос возвращает ошибку;
    @allure.title("Авторизация с неполными данными")
    @allure.description("Возвращает ошибку")
    @pytest.mark.parametrize("wrong_data", DataTest.wrong_data_for_test_user)
    def test_login_with_incomplete_data(self, wrong_data):
        scooter_api = ScooterApi()
        response = scooter_api.post(self.url, wrong_data)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для входа"

    # система вернёт ошибку, если неправильно указать логин или пароль;
    # если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
    @allure.title("Авторизация с неверными данными")
    @allure.description("Возвращает ошибку")
    @pytest.mark.parametrize("wrong_data", DataTest.bad_data_for_test_user)
    def test_login_with_bad_data(self, wrong_data):
        scooter_api = ScooterApi()
        response = scooter_api.post(self.url, wrong_data)
        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"

    # курьер может авторизоваться;
    # успешный запрос возвращает id.
    @allure.title("Успешная авторизация")
    @allure.description("Возвращается ID курьера")
    def test_success_login(self):
        scooter_api = ScooterApi()
        response = scooter_api.post(self.url, DataTest.test_user)
        assert response.status_code == 200
        assert response.json() == {'id': 259058}
