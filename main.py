"""
Основний модуль застосунку Survey Pro.
Точка входу для десктопного застосунку для збору анкетних даних.
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QFont

import config
from styles import STYLESHEET
from ui import UIBuilder, build_main_layout
from handlers import SurveyEventHandler


class SurveyApplication(QMainWindow):
    """
    Головний класс застосунку для збору анкетних даних.
    
    Інтегрує користувацький інтерфейс, обробку подій та збереження даних.
    """
    
    def __init__(self):
        """Ініціалізація головного вікна застосунку."""
        super().__init__()
        self._init_window()
        self._setup_ui()
        self._apply_styles()
        self._setup_event_handlers()
    
    def _init_window(self) -> None:
        """Налаштування параметрів головного вікна."""
        self.setWindowTitle(config.WINDOW_TITLE)
        self.setMinimumWidth(config.WINDOW_MIN_WIDTH)
    
    def _setup_ui(self) -> None:
        """Побудова користувацького інтерфейсу."""
        # Створення центрального віджета
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Побудова компонентів інтерфейсу
        self.header = UIBuilder.create_header()
        self.name_edit = UIBuilder.create_name_input()
        self.age_box = UIBuilder.create_age_spinner()
        self.rating_group, self.rating_buttons = UIBuilder.create_rating_group()
        self.tech_group, self.tech_checks = UIBuilder.create_technology_group()
        self.comment_edit = UIBuilder.create_comment_input()
        self.btn_save = UIBuilder.create_save_button()
        
        # Побудова макету
        main_layout = build_main_layout(
            header=self.header,
            name_edit=self.name_edit,
            age_box=self.age_box,
            rating_group=self.rating_group,
            tech_group=self.tech_group,
            comment_edit=self.comment_edit,
            save_button=self.btn_save
        )
        
        central_widget.setLayout(main_layout)
    
    def _apply_styles(self) -> None:
        """Застосування таблиці стилів QSS."""
        self.setStyleSheet(STYLESHEET)
    
    def _setup_event_handlers(self) -> None:
        """Налаштування обробників подій."""
        event_handler = SurveyEventHandler(
            name_edit=self.name_edit,
            age_box=self.age_box,
            rating_buttons=self.rating_buttons,
            tech_checks=self.tech_checks,
            comment_edit=self.comment_edit,
            parent_widget=self
        )
        self.btn_save.clicked.connect(event_handler.handle_save)


def main():
    """Точка входу для застосунку."""
    app = QApplication(sys.argv)
    
    # Встановлення шрифту за замовчуванням
    app.setFont(QFont(config.DEFAULT_FONT_FAMILY, config.DEFAULT_FONT_SIZE))
    
    # Створення та показ головного вікна
    window = SurveyApplication()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()