"""По 5 видів будь-яких локаторів для будь-якого сайту"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Запуск Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.booking.com/")
time.sleep(10)

print("Знаходимо лого")
header_logo_class = driver.find_element(By.CLASS_NAME, "de576f5064")
header_logo_css = driver.find_element(By.CSS_SELECTOR, '#b2indexPage > div:nth-child(4) > div > div > header > div > nav.Header_bar > div.Header_main > div > span > a')
header_logo_xpath = driver.find_element(By.XPATH, '//*[@id="b2indexPage"]/div[2]/div/div/header/div/nav[1]/div[1]/div/span/a')
print(header_logo_class.get_attribute("aria-label"))
print(header_logo_css.get_attribute("aria-label"))
print(header_logo_xpath.get_attribute("aria-label"))

print("\nЗнаходимо лінк 'Помешкання'")
accommodations_link_id = driver.find_element(By.ID, "accommodations")
accommodations_link_class = driver.find_element(By.CLASS_NAME, "b99b6ef58f")
accommodations_link_css = driver.find_element(By.CSS_SELECTOR, "div.ca9d921c46 > span.b99b6ef58f")
accommodations_link_xpath = driver.find_element(By.XPATH, '//*[@id="accommodations"]')
print(accommodations_link_id.text)
print(accommodations_link_class.text)
print(accommodations_link_css.text)
print(accommodations_link_xpath.text)

print("\nЗнаходимо лінк 'Переліт'")
flights_link_id = driver.find_element(By.ID, "flights")
flights_link_css = driver.find_element(By.CSS_SELECTOR, "#flights")
flights_link_xpath = driver.find_element(By.XPATH, '//*[@id="flights"]')
print(flights_link_id.text)
print(flights_link_css.text)
print(flights_link_xpath.text)

print("\nЗнаходимо лінк 'Оренда авто'")
cars_link_id = driver.find_element(By.ID, "cars")
cars_link_xpath = driver.find_element(By.XPATH, '//*[@id="cars"]')
print(cars_link_id.text)
print(cars_link_xpath.text)

print("\nЗнаходимо лінк 'Дозвілля'")
attractions_link_id = driver.find_element(By.ID, "attractions")
attractions_link_xpath = driver.find_element(By.XPATH, '//*[@id="attractions"]')
print(attractions_link_id.text)
print(attractions_link_xpath.text)

print("\nЗнаходимо лінк 'Таксі з/до аеропорту'")
airport_taxis_link_id = driver.find_element(By.ID, "airport_taxis")
airport_taxis_link_xpath = driver.find_element(By.XPATH, '//*[@id="airport_taxis"]')
print(airport_taxis_link_id.text)
print(airport_taxis_link_xpath.text)

print("\nЗнаходимо поле інпуту 'Куди ви вирушаєте?'")
destination_field_id = driver.find_element(By.ID, ":rh:")
destination_field_name = driver.find_element(By.NAME, "ss")
destination_field_class = driver.find_element(By.CLASS_NAME, "b915b8dc0b")
destination_field_css = driver.find_element(By.CSS_SELECTOR, r"#\:rh\:")
destination_field_xpath = driver.find_element(By.XPATH, '//*[@id=":rh:"]')
print(destination_field_id.get_attribute("aria-label"))
print(destination_field_name.get_attribute("aria-label"))
print(destination_field_class.get_attribute("aria-label"))
print(destination_field_css.get_attribute("aria-label"))
print(destination_field_xpath.get_attribute("aria-label"))

print("\nЗнаходимо чекбокс 'Перельоти'")
flight_checkbox_id = driver.find_element(By.ID, ":rj:")
flight_checkbox_name = driver.find_element(By.NAME, "sb_flight_search")
flight_checkbox_class = driver.find_element(By.CLASS_NAME, "faadc60545")
flight_checkbox_css = driver.find_element(By.CSS_SELECTOR, r"#\:rj\:")
flight_checkbox_xpath = driver.find_element(By.XPATH, '//*[@id=":rj:"]')
print(flight_checkbox_id.get_attribute("type"))
print(flight_checkbox_name.get_attribute("type"))
print(flight_checkbox_class.get_attribute("type"))
print(flight_checkbox_css.get_attribute("type"))
print(flight_checkbox_xpath.get_attribute("type"))

# Закриваємо браузер
driver.quit()
