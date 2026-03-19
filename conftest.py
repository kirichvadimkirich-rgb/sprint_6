import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from locators.main_page_locators import ACCEPT_COOKIES


BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@pytest.fixture
#Фикстура для открытия и закрытия драйвера Firefox,  принимаем куки, если есть
def browser():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    #service = Service(GeckoDriverManager().install())
    #driver = webdriver.Firefox(service=service, options=firefox_options)
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(BASE_URL)
    try:
        driver.find_element(*ACCEPT_COOKIES).click()
    except Exception as e:
        print(f"Не удалось принять куки: {e}")
    pass
    yield driver
    driver.quit()

