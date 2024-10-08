import allure

from locators.page_locators import HeadersPageLocators, MainPageLocators, FeedPageLocators
from page_object.base_page import BasePage


@allure.suite('Методы на Конструктор для бургеров')
class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Личный кабинет" в верхнем меню')
    def find_and_click_account_button(self):
        return self.find_element(HeadersPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    @allure.step('Клик по кнопке "Конструктор" в верхнем меню')
    def find_and_click_constructor_button(self):
        return self.find_element(HeadersPageLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step('Поиск элемента панель конструктора на главной странице')
    def find_burger_panel(self):
        return self.find_element(MainPageLocators.BURGER_PANEL)

    @allure.step('Поиск элемента "Флюоресцентная булка R2-D3"')
    def find_bun(self):
        return self.find_element(MainPageLocators.BUN)

    @allure.step('Поиск и клик по кнопке "Лента заказов" в верхнем меню')
    def find_and_click_feed_orders(self):
        return self.find_element(HeadersPageLocators.FEED_ORDER_BUTTON).click()

    @allure.step('Поиск окна "Лента заказов"')
    def find_window_feed_order(self):
        return self.find_element(FeedPageLocators. WINDOW_FEED_ORDER)

    @allure.step('Поиск кнопки "Булки" в конструкторе')
    def find_and_button_buns(self):
        return self.find_element(MainPageLocators.BUTTON_BUNS)

    @allure.step('Клик по ингредиенту "Флюоресцентная булка R2-D3" в конструкторе')
    def find_and_click_bun(self):
        return self.find_element(MainPageLocators.BUN).click()

    @allure.step('Поиск окна с информацией об ингредиенте "Флюоресцентная булка R2-D3"')
    def find_and_check_window_info(self):
        return self.find_element(MainPageLocators.INGREDIENT_INFO_WINDOW)

    @allure.step('Поиск и нажатие кнопки закрытия окна с информацией об ингредиенте "Флюоресцентная булка R2-D3"')
    def find_and_click_modal_close_button(self):
        return self.find_element(MainPageLocators.MODAL_CLOSE_BUTTON).click()

    @allure.step('Поиск и нажатие кнопки "Соусы" в конструкторе')
    def find_and_click_buttons_sauces(self):
        return self.find_element(MainPageLocators.BUTTON_SAUCES).click()

    @allure.step('Поиск и нажатие ингредиента "Соус Spicy-X" в конструкторе')
    def find_and_click_sauce(self):
        return self.find_element(MainPageLocators.SAUCE).click()

    @allure.step('Поиск и нажатие кнопки "Начинки" в конструкторе')
    def find_and_click_buttons_sauces(self):
        return self.find_element(MainPageLocators.BUTTON_FILLINGS).click()

    @allure.step('Поиск и нажатие ингредиента "Говяжий метеорит (отбивная)" в конструкторе')
    def find_and_click_sauce(self):
        return self.find_element(MainPageLocators.FILLING).click()

    @allure.step('Перетаскивание ингредиента "Флюоресцентная булка R2-D3" в корзину')
    def transfer_ingredient(self):
        self.drag_and_drop(MainPageLocators.BUN, MainPageLocators.BURGER_BASKET)

    @allure.step('Поиск и получение количества ингредиента "Флюоресцентная булка R2-D3"')
    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENTS_COUNTER)

    @allure.step('Поиск и нажатие кнопки "Оформить заказ"')
    def find_and_click_button_place_order(self):
        return self.find_element(MainPageLocators.BUTTON_PLACE_ORDER).click()

    @allure.step('Поиск окна с подтверждением оформления заказа')
    def find_window_order_confirm(self):
        return self.find_element(MainPageLocators.MODAL_WINDOW_CONFIRM)

    @allure.step('Поиск текста в окне с подтверждением оформления заказа')
    def find_text_order_confirm(self):
        return self.get_text(MainPageLocators.TEXT_ORDER_CONFIRM)
