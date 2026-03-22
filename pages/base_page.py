from locators import base_page_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common.exceptions import TimeoutException
import logging


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажать на логотип 'Самокат'")
    def click_scooter_logo(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc.SCOOTER_LOGO)).click()

    @allure.step("Нажать на логотип 'Яндекс'")
    def click_yandex_logo(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc.YANDEX_LOGO)).click()    

    @allure.step('Получение текущего URL')
    def get_current_url(self, driver):
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete" and d.current_url != "about:blank")
        return self.driver.current_url
    
    @staticmethod
    @allure.step("Форматирование локатора: подстановка '{text}'")
    def format_locator(locator, text):
        by, value = locator
        return (by, value.format(text))
    
    @staticmethod
    @allure.step("Перейти на другую вкладку")
    def switch_to_new_tab(driver, expected_url=None, timeout=5):
        original_tab = driver.current_window_handle
        try:
            WebDriverWait(driver, timeout).until(lambda d: len(d.window_handles) > 1)
            new_tab = [tab for tab in driver.window_handles if tab != original_tab][0]
            driver.switch_to.window(new_tab)
            if expected_url:
                 WebDriverWait(driver, timeout).until(EC.url_to_be(expected_url))
            else:
            # Дождаться, чтобы URL перестал быть about:blank
                WebDriverWait(driver, timeout).until(lambda d: d.current_url != "about:blank")
            return original_tab
        except TimeoutException:
            logging.error("Не удалось обнаружить новую вкладку за %s секунд", timeout)
            return None
        except Exception as e:
            logging.exception("Ошибка при переключении на новую вкладку: %s", e)
            return None

    @staticmethod
    @allure.step("Закрыть вкладку и вернуться на предыдущую вкладку")
    def close_and_switch_back(driver, original_tab):
        driver.close()
        driver.switch_to.window(original_tab)

    @staticmethod
    @allure.step("Ожидаем полной загрузки страницы")
    def wait_for_page_to_load(driver):
        WebDriverWait(driver, 5).until(
        lambda d: d.execute_script("return document.readyState") == "complete")    