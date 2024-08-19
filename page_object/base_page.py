import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получение URL')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Проверка URL')
    def check_url(self, url):
        return WebDriverWait(self.driver, 15).until(EC.url_to_be(url))

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Ввод текста в поле')
    def input_text_in_field(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Проверка видимости элемента')
    def check_element_visibility(self, locator):
        return self.driver.find_element(locator).is_displayed()

    @allure.step('Ожидание появления элемента')
    def wait_for_closing_of_element(self, locator):
        WebDriverWait(self.driver, 15).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание смены значения')
    def wait_to_number(self, locator, value):
        return WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(locator, value))

    @allure.step('Скролл на элемент')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Перемещение элемента')
    def drag_and_drop(self, element_locator, target_locator):
        element = self.driver.find_element(*element_locator)
        target = self.driver.find_element(*target_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(element, target).perform()
