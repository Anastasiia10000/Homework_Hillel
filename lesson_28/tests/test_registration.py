import time
import allure
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("User Registration")
class TestUserRegistration:
    @allure.title("User can register and access the dashboard/garage")
    def test_user_can_register(self, driver, wait, fill_registration_form, submit_registration):
        email = f"test_{int(time.time())}@mail.com"

        with allure.step("Fill in the registration form"):
            fill_registration_form("Test", "User", email, "Password123!")

        with allure.step("Submit the form"):
            submit_registration()

        with allure.step("Wait for redirect to the dashboard"):
            wait.until(EC.url_contains("garage"))

        with allure.step("Verify user is on the dashboard page"):
            assert "garage" in driver.current_url.lower()