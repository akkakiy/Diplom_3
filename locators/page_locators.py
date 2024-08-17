from selenium.webdriver.common.by import By


class HeadersPageLocators:

    # логотип
    LOGO = (By.XPATH, ".//a[@class='Header_Link__1TAG7']")
    # кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # кнопка "Лента Заказов"
    FEED_ORDER_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    # кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")


class MainPageLocators:

    # панель конструктора бургера
    BURGER_PANEL = (By.XPATH, ".//body[contains((text), display)]")
    # кнопка "Булки"
    BUTTON_BUNS = (By.XPATH, ".//span[text() = 'Булки']")
    # кнопка "Соусы"
    BUTTON_SAUCES = (By.XPATH, ".//span[text()='Соусы']")
    # кнопка "Начинки"
    BUTTON_FILLINGS = (By.XPATH, ".//span[text()='Начинки']")
    # Флюоресцентная булка R2-D3
    BUN = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")
    # Соус Spicy-X
    SAUCE = (By.XPATH, ".//p[text()='Соус Spicy-X']")
    # Говяжий метеорит (отбивная)
    FILLING = (By.XPATH, ".//p[text()='Говяжий метеорит (отбивная)']")
    # Кнопка "Войти в аккаунт"
    BUTTON_LOGIN_MAIN_PAGE = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    # Кнопка "Оформить заказ"
    BUTTON_PLACE_ORDER = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")
    # кнопка для закрытия окна с подтверждением заказа
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"
                                    "//button[@type='button']")
    # корзина заказов
    BURGER_BASKET = (By.XPATH, ".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']")
    # окно с информацией об ингредиенте
    INGREDIENT_INFO_WINDOW = (By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']")
    # счетчик ингредиентов в корзине
    INGREDIENTS_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    # окно принятия заказа
    MODAL_WINDOW_CONFIRM = (By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']")
    # текст "Ваш заказ начали готовить"
    TEXT_ORDER_CONFIRM = (By.XPATH, ".//p[contains(text(),'Ваш заказ начали готовить')]")


class AutorizationPageLocators:

    # текст "Вход"
    TEXT_ENTER = (By.XPATH, "//h2[contains(text(),'Вход')]")
    # поле ввода email
    FIELD_EMAIL = (By.XPATH, ".//input[@name='name']")
    # поле ввода пароля
    FIELD_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    # кнопка "Войти"
    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")
    # Ссылка "Зарегистрироваться"
    LINK_REGISTER = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # Ссылка "Восстановить пароль"
    LINK_RECOVERY = (By.XPATH, "//a[text()='Восстановить пароль']")


class RecoveryPageLocators:

    # поле ввода email
    FIELD_EMAIL_RECOVERY = (By.XPATH, ".//input[@name='name']")
    # Кнопка "Восстановить"
    BUTTON_RECOVERY = (By.XPATH, ".//button[text()='Восстановить']")
    # Ссылка "Войти"
    LINK_LOGIN = (By.XPATH, ".//a[text() = 'Войти']")
    # поле для ввода нового пароля
    NEW_FIELD_PASSWORD = (By.XPATH, ".//input[@name='Введите новый пароль']")
    # Кнопка "Сохранить"
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")
    # Кнопка "Показать пароль"
    BUTTON_VIEW_PASSWORD = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    # активность поля пароля
    FIELD_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")
    # Текст "Восстановление пароля"
    RECOVERY_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']")


class AccountPageLocators:

    # кнопка "Профиль"
    PROFILE_BUTTON = (By.XPATH, "//a[contains(text(),'Профиль')]")
    # кнопка "История заказов"
    HISTORY_BUTTON = (By.LINK_TEXT, "История заказов")
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    # поле с именем
    NAME_FIELD = (By.XPATH, "//label[contains(text(), 'Имя')]")
    # поле с логином/почтой
    LOGIN_FIELD = (By.XPATH, "//label[contains(text(), 'Логин')]")
    # поле с паролем
    PASSWORD_FIELD = (By.XPATH, "//label[contains(text(), 'Пароль')]")
    # кнопка "Отмена"
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(),'Отмена')]")
    # кнопка "Сохранить"
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]")
    # текст "В этом разделе вы можете изменить свои персональные данные"
    TEXT_INFO = (By.XPATH, "//p[contains(text(),'В этом разделе вы можете')]")
    # Информация профиля с персональными данными
    INFO_PROFILE = (By.XPATH, "//div[@class='Account_account__vgk_w']")
    # Список заказов
    LIST_ORDERS = (By.XPATH, "//div[@class='Account_contentBox__2CPm3']")
    # Получение номера заказа
    NUMBER_ORDER = (By.XPATH, "//p[@class='text text_type_digits-default']")


class FeedPageLocators:

    # Текст "Лента Заказов"
    FEED_ORDER = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    # счетчик "В работе:"
    ORDER_IN_WORK = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]"
                               "//li[contains(@class,'text_type_digits-default')]")
    # счетчик "Выполнено за все время:"
    TOTAL_ODER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    # счетчик "Выполнено за сегодня:"
    DAILY_ORDER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    # номер заказа
    NUMBER_ORDER = (By.XPATH, "//p[@class='text text_type_digits-default mb-10 mt-5']")
    # окно с лентой заказов
    WINDOW_FEED_ORDER = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']")
    # окно с информацией о заказе
    WINDOW_INFO_ORDER_IN_WORK = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    # Номер заказа в истории заказов
    HISTORY_NUMBER_ORDER = (By.XPATH, "//p[(@class= 'text text_type_digits-default')]")
    # текст в модальном окне
    STATION_TEXT_IN_WIN_INFO = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]"
                                          "//p[contains(text(),'Дождитесь готовности на орбитальной станции')]")
    # Кнопка "Закрыть" в модальном окне
    EXIT_BUTTON = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]"
                             "//button[contains(@class,'Modal_modal__close_modified')]")
    # Номер заказа в модальном окне
    NUMBER_ORDER_IN_MODAL_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')
