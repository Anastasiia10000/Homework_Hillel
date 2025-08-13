# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор
# у файл json__<your_second_name>.log

import os
import json
import logging

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(CURRENT_DIR, "json__Kalyta.log")

def setup_logger(log_path):
    logger_json = logging.getLogger("log_json_validator")
    logger_json.setLevel(logging.ERROR)

    if logger_json.hasHandlers():
        logger_json.handlers.clear()

    fh = logging.FileHandler(log_path, mode='a', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger_json.addHandler(fh)

    return logger_json

def validate_json_files(folder_path, log):
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                log.error(f"File {filename} is not valid JSON: {e}")

if __name__ == "__main__":
    logger = setup_logger(LOG_FILE)
    validate_json_files(CURRENT_DIR, logger)