import random

class DataTest:
    # Тестовый пользователь
    test_user = {
        "login": "TestUserBna",
        "password": "1qaz2wsx",
        "first_name": "bna"
    }
    # Неверные данные для логина под тестовым пользователем
    wrong_data_for_test_user = [
        {
            "login": "TestUserBna",
            "password": "",
            "first_name": "bna"
        },
        {
            "login": "",
            "password": "1qaz2wsx",
            "first_name": "bna"
        }
    ]

    bad_data_for_test_user = [
        {
            "login": "TestUserBna2",
            "password": "1qaz2wsx",
            "first_name": "bna"
        },
        {
            "login": "TestUserBna",
            "password": "1qaz2w",
            "first_name": "bna"
        }
    ]

    randomData = 'rand' + str(random.randint(100, 999))

    # Неполные данные
    incomplete_data = [
        {
            "login": randomData,
            "password": "",
            "firstName": "Иван"
        },
        {
            "login": "",
            "password": "123456",
            "firstName": "Петр"
        }
    ]

    # Верные данные
    right_data = {
        "login": randomData,
        "password": randomData,
        "firstName": "Иван"
    }

    # Данные для создания заказа
    new_order_data = [
        {"firstName": "Иван", "lastName": "Иванов", "address": "Москва г., ул.Потылиха, д.2, кв.8",
         "metroStation": "Третьяковская", "phone": "+7 903 123-45-67", "rentTime": 1, "deliveryDate": "2024-02-05",
         "comment": "-", "color": ["GREY"]},
        {"firstName": "Петр", "lastName": "Петров", "address": "Москва г., ул.Винокурова, д.2, кв.3",
         "metroStation": "Нахимовский проспект", "phone": "+7 901 890-12-34", "rentTime": 5, "deliveryDate": "2024-02-03",
         "comment": "-", "color": ["GREY","BLACK"]},
        {"firstName": "Сидор", "lastName": "Сидоров", "address": "Москва г., ул.Вавилова, д.1, кв.4",
         "metroStation": "Ленинский проспект", "phone": "+7 903 567-89-01", "rentTime": 3, "deliveryDate": "2024-02-03",
         "comment": "-", "color": []}
    ]