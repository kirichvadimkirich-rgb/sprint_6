from selenium.webdriver.common.by import By

# Окно с принятием куки
ACCEPT_COOKIES = (By.ID, "rcc-confirm-button")

# Логотипы
SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

# Кнопка Заказать
ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_RoadMap')]//button[text()='Заказать']")

# Вопросы о важном 
QUESTION_PREFIX = (By.ID, "accordion__heading-{}")
ANSWER_PREFIX = (By.ID, "accordion__panel-{}")