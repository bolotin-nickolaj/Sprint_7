import pytest
import allure
from api_scooter import ScooterApi
from url import Urls
from data import DataTest


class TestCreateNewCourier:
    url = Urls.courier_create
    url_login = Urls.courier_login

    # курьера можно создать
    @allure.title("Регистрация нового курьера. Данные правильные. Регистрация успешная.")
    @allure.description("Создан новый курьер")
    def test_new_courier_create(self, register_new_courier_and_return_login_password):
        count = len(register_new_courier_and_return_login_password)
        assert count > 0

    # нельзя создать двух одинаковых курьеров
    @allure.title("Создание нового курьера с данными уже созданного курьера.")
    @allure.description("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_two_identical_couriers(self, register_new_courier_and_return_login_password):
        exists_courier_data = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1],
            "firstName": register_new_courier_and_return_login_password[2]
        }
        scooter_api = ScooterApi()
        response = scooter_api.post(self.url, exists_courier_data)
        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    # чтобы создать курьера, нужно передать в ручку все обязательные поля
    # если одного из полей нет, запрос возвращает ошибку
    @allure.title("Регистрация нового курьера без обязательных полей возвращает ошибку")
    @allure.description("Нельзя создать курьера с неполными данными")
    @pytest.mark.parametrize("incompleteData", DataTest.incomplete_data)
    def test_need_to_pass_all_required_fields(self, incompleteData):
        scooter_api = ScooterApi()
        response = scooter_api.post(self.url, incompleteData)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"


    # запрос возвращает правильный код ответа
    # успешный запрос возвращает {"ok":true}
    @allure.title("Успешная регистрация")
    @allure.description("Возвращается ответ True")
    def test_register_success(self):
        scooter_api = ScooterApi()
        response = scooter_api.post(self.url, DataTest.right_data)
        assert response.status_code == 201
        assert response.json() == {'ok': True}


    # если создать пользователя с логином, который уже есть, возвращается ошибка
    @allure.title("Регистрация курьера с существующим логином вернет ошибку")
    @allure.description("Нельзя создать курьера с существующим логином")
    def test_cannot_create_courier_with_existing_login(self, register_new_courier_and_return_login_password):
        exists_login_data = {
            "login": register_new_courier_and_return_login_password[0],
            "password": "159753",
            "firstName": "qqq"
        }
        scooter_api = ScooterApi()
        response = scooter_api.post(self.url, exists_login_data)
        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

