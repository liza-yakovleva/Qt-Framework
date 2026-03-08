"""
Модуль утилітарних функцій.
Містить функції для валідації, форматування та роботи з файлами.
"""

from typing import List, Tuple
import config
from models import SurveyData


def validate_user_name(name: str) -> Tuple[bool, str]:
    """
    Валідація імені користувача.
    
    Args:
        name: Строка з іменем користувача
        
    Returns:
        Кортеж (is_valid, error_message)
    """
    if not name or not name.strip():
        return False, "Будь ласка, введіть Прізвище та Ім'я!"
    
    if len(name.strip()) < 3:
        return False, "Ім'я повинно містити щонайменше 3 символи!"
    
    return True, ""


def validate_age(age: int) -> Tuple[bool, str]:
    """
    Валідація віку користувача.
    
    Args:
        age: Вік користувача
        
    Returns:
        Кортеж (is_valid, error_message)
    """
    if age < config.MIN_AGE or age > config.MAX_AGE:
        return False, f"Вік повинен бути між {config.MIN_AGE} та {config.MAX_AGE} роками!"
    
    return True, ""


def validate_rating(rating: str) -> Tuple[bool, str]:
    """
    Валідація оцінки складності.
    
    Args:
        rating: Оцінка складності
        
    Returns:
        Кортеж (is_valid, error_message)
    """
    if rating == "N/A" or not rating:
        return False, "Будь ласка, виберіть оцінку складності!"
    
    return True, ""


def save_survey_to_file(survey_data: SurveyData) -> Tuple[bool, str]:
    """
    Збереження даних анкети у файл.
    
    Args:
        survey_data: Об'єкт SurveyData з даними анкети
        
    Returns:
        Кортеж (success, message)
    """
    try:
        with open(config.OUTPUT_FILE, "a", encoding=config.FILES_ENCODING) as file:
            file.write(survey_data.to_string())
        return True, "Дані успішно записано у файл 'survey_results.txt'"
    except IOError as e:
        return False, f"Не вдалося зберегти файл: {e}"


def format_technologies(tech_dict: dict) -> List[str]:
    """
    Форматування списку обраних технологій.
    
    Args:
        tech_dict: Словник з технологіями та їх станом перевірки
        
    Returns:
        Список назв обраних технологій
    """
    return [key for key, checkbox in tech_dict.items() if checkbox.isChecked()]
