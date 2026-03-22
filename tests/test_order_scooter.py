import pytest
from data import order_test_data
import allure
from pages.main_page import MainPage
from pages.order_customer_info_page import OrderCustomerInfoPage
from pages.order_rental_details_page import OrderRentalDetailsPage
from pages.order_confirmation_modal_page import OrderConfirmationModalPage
from pages.order_success_modal_page import OrderSuccessModalPage
from url import BASE_URL, LINK_YANDEX_REDIRECT 
from pages.base_page import BasePage
import time

@allure.feature('Создания заказа')
class TestOrderScooter:

    @pytest.mark.parametrize('button_locator, user_data', order_test_data)
    @allure.title('Позитивный тест создание заказа с разными точками входа и данными')
    @allure.description('Заполняем формы заказа,подтвержаем заказ, получаем сообщения об успешном создании заказа. ' \
    'Проверка логотипа Самоката - возвращает на главную страницу. Проверка логотипа Яндекса (открытие новой вкладки с Dzen) ')
    def test_order_scooter_successfully(self, browser, button_locator, user_data):
        main_page = MainPage(browser)
        main_page.click_order_button(button_locator)
        order_customer_page = OrderCustomerInfoPage(browser)
        order_customer_page.fill_out_customer_info(user_data["name"], user_data["surname"],
                                                    user_data["address"], user_data["metro_station"], user_data["phone"])
        order_customer_page.click_button_next()
        order_rental_details_page = OrderRentalDetailsPage(browser)
        order_rental_details_page.fill_out_customer_info(user_data["date_offset"], user_data["rental_period"], 
                                                         user_data["scooter_color"], user_data["comment"])
        order_rental_details_page.click_button_order()
        order_confirmation_modal_page = OrderConfirmationModalPage(browser)
        order_confirmation_modal_page.click_button_yes()
        order_success_modal_page = OrderSuccessModalPage(browser)
        assert 'Заказ оформлен' in order_success_modal_page.get_title_text(), "текст 'Заказ оформлен' отсутсвует"
        order_success_modal_page.click_button_status()
        BasePage._wait_for_page_to_load(browser)
        main_page.click_yandex_logo()
        original = BasePage._switch_to_new_tab(browser, expected_url= LINK_YANDEX_REDIRECT)
        assert main_page._get_current_url_with_wait() == LINK_YANDEX_REDIRECT, f'url { main_page._get_current_url_with_wait()} не соответствует ожидаемому {LINK_YANDEX_REDIRECT}'
        BasePage._close_and_switch_back(browser, original)
        main_page.click_scooter_logo()
        assert main_page._get_current_url_with_wait() == BASE_URL, f'url {main_page._get_current_url_with_wait()} не соответствует ожидаемому {BASE_URL}'
