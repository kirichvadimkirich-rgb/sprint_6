from selenium.webdriver.common.by import By

TITLE_TEXT = (By.XPATH, "//div[contains(@class,  'Order_ModalHeader')]")
BUTTON_VIEW_STATUS = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Посмотреть статус']")
