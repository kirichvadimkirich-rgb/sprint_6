import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from locators.main_page_locators import ACCEPT_COOKIES
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from url import BASE_URL

@pytest.fixture
#Фикстура для открытия и закрытия драйвера Firefox,  принимаем куки, если есть
def driver():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()

@pytest.fixture
def browser(driver):
    driver.get(BASE_URL)
    try:
        driver.find_element(*ACCEPT_COOKIES).click()
    except (NoSuchElementException, ElementClickInterceptedException):
        # Если кнопка не найдена или не кликабельна — просто игнорируем
        pass   
    yield driver
