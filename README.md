# 🕷️ Scrapy Parser PEP

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg) ![Scrapy Version](https://img.shields.io/badge/scrapy-2.5.1-green.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg) ![GitHub last commit](https://img.shields.io/github/last-commit/Khoetskiy/scrapy_parser_pep) ![GitHub repo size](https://img.shields.io/github/repo-size/Khoetskiy/scrapy_parser_pep)

**Парсер документации PEP** - проект на Scrapy для сбора и анализа информации о Python Enhancement Proposals (PEP) с официальной документации Python.

## ✨ Возможности

- Парсинг индекса PEP
- Сбор информации о каждом PEP
- Генерация статистики по статусам
- Сохранение результатов в CSV-формате

## ⚙️ Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/khoetskiy/scrapy_parser_pep.git
cd scrapy_parser_pep
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# или
venv\Scripts\activate     # Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

## 🚀 Использование

Для запуска паука и сбора информации о PEP:

```bash
scrapy crawl pep
```

Это создаст два CSV-файла в директории `results`:

- `pep_ДатаВремя.csv` - подробная информация о каждом PEP
- `status_summary_ДатаВремя.csv` - сводка по статусам PEP

## 📁 Структура проекта

```bash
scrapy_parser_pep/
├── pep_parse/
│   ├── spiders/
│   │   └── pep.py         # Основная реализация паука
│   ├── constants.py       # Константы проекта
│   ├── items.py           # Определения элементов
│   ├── middlewares.py     # Промежуточные слои
│   ├── pipelines.py       # Конвейеры обработки данных
│   └── settings.py        # Настройки Scrapy
├── results/               # Директория для CSV-файлов
├── tests/
├── .flake8
├── pyproject.toml
├── pytest.ini
├── requirements.txt
├── scrapy.cfg
├── uv.lock
├── README.md
└── LICENSE
```

## ⚙️ Конфигурация

Поведение проекта настраивается через `settings.py`:

- `FEEDS` - Настройка форматов и путей вывода
- `ITEM_PIPELINES` - Включение/отключение конвейеров обработки

## 🛠️ Технологии

![Scrapy](https://img.shields.io/badge/Scrapy-2.5.1-60A839?style=for-the-badge&logo=scrapy&logoColor=white) ![lxml](https://img.shields.io/badge/lxml-4.8.0-0B4F79?style=for-the-badge&logo=python&logoColor=white) ![Pytest](https://img.shields.io/badge/Pytest-6.2.5-0A9EDC?style=for-the-badge&logo=pytest&logoColor=green) ![Flake8](https://img.shields.io/badge/Flake8-4.0.1-007ACC?style=for-the-badge&logo=python&logoColor=red) ![Ruff](https://img.shields.io/badge/Ruff-0.13.0-000000?style=for-the-badge&logo=ruff&logoColor=purple) ![IPython](https://img.shields.io/badge/IPython-8.18.1-3776AB?style=for-the-badge&logo=ipython&logoColor=white)

Полный список см. в `requirements.txt`

## 🧪 Тесты

Для запуска тестов используйте:

```bash
pytest
```

## 🔍 Линтинг

Проект использует [ruff](https://github.com/astral-sh/ruff) для проверки качества кода. Конфигурация находится в `pyproject.toml`.

Для проверки кода выполните:

```bash
ruff check .
```

## 📄 Лицензия

Проект распространяется под лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

## 👨‍💻 Автор

**GitHub:** [@Khoetskiy](https://github.com/Khoetskiy)
