import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from .pages.main_page import MainPage
from .pages.registration_page import RegistrationPage

BASE_URL = "https://guest:welcome2qauto@qauto2.forstudy.space"


@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    # === ОБОВ'ЯЗКОВО для контейнера: headless ===
    chrome_options.add_argument("--headless=new")  # новий режим headless у Chrome 112+
    chrome_options.add_argument("--no-sandbox")  # потрібно для контейнерів
    chrome_options.add_argument("--disable-dev-shm-usage")  # уникнути проблем з /dev/shm
    chrome_options.add_argument("--disable-gpu")  # старі версії Chrome
    chrome_options.add_argument("--window-size=1920,1080")  # щоб елементи на сторінці були видимі
    # === Ініціалізація драйвера ===
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture
def open_registration(driver, wait):
    main = MainPage(driver)
    wait.until(EC.element_to_be_clickable(main.SIGNUP_BUTTON)).click()
    return RegistrationPage(driver)


@pytest.fixture
def fill_registration_form(driver, wait, open_registration):
    def _fill(firstname, lastname, email, password):
        reg = open_registration
        wait.until(EC.visibility_of_element_located(reg.FIRSTNAME_INPUT)).send_keys(firstname)
        driver.find_element(*reg.LASTNAME_INPUT).send_keys(lastname)
        driver.find_element(*reg.EMAIL_INPUT).send_keys(email)
        driver.find_element(*reg.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*reg.REPEAT_PASSWORD_INPUT).send_keys(password)
    return _fill


@pytest.fixture
def submit_registration(driver, open_registration):
    def _submit():
        reg = open_registration
        driver.find_element(*reg.REGISTER_BUTTON).click()
    return _submit