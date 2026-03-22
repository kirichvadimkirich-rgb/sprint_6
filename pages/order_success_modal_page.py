from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import order_success_modal_page_locators as loc
import allure


class OrderSuccessModalPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить название заголовка')
    def get_title_text(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc.TITLE_TEXT)).text
    
    @allure.step("Нажать на кнопку 'Посмотреть статус'")
    def click_button_status(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc.BUTTON_VIEW_STATUS)).click()
    