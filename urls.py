class Urls:
    MAIN_URLS = 'https://stellarburgers.nomoreparties.site'
    ORDERS_FEED_URL = 'https://stellarburgers.nomoreparties.site/feed'
    PROFILE_URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    REGISTRATION_URL = 'https://stellarburgers.nomoreparties.site/register'
    LOGIN_URL = 'https://stellarburgers.nomoreparties.site/login'
    FORGOT_PASSWORD_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    RECOVERY_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    RESET_PASSWORD_URL = 'https://stellarburgers.nomoreparties.site/reset-password'


class Endpoints:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'

    INGREDIENTS_URL = f'{MAIN_URL}api/ingredients'  # url для получения списка ингредиентов
    CREATE_ORDER_URL = f'{MAIN_URL}api/orders'  # url для создания заказа
    RESET_PASSWORD_URL = f'{MAIN_URL}api/password-reset'  # url для сброса пароля
    USER_REGISTER_URL = f'{MAIN_URL}api/auth/register'  # url для регистрации
    USER_LOGIN_URL = f'{MAIN_URL}api/auth/login'  # url для авторизации
    USER_LOGOUT_URL = f'{MAIN_URL}api/auth/logout'  # url для выхода
    TOKEN_URL = f'{MAIN_URL}api/auth/token'  # url для получения токена
    USER_INFO_URL = f'{MAIN_URL}api/auth/user'  # url для получения информации о пользователе
    USER_UPDATE_URL = f'{MAIN_URL}api/auth/user'  # url для изменения данных о пользователе
    USER_DELETE_URL = f'{MAIN_URL}api/auth/user'  # url для удаления пользователя
    ALL_ORDERS_URL = f'{MAIN_URL}api/orders/all'  # url для получения информации о всех заказах
    USER_ORDER_INFO_URL = f'{MAIN_URL}api/orders'  # url для получения информации о конкретном заказе
