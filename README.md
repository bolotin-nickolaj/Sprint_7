# Sprint_7
## Тестирование API учебного сервиса Яндекс.Самокат
## Описание проекта

Адрес сервиса: https://qa-scooter.praktikum-services.ru/

Документация сервиса: https://qa-scooter.praktikum-services.ru/docs/

Описание тестов:

| Наименование файла         | Наименование теста | Описание теста        |
|:---------------------------|:-------------------|:----------------------|
| test_new_order.py          |test_is_track_exists | Создание заказа  |
| test_get_list_of_orders.py |test_is_order_list_exists|Получение списка заказов|
| test_create_new_courier.py |test_new_courier_create|Регистрация нового курьера. Данные правильные. Регистрация успешная.|
| test_create_new_courier.py |test_cannot_create_two_identical_couriers|Создание нового курьера с данными уже созданного курьера.
| test_create_new_courier.py |test_need_to_pass_all_required_fields|Регистрация нового курьера без обязательных полей возвращает ошибку|
| test_create_new_courier.py |test_register_success|Успешная регистрация|
| test_create_new_courier.py |test_cannot_create_courier_with_existing_login|Регистрация курьера с существующим логином вернет ошибку|
| test_courier_login.py      |test_login_with_incomplete_data|Авторизация с неполными данными|
| test_courier_login.py      |test_login_with_bad_data|Авторизация с неверными данными|
| test_courier_login.py      |test_success_login|Успешная авторизация|
