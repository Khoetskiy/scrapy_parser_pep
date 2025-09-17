import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

from pep_parse.constants import (
    BASE_DIR,
    COUNT_FIELD,
    DATE_FORMAT,
    STATUS_FIELD,
)


class PepParsePipeline:
    def __init__(self) -> None:
        self.status_counter = Counter()

    def open_spider(self, spider):
        """Метод вызывается при старте паука. Сейчас не используется."""

    def process_item(self, item, spider):
        """Увеличивает счётчик для статуса PEP."""
        status = item['status']
        if status:
            self.status_counter[status] += 1
        return item

    def close_spider(self, spider):
        """Создает csv файл с данными о количестве статусов."""
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = datetime.now().strftime(DATE_FORMAT)
        filename = results_dir / f'status_summary_{now}.csv'

        with Path(filename).open('w', encoding='utf-8', newline='') as f:
            fieldnames = [STATUS_FIELD, COUNT_FIELD]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            total_count = sum(self.status_counter.values())
            for status, count in sorted(self.status_counter.items()):
                writer.writerow({STATUS_FIELD: status, COUNT_FIELD: count})
            writer.writerow({STATUS_FIELD: 'Total', COUNT_FIELD: total_count})
