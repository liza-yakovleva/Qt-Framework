"""
Модуль конфігурації застосунку.
Містить константи та глобальні налаштування.
"""

# Вікно
WINDOW_TITLE = "Survey Pro v5.0 | High-Contrast Edition"
WINDOW_MIN_WIDTH = 500

# Валідація
MIN_AGE = 16
MAX_AGE = 100
DEFAULT_AGE = 21

# Рейтинги
RATING_MIN = 1
RATING_MAX = 5
DEFAULT_RATING = 5

# Технології
TECHNOLOGIES = {
    "Python/Qt": "Python 3 & PySide6 (Qt)",
    "Git/GitHub": "Система контролю версій Git",
    "UX/UI": "Принципи дизайну інтерфейсів"
}

# Файли
OUTPUT_FILE = "survey_results.txt"
FILES_ENCODING = "utf-8"

# Шрифти
DEFAULT_FONT_FAMILY = "Segoe UI"
DEFAULT_FONT_SIZE = 10
