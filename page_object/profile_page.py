import allure

from locators.page_locators import HeadersPageLocators, AutorizationPageLocators, AccountPageLocators
from page_object.base_page import BasePage


@allure.suite('Методы на Личный кабинет')
class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Поиск и нажатие кнопки "Личный кабинет"')
    def find_and_click_my_account_button(self):
        return self.find_element(HeadersPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    @allure.step('Поиск и ввод email')
    def find_email_field_and_input_email(self, email):
        return self.input_text_in_field(AutorizationPageLocators.FIELD_EMAIL, email)

    @allure.step('Поиск и ввод пароля')
    def find_password_field_and_input_password(self, password):
        return self.input_text_in_field(AutorizationPageLocators.FIELD_PASSWORD, password)

    @allure.step('Клик по кнопке "Войти"')
    def click_element_login_button(self):
        return self.click_element(AutorizationPageLocators.BUTTON_LOGIN)

    @allure.step('Авторизация пользователя')
    def login_user(self, email, password):
        self.find_email_field_and_input_email(email)
        self.find_password_field_and_input_password(password)
        self.click_element_login_button()

    @allure.step('Поиск информации профиля')
    def get_info_profile(self):
        return self.find_element(AccountPageLocators.INFO_PROFILE)

    @allure.step('Поиск и клик по кнопке "Выход"')
    def find_exit_button(self):
        return self.find_element(AccountPageLocators.LOGOUT_BUTTON).click()

    @allure.step('Поиск и клик по кнопке "Войти"')
    def find_login_button(self):
        return self.find_element(AutorizationPageLocators.BUTTON_LOGIN)

    @allure.step('Получение текста "Вход"')
    def get_text_enter(self):
        return self.get_text(AutorizationPageLocators.TEXT_ENTER)

    @allure.step('Поиск и клик по кнопке "История заказов"')
    def find_and_click_history_orders_button(self):
        return self.find_element(AccountPageLocators.HISTORY_BUTTON).click()

    @allure.step('Поиск списка заказов в закладке "История заказов"')
    def find_list_info_orders(self):
        return self.find_element(AccountPageLocators.LIST_ORDERS)

    @allure.step('Полные шаги для авторизации пользователя')
    def full_steps_login_user(self):
        self.find_and_click_my_account_button()

    @allure.step('Полные шаги для логаута пользователя')
    def full_steps_login_and_logaut(self):
        self.find_and_click_my_account_button()
        self.find_and_click_my_account_button()
        self.find_exit_button()

    @allure.step('Полные шаги для открытия истории заказов')
    def full_steps_open_history_orders(self):
        self.find_and_click_my_account_button()
        self.find_and_click_my_account_button()
        self.find_and_click_history_orders_button()
