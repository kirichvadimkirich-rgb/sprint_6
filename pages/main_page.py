
from locators import main_page_locators as loc
import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по вопросу с индексом {index}')
    def click_question(self, index):
        locator = BasePage._format_locator(loc.QUESTION_PREFIX, index)
        self._click_with_scroll(locator)

    @allure.step('Получение текста ответа для вопроса с индексом {index}')
    def get_answer_text(self, index):
        locator = BasePage._format_locator(loc.ANSWER_PREFIX, index)
        return self._get_text(locator)
       
    @allure.step('Нажать на кнопку заказа (верхнюю или нижнюю)')
    def click_order_button(self, button_locator):
        self._click_with_scroll(button_locator)
