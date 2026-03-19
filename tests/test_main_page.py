import pytest
from data import faq_data
import allure
from pages.main_page import MainPage
from conftest import BASE_URL


@allure.feature('FAQ')
class TestMainPage:

    @pytest.mark.parametrize('index, expected_text', faq_data)
    @allure.title('Проверка текста ответа на вопрос из FAQ')
    @allure.description('На главной странице ищем вопросы с выпадающими ответами по нажатию и сверяем текст ответов')
    @allure.link(BASE_URL, name='Ссылка на страницу сайта')
    def test_faq_answer_text(self, browser, index, expected_text):
        main_page = MainPage(browser)
        main_page.click_question(index)
        actual_text = main_page.get_answer_text(index)
        assert actual_text == expected_text, f'Текст ответа для вопроса {index} не соответствует ожидаемому'