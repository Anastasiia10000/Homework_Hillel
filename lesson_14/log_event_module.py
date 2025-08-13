# log_event_module.py

import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "login_system.log")

# LOG_FILE = "login_system.log" # Задаємо назву лог-файлу, в який буде записуватися інформація

# Створюємо глобальний логер
logger = logging.getLogger("log_event") # Створюємо (або отримуємо існуючий) логер із назвою
logger.setLevel(logging.DEBUG) # Встановлюємо від якого рівня буде логування, DEBUG — найнижчий рівень = логування всіх повідомлень

#Додаємо хендлер лише один раз
if not logger.handlers: # Перевіряємо, чи у логера вже є обробники (handlers)
    # --- Хендлер для файлу ---
    file_handler = logging.FileHandler(LOG_FILE, mode='a')
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter) # Прив’язуємо форматтер до обробника, щоб всі записи у лог-файлі мали відповідний вигляд
    logger.addHandler(file_handler) # Додаємо обробник до логера

    # --- Хендлер для консолі ---
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

# # Зачищаємо хендлери, якщо вони вже існують
# if logger.hasHandlers():
#     logger.handlers.clear()
#
# file_handler = logging.FileHandler(LOG_FILE, mode='a')
# file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
#
# console_handler = logging.StreamHandler()
# console_formatter = logging.Formatter('%(levelname)s - %(message)s')
# console_handler.setFormatter(console_formatter)
# logger.addHandler(console_handler)

def log_event(username: str, status: str):

# Логує подію входу в систему.
    log_message = f"Login event - Username: {username}, Status: {status}" #Формуємо повідомлення, яке буде записано у лог.

# Логування з відповідним рівнем важливості:
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

# 🔸 Ручний запуск для перевірки
if __name__ == "__main__":
    log_event("admin", "success") # У файл записується: 2025-08-07 20:42:33,987 - INFO - Login event - Username: admin, Status: success
    log_event("admin", "expired")
    log_event("admin", "failed")
    log_event("admin", "unknown")
    print(f"Logs are saved in a file: {LOG_FILE}")

