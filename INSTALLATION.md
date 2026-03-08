# INSTALLATION.md - Інструкція з встановлення

## 🖥️ Системні вимоги

| Компонент | Мінімум | Рекомендовано |
|-----------|---------|--------------|
| **ОС** | Windows 7, Ubuntu 18.04, macOS 10.13 | Windows 10+, Ubuntu 20.04+, macOS 11+ |
| **Python** | 3.8 | 3.10+ |
| **RAM** | 512 MB | 2 GB+ |
| **Місце на диску** | 100 MB | 500 MB+ |

---

## 📥 Встановлення Python

### Windows

1. Завантажте Python з [python.org](https://www.python.org/downloads/)
2. Запустіть інсталятор
3. **ВАЖЛИВО:** Позначте "Add Python to PATH"
4. Натисніть "Install Now"

Перевірка успішного встановлення:

```powershell
python --version
# Має вивести: Python 3.x.x
```

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

### macOS

```bash
brew install python3
python3 --version
```

---

## 🔧 Встановлення проекту

### Варіант 1: Із файлу requirements.txt (РЕКОМЕНДОВАНО)

```bash
# Перейдіть до папки проекту
cd "l:\LIZA\KNU\SEMESTER_8\РІК\lab3"

# Встановіть залежності
pip install -r requirements.txt
```

### Варіант 2: Ручне встановлення

```bash
pip install PySide6
```

### Варіант 3: Встановлення конкретної версії

```bash
# PySide6 версія 6.4.0
pip install PySide6==6.4.0

# Найновіша версія
pip install --upgrade PySide6
```

---

## ✅ Перевірка встановлення

### Крок 1: Перевірте Python

```powershell
python --version
# Очікуваний вивід: Python 3.8+ (наприклад, Python 3.11.0)
```

### Крок 2: Перевірте pip

```powershell
pip --version
# Очікуваний вивід: pip x.x.x from ...
```

### Крок 3: Перевірте PySide6

```powershell
python -c "import PySide6; print(PySide6.__version__)"
# Очікуваний вивід: 6.x.x
```

### Крок 4: Запустіть проект

```powershell
python main.py
```

Якщо вікно програми відкрилось - все встановлено правильно! ✅

---

## 🐛 Вирішення проблем при встановленні

### Проблема 1: "command not found: python"

**Причина:** Python не додан до PATH

**Рішення для Windows:**
```powershell
# Перевстановіть Python та позначте "Add Python to PATH"
# або встановіть вручну:
setx PATH "%PATH%;C:\Users\YourName\AppData\Local\Programs\Python\Python311"
```

**Рішення для Linux/Mac:**
```bash
# Перевірте як встановлено
which python3
# Створіть symlink
sudo ln -s /usr/bin/python3 /usr/bin/python
```

---

### Проблема 2: "No module named PySide6"

**Причина:** PySide6 не встановлена

**Рішення:**
```powershell
pip install --upgrade pip
pip install PySide6

# або якщо вищеописане не допомогло
pip install PySide6 --prefer-binary
```

---

### Проблема 3: "Permission denied" при встановленні

**Причина:** Недостатньо прав користувача

**Рішення для Windows:**
- Запустіть PowerShell як адміністратор
- Повторіть встановлення

**Рішення для Linux/Mac:**
```bash
# Встановіть для поточного користувача (БЕЗ sudo!)
pip install --user PySide6

# або використайте virtual environment
python3 -m venv venv
source venv/bin/activate  # На macOS/Linux
# або
venv\Scripts\activate  # На Windows
pip install PySide6
```

---

### Проблема 4: Visual C++ Runtime помилка (Windows)

**Повідомлення:**
```
Microsoft Visual C++ 14.0 or greater is required
```

**Рішення:**
1. Завантажте [Visual C++ Build Tools](https://visualstudio.microsoft.com/downloads/)
2. Встановіть з опцією "Desktop development with C++"
3. Перезавантажте комп'ютер
4. Повторіть встановлення PySide6

---

### Проблема 5: SSL Certificate Error

**Помилка:**
```
SSL: CERTIFICATE_VERIFY_FAILED
```

**Рішення:**
```powershell
pip install --trusted-host pypi.python.org PySide6
```

---

## 🔄 Virtual Environment (Рекомендовано)

Virtual Environment ізолює залежності вашого проекту від системи.

### Создание virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Встановлення залежностей у venv

```bash
pip install -r requirements.txt
```

### Деактивація venv

```bash
deactivate
```

---

## 📊 Перевірка версій всіх компонентів

Створіть файл `check_versions.py`:

```python
#!/usr/bin/env python3
"""Скрипт для перевірки версій всіх компонентів."""

import sys

print(f"Python: {sys.version}")
print(f"Python executable: {sys.executable}")

try:
    import PySide6
    print(f"PySide6: {PySide6.__version__}")
    print("✅ PySide6 встановлена правильно")
except ImportError:
    print("❌ PySide6 не встановлена!")
    sys.exit(1)

print("\n✅ Всі компоненти встановлені успішно!")
```

Запустіть:
```bash
python check_versions.py
```

---

## 🚀 Видалення встановленого

Якщо потрібно видалити проект та залежності:

```bash
# Видалити тільки PySide6
pip uninstall PySide6

# Видалити всі залежності
pip uninstall -r requirements.txt

# Видалити entire venv (якщо використовували)
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows
```

---

## 🌐 Установка без інтернету

Якщо у вас немає інтернету на комп'ютері, де запускається програма:

### На комп'ютері з інтернетом:

```bash
pip download -r requirements.txt -d ./packages
```

### На комп'ютері без інтернету:

```bash
# Скопіюйте папку packages
pip install --no-index --find-links ./packages PySide6
```

---

## 💡 Рекомендовані інструменти

### Для розробки:

- **PyCharm Community Edition** - IDE для Python
- **Visual Studio Code** - Легкий редактор з розширеннями
- **Git** - Контроль версій

### Для тестування:

```bash
# Встановіть додаткові інструменти
pip install pytest  # Тестування
pip install pylint  # Linting
pip install black   # Code formatting
```

---

## ❓ Частозадавані запитання

**Q: Яку версію Python використовувати?**  
A: 3.10 або 3.11 - найстабільніші. 3.8 мінімальна вимога.

**Q: Чи потрібна Unix/Linux для запуску?**  
A: Ні, PySide6 комплексує Windows, Linux, і macOS.

**Q: Чи можу я використовувати PyCharm Community Edition?**  
A: Так, вона повністю безкоштовна та має хорошу підтримку Python і PySide6.

**Q: Де шукати документацію PySide6?**  
A: https://doc.qt.io/qtforpython/

---

## 🆘 Якщо нічого не допомагає

1. Переустановіть Python повністю
2. Видаліть всі Python папки з PATH
3. Перезавантажте комп'ютер
4. Встановіть Python заново
5. Встановіть PySide6 в чистому virtual environment

Якщо все ще не работает - можливо у вас застарілий ОС. Зверніться до системного адміністратора.
