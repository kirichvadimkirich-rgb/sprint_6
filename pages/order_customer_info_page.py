from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import order_customer_info_page_locators as loc
import allure


class OrderCustomerInfoPage:

    def __init__(self, driver):
        self.driver = driver
   
    @allure.step("Заполнить поле 'Имя' {name}")
    def set_name(self, name):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc.NAME_FIELD)).send_keys(name)

    @allure.step("Заполнить поле 'Фамилия'{surname}")
    def set_surname(self, surname):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc.SURNAME_FIELD)).send_keys(surname)

    @allure.step("Заполнить поле 'Адрес'{address}")
    def set_address(self, address):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc.ADDRESS_FIELD)).send_keys(address)

    @allure.step('Выбрать станцию метро {metro_station}')
    def set_metro(self, metro_station):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc.METRO_FIELD)).send_keys(metro_station)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc.METRO_DROPDOWN_LIST)).click()
        
    @allure.step("Заполнить поле 'Телефон' {phone}")
    def set_phone(self, phone):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc.PHONE_FIELD)).send_keys(phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_button_next(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc.NEXT_BUTTON)).click()
       
    @allure.step("Заполнить все поля")
    def fill_out_customer_info(self, name, surname, address, metro_station, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro_station)
        self.set_phone(phone)
        