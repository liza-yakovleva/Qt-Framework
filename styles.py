"""
Модуль стилів застосунку.
Містить всі стилі QSS для оформлення інтерфейсу.
"""

STYLESHEET = """
    /* Головне вікно */
    QMainWindow { background-color: #fcfdfe; }
    
    /* Заголовок */
    #header { 
        font-size: 26px; 
        font-weight: bold; 
        color: #2c3e50; 
        margin-bottom: 10px; 
    }
    
    /* Мітки полів */
    QLabel { 
        font-size: 15px; 
        color: #2c3e50; 
        font-weight: bold; 
    }
    
    /* Елементи вводу - ЧІТКИЙ ЧОРНИЙ ТЕКСТ */
    QLineEdit, QSpinBox, QTextEdit { 
        padding: 10px; 
        border: 2px solid #bdc3c7; 
        border-radius: 6px; 
        background-color: white; 
        color: #000000;
        font-size: 15px;
    }
    
    QLineEdit:focus, QSpinBox:focus, QTextEdit:focus { 
        border: 2px solid #3498db; 
    }
    
    /* Контейнери груп */
    QGroupBox { 
        font-weight: bold; 
        border: 2px solid #ecf0f1; 
        border-radius: 10px; 
        margin-top: 10px; 
        padding-top: 5px; 
        color: #2c3e50; 
        font-size: 15px;
    }
    
    QGroupBox::title { 
        subcontrol-origin: margin; 
        left: 15px; 
        padding: 0 5px; 
        background-color: #fcfdfe; 
    }
    
    /* Кнопки вибору */
    QRadioButton, QCheckBox { 
        font-size: 14px; 
        color: #2c3e50; 
        font-weight: 500; 
    }
    
    /* Головна кнопка */
    QPushButton { 
        background-color: #27ae60; 
        color: #ffffff; 
        font-weight: bold; 
        padding: 15px; 
        border-radius: 10px; 
        font-size: 16px; 
        margin-top: 15px;
    }
    
    QPushButton:hover { 
        background-color: #2ecc71; 
    }
    
    QPushButton:pressed { 
        background-color: #1e8449; 
    }
"""
