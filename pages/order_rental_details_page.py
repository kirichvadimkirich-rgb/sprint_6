from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import order_rental_details_page_locators as loc
import allure
from datetime import date
from pages.base_page import BasePage


class OrderRentalDetailsPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Выбрать дату, поле 'Когда привезти самокат'. " \
    "Получить текущую дату, взять из параметров значение на сколько дней сместим, добавить к текущей дате. {date_offset}")
    def set_delivery_date(self, date_offset):
        current_day = int(date.today().day)
        delivery_day = current_day + date_offset
        delivery_date= f"{delivery_day}.{date.today().month}.{date.today().year}"
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc.DELIVERY_DATE_FIELD)).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc.DELIVERY_DATE_FIELD)).send_keys(delivery_date)
        locator = BasePage.format_locator(loc.DELIVERY_DATE_CALENDAR, date_offset)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).click()

    @allure.step("Выбрать срок аренды, поле 'Срок аренды'{rental_period}")
    def set_rental_period(self, rental_period):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc.RENTAL_PERIOD_FIELD)).click()
        locator = BasePage.format_locator(loc.RENTAL_PERIOD, rental_period)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).click()

    @allure.step("Выбрать цвет самоката, поле 'Цвет самоката'{scooter_color}")
    def set_scooter_color(self, scooter_color):
        locator = BasePage.format_locator(loc.SCOOTER_COLOR, scooter_color)
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator)).click()
        
    @allure.step("Заполнить поле 'Комментарий для курьера' {comment}")
    def set_comment(self, comment):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc.COMMENT_FIELD)).send_keys(comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_button_order(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc.ORDER_BUTTON)).click()
       
    @allure.step("Заполнить все поля")
    def fill_out_customer_info(self, date_offset, rental_period, scooter_color, comment):
        self.set_delivery_date(date_offset)
        self.set_rental_period(rental_period)
        self.set_scooter_color(scooter_color)
        self.set_comment(comment)

    

        