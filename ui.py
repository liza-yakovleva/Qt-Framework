"""
Модуль побудови користувацького інтерфейсу.
Містить методи для ініціалізації всіх UI компонентів.
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QSpinBox, QGroupBox, QRadioButton, QCheckBox, QTextEdit, QPushButton
)
from PySide6.QtCore import Qt

import config


class UIBuilder:
    """Клас для побудови компонентів інтерфейсу."""
    
    @staticmethod
    def create_header() -> QLabel:
        """Створення заголовка анкети."""
        header = QLabel("Анкета зворотного зв'язку")
        header.setObjectName("header")
        header.setAlignment(Qt.AlignCenter)
        return header
    
    @staticmethod
    def create_name_input() -> QLineEdit:
        """Створення поля для введення імені."""
        name_edit = QLineEdit()
        name_edit.setPlaceholderText("Введіть ваше ПІБ...")
        return name_edit
    
    @staticmethod
    def create_age_spinner() -> QSpinBox:
        """Створення контролю для введення віку."""
        age_box = QSpinBox()
        age_box.setRange(config.MIN_AGE, config.MAX_AGE)
        age_box.setValue(config.DEFAULT_AGE)
        return age_box
    
    @staticmethod
    def create_rating_group() -> tuple:
        """
        Створення групи перемикачів для оцінки складності.
        
        Returns:
            Кортеж (group_box, list_of_radio_buttons)
        """
        rating_group = QGroupBox(f"3. Оцініть складність проекту ({config.RATING_MIN}-{config.RATING_MAX}):")
        rating_layout = QHBoxLayout()
        rating_buttons = []
        
        for i in range(config.RATING_MIN, config.RATING_MAX + 1):
            rb = QRadioButton(str(i))
            if i == config.DEFAULT_RATING:
                rb.setChecked(True)
            rating_buttons.append(rb)
            rating_layout.addWidget(rb)
        
        rating_group.setLayout(rating_layout)
        return rating_group, rating_buttons
    
    @staticmethod
    def create_technology_group() -> tuple:
        """
        Створення групи прапорців для технологій.
        
        Returns:
            Кортеж (group_box, dict_of_checkboxes)
        """
        tech_group = QGroupBox("4. Які технології ви вивчаєте?")
        tech_layout = QVBoxLayout()
        tech_checks = {}
        
        for tech_key, tech_label in config.TECHNOLOGIES.items():
            checkbox = QCheckBox(tech_label)
            tech_checks[tech_key] = checkbox
            tech_layout.addWidget(checkbox)
        
        tech_group.setLayout(tech_layout)
        return tech_group, tech_checks
    
    @staticmethod
    def create_comment_input() -> QTextEdit:
        """Створення поля для введення коментарів."""
        comment_edit = QTextEdit()
        comment_edit.setPlaceholderText("Напишіть відгук тут...")
        return comment_edit
    
    @staticmethod
    def create_save_button() -> QPushButton:
        """Створення кнопки для збереження результатів."""
        btn_save = QPushButton("ЗБЕРЕГТИ РЕЗУЛЬТАТИ")
        btn_save.setCursor(Qt.PointingHandCursor)
        return btn_save


def build_main_layout(
    header: QLabel,
    name_edit: QLineEdit,
    age_box: QSpinBox,
    rating_group: QGroupBox,
    tech_group: QGroupBox,
    comment_edit: QTextEdit,
    save_button: QPushButton
) -> QVBoxLayout:
    """
    Побудова основного макету вікна.
    
    Args:
        header: Заголовок
        name_edit: Поле для введення імені
        age_box: Контроль виду spinner для віку
        rating_group: Група для оцінки
        tech_group: Група для технологій
        comment_edit: Поле для коментарів
        save_button: Кнопка збереження
        
    Returns:
        Основний макет (QVBoxLayout)
    """
    main_layout = QVBoxLayout()
    main_layout.setSpacing(15)
    main_layout.setContentsMargins(30, 30, 30, 30)
    
    # Заголовок
    main_layout.addWidget(header)
    
    # 1. Текстовий ввід
    main_layout.addWidget(QLabel("1. Прізвище та ім'я користувача:"))
    main_layout.addWidget(name_edit)
    
    # 2. Числовий ввід
    main_layout.addWidget(QLabel("2. Вкажіть ваш повний вік:"))
    main_layout.addWidget(age_box)
    
    # 3. Вибір одного варіанту
    main_layout.addWidget(rating_group)
    
    # 4. Множинний вибір
    main_layout.addWidget(tech_group)
    
    # 5. Багаторядковий ввід
    main_layout.addWidget(QLabel("5. Ваші додаткові пропозиції:"))
    main_layout.addWidget(comment_edit)
    
    # Кнопка
    main_layout.addWidget(save_button)
    
    return main_layout
