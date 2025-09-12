import time
from selenium.webdriver.support import expected_conditions as EC

def test_user_can_register(driver, wait, fill_registration_form, submit_registration):
    email = f"test_{int(time.time())}@mail.com"
    fill_registration_form("Test", "User", email, "Password123!")
    submit_registration()

    # Перевірка, що користувача перекинуло в гараж (garage page)
    wait.until(EC.url_contains("garage"))
    assert "garage" in driver.current_url.lower()