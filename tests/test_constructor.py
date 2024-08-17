import allure

from data import Massage


@allure.suite('Проверка на функции Конструктора')
class TestConstructor:
    @allure.title('Проверка кнопки "Конструктор"')
    def test_constructor_button(self, driver, constructor_page):
        constructor_page.full_check_constructor_page()
        assert (constructor_page.find_burger_panel().is_displayed()
                and constructor_page.find_bun().is_displayed())

    @allure.title('Проверка кнопки "Лента заказов"')
    def test_feed_orders(self, driver, constructor_page):
        constructor_page.find_and_click_feed_orders()
        assert constructor_page.find_window_feed_order().is_displayed()


@allure.suite('Проверки на работу с Ингредиентами')
class TestIngredients:
    @allure.title('Проверка открытия окна с информацией об ингредиенте "Флюоресцентная булка R2-D3"')
    def test_ingredients_bun(self, driver, constructor_page):
        constructor_page.full_check_open_window_info_bun()
        assert constructor_page.find_and_check_window_info().is_displayed()
        constructor_page.find_and_click_modal_close_button()
        assert constructor_page.find_burger_panel().is_displayed()

    @allure.title('Проверка открытия окна с информацией об ингредиенте "Соус Spicy"')
    def test_ingredients_sauce(self, driver, constructor_page):
        constructor_page.full_steps_open_window_info_sauce()
        assert constructor_page.find_and_check_window_info().is_displayed()
        constructor_page.find_and_click_modal_close_button()
        assert constructor_page.find_burger_panel().is_displayed()

    @allure.title('Проверка открытия окна с информацией об ингредиенте "Говяжий метеорит (отбивная)"')
    def test_ingredients_filling(self, driver, constructor_page):
        constructor_page.full_steps_open_window_info_filling()
        assert constructor_page.find_and_check_window_info().is_displayed()
        constructor_page.find_and_click_modal_close_button()
        assert constructor_page.find_burger_panel().is_displayed()

    @allure.title('Проверка счетчика ингредиентов')
    def test_check_count_ingredient(self, driver, constructor_page):
        constructor_page.transfer_ingredient()
        assert int(constructor_page.get_ingredient_counter()) > 0


@allure.suite('Проверка на Оформление заказа')
class TestPlaceOrderButton:
    @allure.title('Проверка кнопки "Оформить заказ"')
    def test_place_order_button(self, driver, constructor_page, user, login):
        constructor_page.find_and_click_button_place_order()
        assert constructor_page.find_window_order_confirm().is_displayed()
        assert constructor_page.find_text_order_confirm() == Massage.TEXT_ORDER_CONFIRM
