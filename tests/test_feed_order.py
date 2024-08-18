import allure
import time


@allure.suite('Проверки ленты заказов')
class TestFeedOrder:
    @allure.title('Проверка открытия окна с информацией о заказе')
    def test_open_feed_order(self, driver, feed_order_page):
        feed_order_page.full_steps_open_order_window_info()
        assert (feed_order_page.find_window_info_order().is_displayed()
                and feed_order_page.find_text_compound().is_displayed())

    @allure.title('Проверка поиска номера заказа в Ленте заказов')
    def test_find_number_order_in_feed_orders(self, driver, feed_order_page, user, login):
        feed_order_page.full_find_and_transfer_ingredient_bun()
        feed_order_page.wait_find_modal_window()
        feed_order_page.wait_station_text()
        feed_order_page.find_exit()
        feed_order_page.get_number_order_modal_window()
        feed_order_page.click_exit()
        feed_order_page.find_and_click_button_account()
        feed_order_page.find_and_click_button_history_order()
        number_order = feed_order_page.get_number_order_in_history_orders()
        assert number_order in feed_order_page.get_number_order_in_feed_orders_history()

    @allure.title('Проверка счетчика выполненых заказов за все время в Ленте заказов')
    def test_counter_up_all_time(self, driver, feed_order_page, user, login):
        feed_order_page.find_and_click_feed_order_button()
        all_time_before = feed_order_page.get_text_done_all_time()
        feed_order_page.find_and_click_constructor_button()
        feed_order_page.find_bun_button()
        feed_order_page.find_bun()
        feed_order_page.transfer_ingredient_bun()
        feed_order_page.find_and_click_button_place_order()
        feed_order_page.wait_find_modal_window()
        feed_order_page.find_exit()
        feed_order_page.get_number_order_modal_window()
        feed_order_page.click_exit()
        feed_order_page.find_and_click_feed_order_button()
        all_time_after = feed_order_page.get_text_done_all_time()
        assert all_time_before < all_time_after

    @allure.title('Проверка счетчика выполненых заказов за день в Ленте заказов')
    def test_counter_up_daily(self, driver, feed_order_page, user, login):
        feed_order_page.find_and_click_feed_order_button()
        daily_before = feed_order_page.get_text_done_daily()
        feed_order_page.find_and_click_constructor_button()
        feed_order_page.find_bun_button()
        feed_order_page.find_bun()
        feed_order_page.transfer_ingredient_bun()
        feed_order_page.find_and_click_button_place_order()
        feed_order_page.wait_find_modal_window()
        feed_order_page.find_exit()
        feed_order_page.get_number_order_modal_window()
        feed_order_page.click_exit()
        feed_order_page.find_and_click_feed_order_button()
        daily_after = feed_order_page.get_text_done_daily()
        assert daily_before < daily_after

    @allure.title('Проверка отображения номера заказа в разделе "В работе"')
    def test_order_in_works(self, driver, feed_order_page, user, login):
        feed_order_page.find_and_click_feed_order_button()
        feed_order_page.find_and_click_constructor_button()
        feed_order_page.find_bun_button()
        feed_order_page.find_bun()
        feed_order_page.transfer_ingredient_bun()
        feed_order_page.find_and_click_button_place_order()
        feed_order_page.wait_find_modal_window()
        feed_order_page.find_exit()
        number_order = feed_order_page.get_number_order_modal_window()
        feed_order_page.click_exit()
        feed_order_page.find_and_click_feed_order_button()
        feed_order_page.get_number_order_in_work()
        assert number_order in feed_order_page.get_number_order_in_work()
