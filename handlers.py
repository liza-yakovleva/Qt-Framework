"""
Модуль обробки подій.
Містить логіку для обробки клацань кнопок та інших користувацьких взаємодій.
"""

from PySide6.QtWidgets import QLineEdit, QSpinBox, QTextEdit, QMessageBox, QRadioButton
from typing import List, Callable

import config
import utils
from models import SurveyData


class SurveyEventHandler:
    """Клас для обробки подій анкети."""
    
    def __init__(
        self,
        name_edit: QLineEdit,
        age_box: QSpinBox,
        rating_buttons: List[QRadioButton],
        tech_checks: dict,
        comment_edit: QTextEdit,
        parent_widget = None
    ):
        """
        Ініціалізація обробника подій.
        
        Args:
            name_edit: Поле для введення імені
            age_box: Контроль для введення віку
            rating_buttons: Список перемикачів для оцінки
            tech_checks: Словник прапорців для технологій
            comment_edit: Поле для коментарів
            parent_widget: Батьківський віджет для показу діалогів
        """
        self.name_edit = name_edit
        self.age_box = age_box
        self.rating_buttons = rating_buttons
        self.tech_checks = tech_checks
        self.comment_edit = comment_edit
        self.parent_widget = parent_widget
    
    def handle_save(self) -> bool:
        """
        Обробка натискання кнопки збереження.
        Включає валідацію даних, збереження у файл та очищення форми.
        
        Returns:
            bool: True якщо операція успішна, False в іншому випадку
        """
        # Валідація імені
        name_valid, name_error = utils.validate_user_name(self.name_edit.text())
        if not name_valid:
            self._show_error("Помилка", name_error)
            return False
        
        # Валідація віку
        age_valid, age_error = utils.validate_age(self.age_box.value())
        if not age_valid:
            self._show_error("Помилка", age_error)
            return False
        
        # Отримання оцінки
        selected_rating = self._get_selected_rating()
        
        # Валідація оцінки
        rating_valid, rating_error = utils.validate_rating(selected_rating)
        if not rating_valid:
            self._show_error("Помилка", rating_error)
            return False
        
        # Отримання обраних технологій
        selected_tech = utils.format_technologies(self.tech_checks)
        
        # Створення об'єкту даних анкети
        survey_data = SurveyData(
            user_name=self.name_edit.text().strip(),
            age=self.age_box.value(),
            rating=selected_rating,
            technologies=selected_tech,
            comment=self.comment_edit.toPlainText().strip()
        )
        
        # Збереження у файл
        success, message = utils.save_survey_to_file(survey_data)
        
        if success:
            self._show_info("Успіх", message)
            self._clear_form()
            return True
        else:
            self._show_error("Помилка файлової системи", message)
            return False
    
    def _get_selected_rating(self) -> str:
        """
        Отримання обраної оцінки складності.
        
        Returns:
            str: Обрана оцінка або "N/A"
        """
        for rb in self.rating_buttons:
            if rb.isChecked():
                return rb.text()
        return "N/A"
    
    def _clear_form(self) -> None:
        """Очищення всіх полів форми після успішного збереження."""
        self.name_edit.clear()
        self.comment_edit.clear()
        # Встановлення віку на значення за замовчуванням
        self.age_box.setValue(config.DEFAULT_AGE)
        # Встановлення рейтингу на значення за замовчуванням
        for i, rb in enumerate(self.rating_buttons):
            rb.setChecked(i == config.DEFAULT_RATING - 1)
        # Зняття позначень з усіх технологій
        for checkbox in self.tech_checks.values():
            checkbox.setChecked(False)
    
    def _show_error(self, title: str, message: str) -> None:
        """Показ діалогу помилки."""
        QMessageBox.critical(self.parent_widget, title, message)
    
    def _show_info(self, title: str, message: str) -> None:
        """Показ інформаційного діалогу."""
        QMessageBox.information(self.parent_widget, title, message)
