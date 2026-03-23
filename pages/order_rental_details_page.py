
from locators import order_rental_details_page_locators as loc
import allure
from datetime import date
from pages.base_page import BasePage


class OrderRentalDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Выбрать дату, поле 'Когда привезти самокат'. " \
    "Получить текущую дату, взять из параметров значение на сколько дней сместим, добавить к текущей дате. {date_offset}")
    def set_delivery_date(self, date_offset):
        current_day = int(date.today().day)
        delivery_day = current_day + date_offset
        delivery_date= f"{delivery_day}.{date.today().month}.{date.today().year}"
        self._click(loc.DELIVERY_DATE_FIELD)
        self._send_keys(loc.DELIVERY_DATE_FIELD, delivery_date)
        locator = self._format_locator(loc.DELIVERY_DATE_CALENDAR, date_offset)
        self._click(locator)

    @allure.step("Выбрать срок аренды, поле 'Срок аренды'{rental_period}")
    def set_rental_period(self, rental_period):
        self._click(loc.RENTAL_PERIOD_FIELD)
        locator = self._format_locator(loc.RENTAL_PERIOD, rental_period)
        self._click(locator)

    @allure.step("Выбрать цвет самоката, поле 'Цвет самоката'{scooter_color}")
    def set_scooter_color(self, scooter_color):
        locator = self._format_locator(loc.SCOOTER_COLOR, scooter_color)
        self._click(locator)
        
    @allure.step("Заполнить поле 'Комментарий для курьера' {comment}")
    def set_comment(self, comment):
        self._send_keys(loc.COMMENT_FIELD, comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_button_order(self):
        self._click(loc.ORDER_BUTTON)
       
    @allure.step("Заполнить все поля")
    def fill_out_customer_info(self, date_offset, rental_period, scooter_color, comment):
        self.set_delivery_date(date_offset)
        self.set_rental_period(rental_period)
        self.set_scooter_color(scooter_color)
        self.set_comment(comment)

    

        