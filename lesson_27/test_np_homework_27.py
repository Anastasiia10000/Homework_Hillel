from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from lesson_27.np_tracking_page import NovaPoshtaTrackingPage
import pytest

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def test_novaposhta_tracking(driver):
    ttn_number = "20451227388216"
    expected_status = "Отримана"

    page = NovaPoshtaTrackingPage(driver)
    page.open()
    page.enter_ttn(ttn_number)
    status = page.get_status()

    assert status == expected_status, f"Очікувався статус '{expected_status}', отримано '{status}'"