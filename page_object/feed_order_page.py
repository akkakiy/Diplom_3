import allure

from locators.page_locators import HeadersPageLocators, FeedPageLocators, MainPageLocators, AccountPageLocators
from page_object.base_page import BasePage


@allure.suite('Методы на Ленту Заказов')
class FeedOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Поиск и клик по кнопке "Лента заказов" в верхнем меню')
    def find_and_click_feed_order_button(self):
        return self.find_element(HeadersPageLocators.FEED_ORDER_BUTTON).click()

    @allure.step('Поиск заказа в ленте')
    def find_order_in_feed_order(self):
        return self.find_element(FeedPageLocators.WINDOW_FEED_ORDER).click()

    @allure.step('Поиск окна с информацией о заказе')
    def find_window_info_order(self):
        return self.find_element(FeedPageLocators.WINDOW_INFO_ORDER_IN_WORK)

    @allure.step('Поиск информации с номером заказа')
    def find_text_compound(self):
        return self.find_element(FeedPageLocators.NUMBER_ORDER)

    @allure.step('Полные шаги для открытия окна с информацией о заказе')
    def full_steps_open_order_window_info(self):
        self.find_and_click_feed_order_button()
        self.find_order_in_feed_order()

    @allure.step('Поиск ингредиента "Флюоресцентная булка R2-D3"')
    def find_bun(self):
        return self.find_element(MainPageLocators.BUN)

    @allure.step('Перетаскивание ингредиента "Флюоресцентная булка R2-D3" в корзину')
    def transfer_ingredient_bun(self):
        self.drag_and_drop(MainPageLocators.BUN, MainPageLocators.BURGER_BASKET)

    @allure.step('Поиск и нажатие кнопки "Оформить заказ"')
    def find_and_click_button_place_order(self):
        return self.find_element(MainPageLocators.BUTTON_PLACE_ORDER).click()

    @allure.step('Поиск окна подтверждения принятия заказа')
    def wait_find_modal_window(self):
        return self.find_element(MainPageLocators.MODAL_WINDOW_CONFIRM)

    # @allure.step('Поиск текста в окне оформления заказа')
    # def wait_station_text(self):
    #     return self.find_element(FeedPageLocators.STATION_TEXT_IN_WIN_INFO)

    @allure.step('Поиск и клик по кнопке "Личный кабинет" в верхнем меню')
    def find_and_click_button_account(self):
        return self.find_element(HeadersPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    @allure.step('Поиск и клик по кнопке "История заказов" в личном кабинете')
    def find_and_click_button_history_order(self):
        return self.find_element(AccountPageLocators. HISTORY_BUTTON).click()

    @allure.step('Поиск информации о номере заказа в Личном кабинете')
    def get_number_order_in_history_orders(self):
        return self.get_text(AccountPageLocators.NUMBER_ORDER)

    @allure.step('Поиск информации о номере заказа в Ленте заказов')
    def get_number_order_in_feed_orders_history(self):
        return self.get_text(FeedPageLocators.HISTORY_NUMBER_ORDER)

    @allure.step('Поиск количества заказов за все время')
    def get_text_done_all_time(self):
        return self.get_text(FeedPageLocators.TOTAL_ODER_ALL_TIME)

    @allure.step('Поиск и клик по кнопке "Конструктор"')
    def find_and_click_constructor_button(self):
        return self.find_element(HeadersPageLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step('Поиск количества заказов за день')
    def get_text_done_daily(self):
        return self.get_text(FeedPageLocators.DAILY_ORDER)

    @allure.step('Получаем номер заказа в модальном окне')
    def get_number_order_modal_window(self):
        self.wait_to_number(FeedPageLocators.NUMBER_ORDER_IN_MODAL_WINDOW, "9999")
        return self.get_text(FeedPageLocators.NUMBER_ORDER_IN_MODAL_WINDOW)

    @allure.step('Поиск кнопки "Выход" в модальном окне')
    def find_exit(self):
        return self.find_element(FeedPageLocators.EXIT_BUTTON)

    @allure.step('Клик по кнопке "Выход" в модальном окне')
    def click_exit(self):
        return self.click_element(FeedPageLocators.EXIT_BUTTON)

    @allure.step('Поиск информации о номере заказа в работе')
    def get_number_order_in_work(self):
        self.find_element(FeedPageLocators.ORDER_IN_WORK)
        return self.get_text(FeedPageLocators.ORDER_IN_WORK)
