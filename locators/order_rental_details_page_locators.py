from selenium.webdriver.common.by import By

DELIVERY_DATE_FIELD = (By.CSS_SELECTOR ,"input[placeholder='* Когда привезти самокат']")
DELIVERY_DATE_CALENDAR = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='{}']")
RENTAL_PERIOD_FIELD = (By.XPATH, "//span[@class= 'Dropdown-arrow']")
RENTAL_PERIOD = (By.XPATH, "//div[@class= 'Dropdown-option' and text() = '{}']")
SCOOTER_COLOR = (By.XPATH, "//label[text() = '{}']/input")
COMMENT_FIELD = (By.CSS_SELECTOR , "input[placeholder='Комментарий для курьера']")
ORDER_BUTTON = (By.XPATH, "//div[contains(@class,  'Order_Buttons' )]//button[text()='Заказать']")