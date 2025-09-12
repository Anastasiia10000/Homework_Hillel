"""Створіть необхідні класи та функції, щоб за допомогою Selenium на сайті
https://tracking.novaposhta.ua/#/uk
ввести номер накладної (передається з тесту) та отримує статус посилки в теркінгу, напр."""
# <div data-v-631babf2="" class="header__parcel-dynamic-status px-4 d-flex align-center">
# <div data-v-631babf2="" class="d-flex flex-column status-icon mr-4 status-icon-grey">
# <!----></div>
# <div data-v-631babf2="" class="flex-grow-1"
# <div data-v-631babf2="" class="header__status-header"> Зараз: </div><!---->
# <div data-v-631babf2="" class="header__status-text">Посилка отримана</div>
# </div></div>
"""Поверне: Посилка отримана
Тест повинен перівіряти, що отриманий статус відповідає очікуваному.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NovaPoshtaTrackingPage:
    URL = "https://tracking.novaposhta.ua/#/uk"

    INPUT_FIELD = (By.CSS_SELECTOR, '#en')
    STATUS_TEXT = (By.CSS_SELECTOR, "div.header__status-text")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

    def enter_ttn(self, ttn: str):
        field = self.wait.until(EC.presence_of_element_located(self.INPUT_FIELD))
        field.clear()
        field.send_keys(ttn)
        field.send_keys(Keys.ENTER)

    def get_status(self) -> str:
        status_element = self.wait.until(
            EC.visibility_of_element_located(self.STATUS_TEXT)
        )
        return status_element.text.strip()