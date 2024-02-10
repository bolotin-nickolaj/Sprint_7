import allure
from api_scooter import ScooterApi
from url import Urls
from data import DataTest


class TestGetOrders:
    url_orders = Urls.order
    url_create_courier = Urls.courier_create
    url_login = Urls.courier_login
    url_accept = Urls.accept
    created_order_id = 0

    @allure.title("Получение списка заказов")
    @allure.description("Тестирование получения списка заказов")
    def test_is_order_list_exists(self, register_new_courier_and_return_login_password):
        #Получение экземпляра класса доступа к API
        scooter_api = ScooterApi()
        # Создание курьера
        login_pass = register_new_courier_and_return_login_password
        test_data = {
            "login": login_pass[0],
            "password": login_pass[1],
            "firstName": login_pass[2]
        }
        # Логин курьера
        response = scooter_api.post(self.url_login, test_data)
        # Получение ИД курьера
        courierId = response.json()["id"]

        # Заказ самоката данные
        response1 = scooter_api.post(self.url_orders, DataTest.new_order_data[0])
        # Получение track-номера заказа
        track = response1.json()["track"]
        # Получение url по маске - "/v1/orders/track?t={track-номера заказа}"
        track_url = Urls.track + '?t=' + str(track)
        # Получение заказа по track-номеру
        response2 = scooter_api.get(url=track_url)
        # Получение ИД заказа
        orderId = response2.json()['order']['id']
        #  Создание данных для привязки курьера и заказа, создание url по маске "/v1/orders/accept/{ИД заказа}?courierId={ИД курьера}"
        self.url_accept = Urls.accept + str(orderId) + '?courierId=' + str(courierId)
        # Связывание заказа и курьера
        response3 = scooter_api.put(url=self.url_accept)
        #Запомнить ИД созданного заказа
        self.created_order_id = orderId

        # Получение url для списка заказов данного курьера. url по маске "/v1/orders?courierId={ИД курьера}"
        self.url_orders = Urls.order + "?courierId=" + str(courierId)
        # Получение списка заказов данного курьера
        response4 = scooter_api.get(self.url_orders)
        # ИД одного из заказов из списка заказов
        newOrderId = response4.json()['orders'][0]['id']
        # Проверка: ИД помещенного заказа равен ИД извлеченного заказа
        assert newOrderId == self.created_order_id
