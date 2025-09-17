import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

from pep_parse.constants import (
    COUNT_FIELD,
    DATETIME_FORMAT,
    RESULTS_DIR,
    STATUS_FIELD,
)


class PepParsePipeline:
    """
    Пайплайн для обработки и сохранения данных о статусах PEP.

    Подсчитывает количество PEP в каждом статусе и сохраняет
    результаты в CSV-файл в директории results.
    """

    def __init__(self) -> None:
        RESULTS_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        """Инициализирует счетчик статусов при старте паука."""
        self.status_counter = Counter()

    def process_item(self, item, spider):
        """Обрабатывает каждый PEP и подсчитывает статусы."""
        status = item['status']
        if status:
            self.status_counter[status] += 1
        return item

    def close_spider(self, spider):
        """
        Сохраняет статистику по статусам PEP в CSV-файл.

        Создает CSV-файл в формате:
        - Первый столбец: Статус PEP
        - Второй столбец: Количество PEP в данном статусе
        - Последняя строка содержит общее количество PEP
        """
        now = datetime.now().strftime(DATETIME_FORMAT)
        filename = RESULTS_DIR / f'status_summary_{now}.csv'

        with Path(filename).open('w', encoding='utf-8', newline='') as f:
            fieldnames = [STATUS_FIELD, COUNT_FIELD]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            rows = [
                {STATUS_FIELD: status, COUNT_FIELD: count}
                for status, count in sorted(self.status_counter.items())
            ]
            rows.append(
                {
                    STATUS_FIELD: 'Total',
                    COUNT_FIELD: sum(self.status_counter.values()),
                }
            )
            writer.writerows(rows)
