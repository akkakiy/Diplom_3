import allure


@allure.suite('Восстановление пароля')
class TestRecoveryPass:
    @allure.title('Проверка кнопки "Восстановить пароль" на странице авторизации')
    def test_recovery_pass(self, driver, main_page):
        main_page.full_steps_recovery()
        assert main_page.find_and_check_recovery_text().is_displayed()

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_input_email_for_recovery(self, driver, main_page):
        main_page.full_steps_recovery_pass_page()
        assert main_page.find_field_new_password() is not None

    @allure.title('Проверка ввода нового пароля')
    def test_input_new_password(self, driver, main_page):
        main_page.full_steps_check_input_new_password()
        assert main_page.check_field_activ_new_password().is_displayed()
