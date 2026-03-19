
from locators import main_page_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.action_chains import ActionChains


class MainPage():
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по вопросу с индексом {index}')
    def click_question(self, index):
        by, value = main_page_locators.QUESTION_PREFIX
        locator = (by, value.format(index))
        question = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        self.driver.execute_script("arguments[0].click();", question)


    @allure.step('Получение текста ответа для вопроса с индексом {index}')
    def get_answer_text(self, index):
        by, value = main_page_locators.ANSWER_PREFIX
        locator = (by, value.format(index))
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).text
       

   