# Завдання 3:
# Для файла ideas_for_test/work_with_xml/groups.xml
# створіть функцію пошуку по group/number і повернення значення timingExbytes/incoming
# результат виведіть у консоль через логер на рівні інфо

import logging
from pathlib import Path
import xml.etree.ElementTree as ET

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def get_incoming_timing_by_group_number(xml_path: Path, group_number: int) -> str | None:
    # Парсимо xml
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Ітеруємо по групах
    for group in root.findall('group'):
        number_elem = group.find('number')
        if number_elem is not None and number_elem.text == str(group_number):
            timing = group.find('timingExbytes')
            if timing is not None:
                incoming = timing.find('incoming')
                if incoming is not None:
                    return incoming.text
            break
    return None

if __name__ == '__main__':
    xml_file = Path('groups.xml')
    for group_num in range(-1, 7):
        incoming_value = get_incoming_timing_by_group_number(xml_file, group_num)

        if incoming_value:
            logger.info(f'Group number {group_num} incoming timing: {incoming_value}')
        else:
            logger.info(f'Incoming timing not found for group number {group_num}')