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

    USER_REGISTER_URL = f'{MAIN_URL}api/auth/register'      # url для регистрации
    USER_LOGIN_URL = f'{MAIN_URL}api/auth/login'            # url для авторизации
    TOKEN_URL = f'{MAIN_URL}api/auth/token'                 # url для получения токена
    USER_DELETE_URL = f'{MAIN_URL}api/auth/user'            # url для удаления пользователя

