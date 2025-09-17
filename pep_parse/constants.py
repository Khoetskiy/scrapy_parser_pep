from pathlib import Path

BOT_NAME = 'pep_parse'

BASE_DIR = Path(__file__).parent.parent
RESULTS_PATH = 'results'
RESULTS_DIR = BASE_DIR / RESULTS_PATH

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

STATUS_FIELD = 'Статус'
COUNT_FIELD = 'Количество'
