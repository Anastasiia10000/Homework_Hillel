# Завдання 1:
# Візміть два файли з теки ideas_for_test/work_with_csv
# порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

import csv
from pathlib import Path

# Шлях до файлів
current_dir = Path(__file__).parent
file1_path = current_dir / "random.csv"
file2_path = current_dir / "random-michaels.csv"
output_file = current_dir / "result_Kalyta.csv"

# Читаємо дані з обох файлів як словники
with file1_path.open(encoding="utf-8") as f1, file2_path.open(encoding="utf-8") as f2:
    reader1 = list(csv.DictReader(f1))
    reader2 = list(csv.DictReader(f2))

# Формуємо аналогічний список колонок
columns_file1 = list(reader1[0].keys()) # беремо порядок колонок з 1го файлу
columns_file2 = list(reader2[0].keys()) # беремо порядок колонок з 2го файлу
extra_columns = [col for col in columns_file2 if col not in columns_file1] # визначаємо всі колонки з 2го файлу, яких немає в 1му
all_columns = columns_file1 + extra_columns # Загальний список колонок 1го файлу + екстра колонка

# Додаємо відсутні колонки в рядках
for row in reader1 + reader2:
    for col in all_columns:
        row.setdefault(col, "")

# Вибираємо для порівняння спільні колонки тільки у 2х файлах
common_columns = list(set(columns_file1) & set(columns_file2))

# Прибираємо дублікати
seen = set()
unique_rows = []
for row in reader1 + reader2:
    row_tuple = tuple(row[col] for col in common_columns)
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_rows.append(row)

# Записуємо результат
with output_file.open(mode="w", newline='', encoding="utf-8") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=all_columns)
    writer.writeheader()
    writer.writerows(unique_rows)

print(f"Result is saved in file: {output_file}")