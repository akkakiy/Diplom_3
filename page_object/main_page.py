import allure

from help import RandomUser
from locators.page_locators import HeadersPageLocators, AutorizationPageLocators, RecoveryPageLocators
from page_object.base_page import BasePage


@allure.step('Методы на страницу восстановления пароля')
class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Поиск и клик по кнопки "Личный кабинет" в верхнем меню')
    def find_and_click_my_account_button(self):
        return self.find_element(HeadersPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    @allure.step('Поиск и клик по ссылке "Восстановить пароль" на странице авторизации')
    def find_and_click_forgot_password_button(self):
        self.find_element(AutorizationPageLocators.LINK_RECOVERY).click()

    @allure.step('Проверка наличия текста "Восстановление пароля"')
    def find_and_check_recovery_text(self):
        return self.find_element(RecoveryPageLocators.BUTTON_RECOVERY)

    @allure.step('Поиск поля email на странице восстановления пароля')
    def find_email_field(self):
        return self.find_element(RecoveryPageLocators.FIELD_EMAIL_RECOVERY)

    @allure.step('Ввод в поле email для восстановления пароля')
    def input_email_for_recovery(self):
        self.find_email_field().send_keys(RandomUser.create_random_user()['email'])

    @allure.step('Поиск и клик по кнопке "Восстановить" на странице восстановления пароля')
    def find_and_click_recovery_button(self):
        return self.find_element(RecoveryPageLocators.BUTTON_RECOVERY).click()

    @allure.step('Поиск поля для ввода нового пароля')
    def find_field_new_password(self):
        return self.find_element(RecoveryPageLocators.NEW_FIELD_PASSWORD)

    @allure.step('Ввод нового пароля')
    def input_new_password(self):
        self.find_field_new_password().send_keys(RandomUser.create_random_user()['password'])

    @allure.step('Поиск и клик по кнопке "Показать пароль"')
    def find_and_click_view_new_password(self):
        return self.find_element(RecoveryPageLocators.BUTTON_VIEW_PASSWORD).click()

    @allure.step('Проверка активности поля нового пароля')
    def check_field_activ_new_password(self):
        return self.find_element(RecoveryPageLocators.FIELD_ACTIVE)
