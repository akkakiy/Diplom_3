import pytest
import requests

from selenium import webdriver

from help import RandomUser
from page_object.constructor_page import ConstructorPage
from page_object.feed_order_page import FeedOrderPage
from page_object.main_page import MainPage
from page_object.profile_page import ProfilePage
from urls import Urls, Endpoints


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get(Urls.MAIN_URLS)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)


@pytest.fixture
def constructor_page(driver):
    return ConstructorPage(driver)


@pytest.fixture
def feed_order_page(driver):
    return FeedOrderPage(driver)


@pytest.fixture
def user():                                    # фикстура для создания и удаления пользователя
    payload = RandomUser.create_random_user()
    response = requests.post(Endpoints.USER_REGISTER_URL, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(Endpoints.USER_DELETE_URL, headers={"Authorization": f"{token}"})


@pytest.fixture                                # фикстура для авторизации
def login(user, driver):
    data_user = user[0]
    main_page = MainPage(driver)
    profile_page = ProfilePage(driver)
    main_page.find_and_click_my_account_button()
    profile_page.login_user(data_user["email"], data_user["password"])
