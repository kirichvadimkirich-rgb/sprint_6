from selenium.webdriver.common.by import By


NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
METRO_FIELD = (By.CLASS_NAME,  "select-search__input")
METRO_DROPDOWN_LIST = (By.XPATH, "//ul[@class = 'select-search__options']/li[1]/button")
PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")