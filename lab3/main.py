import sys
import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QSpinBox, 
                             QGroupBox, QRadioButton, QCheckBox, 
                             QTextEdit, QPushButton, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class SurveyApplication(QMainWindow):
    """
    Клас SurveyApplication реалізує логіку десктопного застосунку для збору 
    анкетних даних користувачів з використанням об'єктно-орієнтованого підходу.
    """
    def __init__(self):
        super().__init__()
        # Встановлення параметрів вікна застосунку
        self.setWindowTitle("Survey Pro v5.0 | High-Contrast Edition")
        self.setMinimumWidth(500)
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        """Метод для ініціалізації об'єктів інтерфейсу та їхнього компонування."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Використання QVBoxLayout для вертикального вирівнювання елементів
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # Заголовок секції
        header = QLabel("Анкета зворотного зв'язку")
        header.setObjectName("header")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)

        # 1. Текстовий ввід (QLineEdit)
        main_layout.addWidget(QLabel("1. Прізвище та ім'я користувача:"))
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Введіть ваше ПІБ...")
        main_layout.addWidget(self.name_edit)

        # 2. Числовий ввід (QSpinBox)
        main_layout.addWidget(QLabel("2. Вкажіть ваш повний вік:"))
        self.age_box = QSpinBox()
        self.age_box.setRange(16, 100)
        self.age_box.setValue(21)
        main_layout.addWidget(self.age_box)

        # 3. Вибір одного варіанту (QRadioButton)
        self.rating_group = QGroupBox("3. Оцініть складність проекту (1-5):")
        rating_layout = QHBoxLayout()
        self.rating_buttons = []
        for i in range(1, 6):
            rb = QRadioButton(str(i))
            if i == 5: rb.setChecked(True)
            self.rating_buttons.append(rb)
            rating_layout.addWidget(rb)
        self.rating_group.setLayout(rating_layout)
        main_layout.addWidget(self.rating_group)

        # 4. Множинний вибір (QCheckBox)
        self.tech_group = QGroupBox("4. Які технології ви вивчаєте?")
        tech_layout = QVBoxLayout()
        self.tech_checks = {
            "Python/Qt": QCheckBox("Python 3 & PySide6 (Qt)"),
            "Git/GitHub": QCheckBox("Система контролю версій Git"),
            "UX/UI": QCheckBox("Принципи дизайну інтерфейсів")
        }
        for check in self.tech_checks.values():
            tech_layout.addWidget(check)
        self.tech_group.setLayout(tech_layout)
        main_layout.addWidget(self.tech_group)

        # 5. Багаторядковий ввід (QTextEdit)
        main_layout.addWidget(QLabel("5. Ваші додаткові пропозиції:"))
        self.comment_edit = QTextEdit()
        self.comment_edit.setPlaceholderText("Напишіть відгук тут...")
        main_layout.addWidget(self.comment_edit)

        # Кнопка збереження результатів
        self.btn_save = QPushButton("ЗБЕРЕГТИ РЕЗУЛЬТАТИ")
        self.btn_save.setCursor(Qt.PointingHandCursor)
        self.btn_save.clicked.connect(self.save_to_file)
        main_layout.addWidget(self.btn_save)

    def apply_styles(self):
        """Застосування таблиць стилів QSS для забезпечення високої контрастності."""
        self.setStyleSheet("""
            /* Головне вікно */
            QMainWindow { background-color: #fcfdfe; }
            
            /* Заголовок */
            #header { font-size: 26px; font-weight: bold; color: #2c3e50; margin-bottom: 10px; }
            
            /* Мітки полів */
            QLabel { font-size: 15px; color: #2c3e50; font-weight: bold; }
            
            /* Елементи вводу - ЧІТКИЙ ЧОРНИЙ ТЕКСТ */
            QLineEdit, QSpinBox, QTextEdit { 
                padding: 10px; border: 2px solid #bdc3c7; border-radius: 6px; 
                background-color: white; 
                color: #000000; /* Чорний колір тексту для максимальної видимості */
                font-size: 15px;
            }
            QLineEdit:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #3498db; }
            
            /* Контейнери груп */
            QGroupBox { 
                font-weight: bold; border: 2px solid #ecf0f1; border-radius: 10px; 
                margin-top: 10px; padding-top: 5px; color: #2c3e50; font-size: 15px;
            }
            QGroupBox::title { subcontrol-origin: margin; left: 15px; padding: 0 5px; background-color: #fcfdfe; }
            
            /* Кнопки вибору */
            QRadioButton, QCheckBox { font-size: 14px; color: #2c3e50; font-weight: 500; }
            
            /* Головна кнопка */
            QPushButton { 
                background-color: #27ae60; color: #ffffff; font-weight: bold; 
                padding: 15px; border-radius: 10px; font-size: 16px; margin-top: 15px;
            }
            QPushButton:hover { background-color: #2ecc71; }
            QPushButton:pressed { background-color: #1e8449; }
        """)

    def save_to_file(self):
        """Обробка введених даних та асинхронний запис у файл на диску."""
        user_name = self.name_edit.text().strip()
        
        # Валідація обов'язкового поля
        if not user_name:
            QMessageBox.critical(self, "Помилка", "Будь ласка, введіть Прізвище та Ім'я!")
            return

        # Збір даних з груп перемикачів
        selected_rating = next((rb.text() for rb in self.rating_buttons if rb.isChecked()), "N/A")
        selected_tech = [name for name, chk in self.tech_checks.items() if chk.isChecked()]
        
        # Формування фінального звіту
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = (
            f"--- Survey Record {timestamp} ---\n"
            f"Користувач: {user_name}\n"
            f"Вік: {self.age_box.value()}\n"
            f"Оцінка складності: {selected_rating}\n"
            f"Технологічний стек: {', '.join(selected_tech) if selected_tech else 'Не обрано'}\n"
            f"Відгук: {self.comment_edit.toPlainText().strip()}\n"
            f"{'='*35}\n"
        )

        try:
            # Запис у файл з використанням кодування UTF-8
            with open("survey_results.txt", "a", encoding="utf-8") as file:
                file.write(output)
            
            QMessageBox.information(self, "Успіх", "Дані успішно записано у файл 'survey_results.txt'")
            self.name_edit.clear()
            self.comment_edit.clear()
        except IOError as e:
            QMessageBox.critical(self, "Помилка файлової системи", f"Не вдалося зберегти файл: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Встановлення стандартного шрифту для всіх віджетів застосунку
    app.setFont(QFont("Segoe UI", 10))
    
    window = SurveyApplication()
    window.show()
    sys.exit(app.exec())