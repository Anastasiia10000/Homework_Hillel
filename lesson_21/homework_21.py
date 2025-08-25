"""
Моніторингова система клєнта надсилає сигнал, що вона працездатна кожні 30-31 сек - наприклад:
Timestamp 05:45:40, а в наступному повідомлені — Timestamp 05:45:09 (тут різниця heartbeat в 31 секунду)
Є декілька дублючих потоків, що шлють дані одночасно, тож ми можемо проаналізувати лише один потік -
Key TSTFEED0300|7E3E|0400
Засобами автоматизації проаналізуйте наданий нам лог: hblog.txt
1. Відберіть лише строки з вказаним ключем Key TSTFEED0300|7E3E|0400
2. Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
для кожного випадку де heartbeat більше 31 сек але менше 33 логувало WARNING в файл hb_test.log
для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log
3.Зверніть увагу, що нам для аналізу помилок було б добре знати час, в який помилка відбулася.

Обов’язково включіть результат роботи — файл hb_test.log в PR.

Підказка 1
1. Прочитайте файл по строкам, якщо забули як - зверніться до 12 лекції.
2. Виберіть строки з необхідним значенням:

filtered_log = []
if "key" in "long log string with key":
    filtered_log.append("long log string with key")

Підказка 2
1. Пошук часу у строці можна зробити методом .find("Timestamp ") і повернути наступні 8 символів
2. перетворити строку в час дозволяє метод .strptime("10:00:00", "%H:%M:%S")
3. Значення слід аналізувати парами - від поточного відняти наступне і залогувати (або не залогувати) результат
"""

from datetime import datetime

def analyze_heartbeat_log(input_file: str, output_file: str):
    filtered_log = []
    key = "TSTFEED0300|7E3E|0400"

    # Вибираємо рядки з вказаним ключем
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            if key in line:
                # Знаходимо час після "Timestamp "
                idx = line.find("Timestamp ")
                if idx != -1: # якщо знайдено підрядок з Timestamp
                    time_str = line[idx + 10: idx + 18]  # беремо 8 символів часу HH:MM:SS
                    try:
                        timestamp = datetime.strptime(time_str, "%H:%M:%S")
                        filtered_log.append(timestamp)
                    except ValueError:
                        continue
    print("Filtered timestamps:", [ts.strftime("%H:%M:%S") for ts in filtered_log])

    # Аналіз різниці між сусідніми таймштампами
    with open(output_file, "w", encoding="utf-8") as out:
        for i in range(len(filtered_log) - 1): # перебираємо рядки відфільтровані по Key TSTFEED0300|7E3E|0400 (filtered_log)
            delta = (filtered_log[i] - filtered_log[i + 1]).total_seconds() # записи від новіших до старіших, тому поточне мінус наступне значення

            if 31 < delta < 33:
                out.write(f"[WARNING] Heartbeat {delta:.0f} sec at {filtered_log[i].time()}\n")
            elif delta >= 33:
                out.write(f"[ERROR] Heartbeat {delta:.0f} sec at {filtered_log[i].time()}\n")

if __name__ == "__main__":
    analyze_heartbeat_log(
        input_file="hblog.txt",
        output_file="hb_test.log",
    )