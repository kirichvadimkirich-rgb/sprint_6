
from locators import order_confirmation_modal_page_locators as loc
import allure
from pages.base_page import BasePage


class OrderConfirmationModalPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажать кнопку "Да"')
    def click_button_yes(self):
        self._click(loc.BUTTON_YES)