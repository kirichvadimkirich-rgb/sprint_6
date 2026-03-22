
from locators import base_page_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common.exceptions import TimeoutException
import logging


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _wait_until_visible(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))   
    
    def _wait_until_clickable(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)) 

    def _click(self, locator):
        self._wait_until_clickable(locator).click()

    def _scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _click_with_scroll(self, locator):
        element = self._wait_until_clickable(locator)
        self._scroll_to_element(element)
        self.driver.execute_script("arguments[0].click();", element)

    def _get_text(self, locator):
        element = self._wait_until_visible(locator)
        return element.text
    
    def _send_keys(self, locator, text):
        element = self._wait_until_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидание загрузки страницы == complete, url != about:blank")
    def _wait_page_complete_and_not_about_blank(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: d.execute_script("return document.readyState") == "complete" and d.current_url != "about:blank")

    @allure.step("Нажать на логотип 'Самокат'")
    def click_scooter_logo(self):
        self._click(loc.SCOOTER_LOGO)

    @allure.step("Нажать на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self._click(loc.YANDEX_LOGO)   

    @allure.step('Получение текущего URL c ожиданием загрузки страницы')
    def _get_current_url_with_wait(self):
        self._wait_page_complete_and_not_about_blank()
        return self.driver.current_url
    
    @staticmethod
    @allure.step("Форматирование локатора: подстановка '{text}'")
    def _format_locator(locator, text):
        by, value = locator
        return (by, value.format(text))
    
    @staticmethod
    @allure.step("Перейти на другую вкладку")
    def _switch_to_new_tab(driver, expected_url=None, timeout=5):
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
    def _close_and_switch_back(driver, original_tab):
        driver.close()
        driver.switch_to.window(original_tab)

    @staticmethod
    @allure.step("Ожидаем полной загрузки страницы")
    def _wait_for_page_to_load(driver):
        WebDriverWait(driver, 5).until(lambda d: d.execute_script("return document.readyState") == "complete")  
