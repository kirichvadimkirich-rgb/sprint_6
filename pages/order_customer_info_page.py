
from locators import order_customer_info_page_locators as loc
import allure
from pages.base_page import BasePage

class OrderCustomerInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
   
    @allure.step("Заполнить поле 'Имя' {name}")
    def set_name(self, name):
        self._send_keys(loc.NAME_FIELD, name)

    @allure.step("Заполнить поле 'Фамилия'{surname}")
    def set_surname(self, surname):
        self._send_keys(loc.SURNAME_FIELD, surname)

    @allure.step("Заполнить поле 'Адрес'{address}")
    def set_address(self, address):
        self._send_keys(loc.ADDRESS_FIELD, address)

    @allure.step('Выбрать станцию метро {metro_station}')
    def set_metro(self, metro_station):
        self._send_keys(loc.METRO_FIELD, metro_station)
        self._click(loc.METRO_DROPDOWN_LIST)
        
    @allure.step("Заполнить поле 'Телефон' {phone}")
    def set_phone(self, phone):
        self._send_keys(loc.PHONE_FIELD, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_button_next(self):
        self._click(loc.NEXT_BUTTON)
       
    @allure.step("Заполнить все поля")
    def fill_out_customer_info(self, name, surname, address, metro_station, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro_station)
        self.set_phone(phone)
        