# DEVELOPMENT.md - Гайд для розробників

## 🚀 Додавання нової функціональності

### Як додати нове питання в анкету?

#### Крок 1: Додайте константу в `config.py`

```python
# Приклад для нового питання про емейл
DEFAULT_EMAIL = "user@example.com"
```

#### Крок 2: Додайте метод в `ui.py`

В класс `UIBuilder` додайте:

```python
@staticmethod
def create_email_input() -> QLineEdit:
    """Створення поля для введення email."""
    email_edit = QLineEdit()
    email_edit.setPlaceholderText("Введіть свій email...")
    return email_edit
```

#### Крок 3: Обновіть макет в `ui.py`

В функцію `build_main_layout()` додайте:

```python
# Після коментарю
main_layout.addWidget(QLabel("6. Ваш email адреса:"))
main_layout.addWidget(email_edit)
```

#### Крок 4: Обновіть модель в `models.py`

В dataclass `SurveyData` додайте поле:

```python
@dataclass
class SurveyData:
    # ... існуючі поля ...
    email: str
```

Обновіть метод `to_string()`:

```python
f"Email: {self.email}\n"
```

#### Крок 5: Додайте валідацію в `utils.py`

```python
def validate_email(email: str) -> Tuple[bool, str]:
    """Валідація email адреси."""
    if not email or not "@" in email:
        return False, "Введіть правильний email!"
    return True, ""
```

#### Крок 6: Обновіть обробник в `handlers.py`

В метод `handle_save()` додайте валідацію:

```python
email_valid, email_error = utils.validate_email(email)
```

---

## 🎨 Змінення дизайну

### Як змінити кольори?

Редагуйте файл `styles.py` - жоден інший файл не потребує змін!

Приклад:
```python
# Змініть цей блок
#header { 
    font-size: 26px; 
    color: #2c3e50;  # ← Змініть колір на інший HEX код
}
```

### Як змінити розмір вікна?

В `config.py`:
```python
WINDOW_MIN_WIDTH = 600  # Було 500
```

### Як змінити шрифт?

В `config.py`:
```python
DEFAULT_FONT_FAMILY = "Arial"  # Було "Segoe UI"
DEFAULT_FONT_SIZE = 12  # Було 10
```

---

## 🧪 Тестування

### Як тестувати валідацію?

```python
# test_validation.py
import utils

def test_validate_user_name():
    # Тест 1: Пусте ім'я
    is_valid, error = utils.validate_user_name("")
    assert not is_valid
    assert "введіть" in error.lower()
    
    # Тест 2: Дуже коротке ім'я
    is_valid, error = utils.validate_user_name("Ан")
    assert not is_valid
    
    # Тест 3: Правильне ім'я
    is_valid, error = utils.validate_user_name("Яковлева Єлизавета")
    assert is_valid
    assert error == ""
```

### Як тестувати I/O операції?

```python
import tempfile
import os

def test_save_survey():
    from models import SurveyData
    import utils
    
    survey = SurveyData(
        user_name="Тест",
        age=25,
        rating="5",
        technologies=["Python/Qt"],
        comment="Тестовий коментар"
    )
    
    # Логіка тесту
    success, message = utils.save_survey_to_file(survey)
    assert success
```

---

## 📊 Розширення функціональності

### Як додати експорт в CSV?

1. Додайте функцію в `utils.py`:

```python
import csv

def export_to_csv(surveys: List[SurveyData], filename: str) -> Tuple[bool, str]:
    """Експорт результатів у CSV."""
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Користувач', 'Вік', 'Оцінка', 'Технології', 'Коментар'])
            for survey in surveys:
                writer.writerow([
                    survey.user_name,
                    survey.age,
                    survey.rating,
                    ', '.join(survey.technologies),
                    survey.comment
                ])
        return True, "Експортовано успішно"
    except IOError as e:
        return False, f"Помилка: {e}"
```

2. Додайте кнопку в `ui.py`:

```python
btn_export = QPushButton("ЕКСПОРТУВАТИ CSV")
main_layout.addWidget(btn_export)
```

3. Обробите подію в `handlers.py`:

```python
self.btn_export.clicked.connect(self.handle_export)
```

---

## 🔧 Debugging і логування

### Як додати логування?

```python
import logging

# В main.py додайте
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Застосунок запущено")
```

### Як знайти помилки?

1. Перевірте консоль при запуску:
```bash
python main.py
```

2. Додайте print-statements для debug:
```python
print(f"DEBUG: {variable_name} = {variable_value}")
```

3. Використовуйте debugger VS Code:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

---

## 📦 Архітектурні рішення

### Чому dataclass для SurveyData?

```python
# ❌ Без dataclass (старий спосіб)
class SurveyData:
    def __init__(self, user_name, age, rating, technologies, comment):
        self.user_name = user_name
        self.age = age
        self.rating = rating
        # ... багато стереотипного коду ...

# ✅ З dataclass (сучасний спосіб)
@dataclass
class SurveyData:
    user_name: str
    age: int
    rating: str
    technologies: List[str]
    comment: str
```

Переваги:
- Менше коду
- Автоматичний `__init__`, `__repr__`, `__eq__`
- Type hints
- Légко додавати/видаляти поля

### Чому UIBuilder pattern?

```python
# ✅ UIBuilder - централізований контроль
header = UIBuilder.create_header()
name = UIBuilder.create_name_input()

# ❌ Дублювання коду (без UIBuilder)
header = QLabel("Анкета")
header.setObjectName("header")  # Забув де-то - помилка!
```

Чому це краще:
- Логіка створення в одному місці
- Легко змінювати (один раз змінили - всюди оновилось)
- Type hints для кожного компонента

---

## 🚀 Production-ready checklist

Перед випуском нової версії перевірте:

- [ ] Всі функції задокументовані (docstrings)
- [ ] Код пройшов через linter (pylint)
- [ ] Всі тести проходять (unittest)
- [ ] Немає hardcoded значень (окрім config.py)
- [ ] Error handling на місці (try-except)
- [ ] Логування налаштовано
- [ ] README оновлено
- [ ] CHANGELOG оновлено
- [ ] Версія збільшена в config.py
- [ ] Git commits написані зрозуміло

---

## 📞 Контакти для питань

Якщо у вас є питання щодо розробки:

1. Перевірте README.md
2. Прочитайте docstrings у коді
3. Перевірте CHANGELOG для історії змін
4. Запитайте у Яковлевої Єлизавети Дмитрівни
