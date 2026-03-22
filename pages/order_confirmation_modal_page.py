from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import order_confirmation_modal_page_locators as loc
import allure


class OrderConfirmationModalPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать кнопку "Да"')
    def click_button_yes(self):
         WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc.BUTTON_YES)).click()