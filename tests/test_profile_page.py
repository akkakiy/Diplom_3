import allure

from data import Massage


@allure.suite('Проверки на Авторизацию пользователя')
class TestProfilePage:
    @allure.title('Проверка страницы "Личный кабинет"')
    def test_login(self, driver, profile_page, user, login):
        profile_page.find_and_click_my_account_button()
        assert profile_page.get_info_profile().is_displayed()

    @allure.title('Проверка страницы выхода из "Личного кабинета"')
    def test_logaut(self, driver, profile_page, user, login):
        profile_page.find_and_click_my_account_button()
        profile_page.find_exit_button()
        assert (profile_page.find_login_button().is_displayed()
                and profile_page.get_text_enter() == Massage.TEXT_ENTER_LOGIN_PAGE)

    @allure.title('Проверка страницы "История заказов"')
    def test_history_orders(self, driver, profile_page, user, login):
        profile_page.find_and_click_my_account_button()
        profile_page.find_and_click_history_orders_button()
        assert profile_page.find_list_info_orders().is_displayed()
