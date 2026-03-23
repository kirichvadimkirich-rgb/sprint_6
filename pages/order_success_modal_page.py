
from locators import order_success_modal_page_locators as loc
import allure
from pages.base_page import BasePage

class OrderSuccessModalPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получить название заголовка')
    def get_title_text(self): 
        return self._get_text(loc.TITLE_TEXT)
    
    @allure.step("Нажать на кнопку 'Посмотреть статус'")
    def click_button_status(self):
        self._click(loc.BUTTON_VIEW_STATUS)
    