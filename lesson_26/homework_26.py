"""Написати на python selenium код який пройде по двох фреймах на початковiй сторiнцi,
ввійде в кожний фрейм, введе правильний секретний текст,
натисне кнопку “Перевiрити”,
порівняє текст дiалогового вiкна для підтвердження успішності верифікації та закриє діалогове вікно"""

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "http://localhost:8000/dz.html"
EXPECTED_TEXT = "Верифікація пройшла успішно!"

def run_frame_test(frame_id, input_id, button_selector, secret_text):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)

    try:
        driver.switch_to.frame(driver.find_element(By.ID, frame_id)) # Перехід у потрібний фрейм

        input_box = driver.find_element(By.ID, input_id)
        input_box.clear()
        time.sleep(1)
        input_box.send_keys(secret_text) # Введення секретного тексту

        driver.find_element(By.CSS_SELECTOR, button_selector).click() # Натискання кнопки

        # Alert
        time.sleep(1)
        alert = Alert(driver)
        assert alert.text == EXPECTED_TEXT, f"❌ Тест провалено у {frame_id}!"
        print(f"✅ {frame_id} перевірено успішно")
        alert.accept()

    finally:
        driver.quit()

def test_frame1():
    run_frame_test("frame1", "input1", "body > button", "Frame1_Secret")


def test_frame2():
    run_frame_test("frame2", "input2", "body > button", "Frame2_Secret")


# Запуск тестів
if __name__ == "__main__":
    test_frame1()
    test_frame2()