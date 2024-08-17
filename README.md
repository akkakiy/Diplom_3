# Дипломный проект курса "Инженер по тестированию: от новичка до автоматизатора"
## Задания по теме "UI-тестирование"

    UI-тесты на сервис Stellar Burgers. 
    Это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

## Файлы
    - locators/page_locators.py  -  файл с локаторами используемыми в проверках

    - page_object/  -  каталог с файлами методов
        - page_object/base_page.py  - файл с базовыми методы
        - page_object/constructor_page.py  -  файл с методами конструктора
        - page_object/feed_order_page.py  -  файл с методами ленты заказов
        - page_object/main_page.py  -  файл с методами главной страницы
        - page_object/profile_page.py  -  файл с методами личного кабинета

    - tests/  -  каталог с файлами  
        - tests/test_constructor.py  -  проверки конструктора
        - tests/test_feed_order.py  -  проверки ленты заказа
        - tests/test_profile_page.py  -  проверки личного кабинета
        - tests/test_recovery_pass.py  -  проверки изменения личных данных

    - tests/conftest.py  -  файл с фикстурами

    - data.py  -  файл с постоянными использукемыми в проверках
    - help.py  -  вспомогательные методы используемые в проверках
    - urls.py  -  файл с адресами страниц


## Команды

Запустить тесты

    pytest tests --alluredir=allure_results

Посмотреть веб отчет

    allure serve allure_results
