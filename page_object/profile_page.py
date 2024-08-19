import allure

from locators.page_locators import HeadersPageLocators, AutorizationPageLocators, AccountPageLocators
from page_object.base_page import BasePage


@allure.suite('Методы на Личный кабинет')
class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Поиск кнопки "Личный кабинет" в шапке')
    def find_my_account_button(self):
        return self.find_element(HeadersPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке "Личный кабинет" в шапке')
    def click_my_account_button(self):
        return self.click_element(HeadersPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Поиск и клик по кнопке "Личный кабинет"')
    def find_and_click_my_account_button(self):
        self.find_my_account_button()
        self.click_my_account_button()

    @allure.step('Поиск и ввод email на странице авторизации')
    def find_email_field_and_input_email(self, email):
        return self.input_text_in_field(AutorizationPageLocators.FIELD_EMAIL, email)

    @allure.step('Поиск и ввод пароля на странице авторизации')
    def find_password_field_and_input_password(self, password):
        return self.input_text_in_field(AutorizationPageLocators.FIELD_PASSWORD, password)

    @allure.step('Клик по кнопке "Войти" на странице авторизации')
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

    @allure.step('Поиск и клик по кнопке "Выход" в Личном кабинете')
    def find_exit_button(self):
        return self.find_element(AccountPageLocators.LOGOUT_BUTTON).click()

    @allure.step('Поиск и клик по кнопке "Войти" на странице авторизации')
    def find_login_button(self):
        return self.find_element(AutorizationPageLocators.BUTTON_LOGIN)

    @allure.step('Получение текста "Вход" на странице авторизации')
    def get_text_enter(self):
        return self.get_text(AutorizationPageLocators.TEXT_ENTER)

    @allure.step('Поиск и клик по кнопке "История заказов" в Личном кабинете')
    def find_and_click_history_orders_button(self):
        return self.find_element(AccountPageLocators.HISTORY_BUTTON).click()

    @allure.step('Поиск списка заказов в закладке "История заказов"')
    def find_list_info_orders(self):
        return self.find_element(AccountPageLocators.LIST_ORDERS)
