
from locators import main_page_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.base_page import BasePage


class MainPage:
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по вопросу с индексом {index}')
    def click_question(self, index):
        locator = BasePage.format_locator(loc.QUESTION_PREFIX, index)
        question = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        self.driver.execute_script("arguments[0].click();", question)


    @allure.step('Получение текста ответа для вопроса с индексом {index}')
    def get_answer_text(self, index):
        locator = BasePage.format_locator(loc.ANSWER_PREFIX, index)
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).text
       
    @allure.step('Клик по вопросу с индексом {index}')
    def click_order(self, index):
        locator = BasePage.format_locator(loc.QUESTION_PREFIX, index)
        question = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        self.driver.execute_script("arguments[0].click();", question)

    @allure.step('Нажать на кнопку заказа (верхнюю или нижнюю)')
    def click_order_button(self, button_locator):
        button_next = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(button_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", button_next)
        self.driver.execute_script("arguments[0].click();", button_next)
