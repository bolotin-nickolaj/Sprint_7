import allure
from api_scooter import ScooterApi
from url import Urls
from data import DataTest


class TestGetOrders:
    url_orders = Urls.order
    url_create_courier = Urls.courier_create
    url_login = Urls.courier_login
    url_accept = Urls.accept
    orderIds = []

    @allure.title("Получение списка заказов")
    @allure.description("Тестирование получения списка заказов")
    def test_is_order_list_exists(self):
        #Получение экземпляра класса доступа к API
        scooter_api = ScooterApi()
        #Получение тестовых данных (right_data = { "login": randomData, "password": randomData, "firstName": "Иван" })
        test_data = DataTest.right_data
        # Создание курьера
        response = scooter_api.post(self.url_create_courier, test_data)
        # Логин курьера
        response = scooter_api.post(self.url_login, test_data)
        # Получение ИД курьера
        courierId = response.json()["id"]

        for i in (0, 1, 2):
            # Заказ самоката данные
            response1 = scooter_api.post(self.url_orders, DataTest.new_order_data[i])
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
            # Поместить ИД заказa в список
            self.orderIds.append(orderId)

        # Получение url для списка заказов данного курьера. url по маске "/v1/orders?courierId={ИД курьера}"
        self.url_orders = Urls.order + "?courierId=" + str(courierId)
        # Получение списка заказов данного курьера
        response4 = scooter_api.get(self.url_orders)
        # ИД одного из заказов из списка заказов
        newOrderId = response4.json()['orders'][0]['id']
        # Проверка: Один из ИД помещенных заказов равен ИД извлеченного заказа
        assert newOrderId in self.orderIds
