"""
Модуль моделей даних.
Містить структури для зберігання даних анкети.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class SurveyData:
    """
    Модель даних анкети.
    
    Атрибути:
        user_name: Прізвище та ім'я користувача
        age: Вік користувача
        rating: Оцінка складності (1-5)
        technologies: Список обраних технологій
        comment: Додаткові пропозиції
        timestamp: Час заповнення анкети
    """
    user_name: str
    age: int
    rating: str
    technologies: List[str]
    comment: str
    timestamp: datetime = None
    
    def __post_init__(self):
        """Встановлення часової мітки за замовчуванням, якщо не задана."""
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def to_string(self) -> str:
        """
        Форматування даних анкети для їх збереження у файл.
        
        Returns:
            str: Відформатований рядок з даними анкети
        """
        timestamp_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        tech_str = ", ".join(self.technologies) if self.technologies else "Не обрано"
        
        return (
            f"--- Survey Record {timestamp_str} ---\n"
            f"Користувач: {self.user_name}\n"
            f"Вік: {self.age}\n"
            f"Оцінка складності: {self.rating}\n"
            f"Технологічний стек: {tech_str}\n"
            f"Відгук: {self.comment}\n"
            f"{'='*35}\n"
        )
