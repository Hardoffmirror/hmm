# Установка на Windows / Windows Installation

## Шаг 1: Установите необходимое ПО

### Git для Windows
Скачайте и установите Git:
https://git-scm.com/download/win

### Python 3.7 или новее
Скачайте и установите Python:
https://www.python.org/downloads/

**ВАЖНО:** При установке Python обязательно поставьте галочку "Add Python to PATH"!

## Шаг 2: Откройте командную строку (Command Prompt) или PowerShell

Нажмите `Win + R`, введите `cmd` и нажмите Enter

Или нажмите `Win + X` и выберите "Windows PowerShell"

## Шаг 3: Перейдите в папку, куда хотите скачать проект

Например, если хотите скачать в папку `C:\Projects`:

```cmd
cd C:\
mkdir Projects
cd Projects
```

Или в папку на рабочем столе:

```cmd
cd %USERPROFILE%\Desktop
```

## Шаг 4: Клонируйте репозиторий

```cmd
git clone http://127.0.0.1:50445/git/Hardoffmirror/hmm.git
```

Если репозиторий на GitHub/GitLab, замените URL на ваш:
```cmd
git clone https://github.com/YOUR_USERNAME/hmm.git
```

## Шаг 5: Перейдите в папку проекта

```cmd
cd hmm
```

## Шаг 6: Переключитесь на ветку с кодом

```cmd
git checkout claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS
```

## Шаг 7: Установите зависимости Python

```cmd
pip install -r requirements.txt
```

Или если у вас несколько версий Python:

```cmd
python -m pip install -r requirements.txt
```

## Шаг 8: Запустите программу!

### Базовый запуск:
```cmd
python tarot_analyzer.py
```

### С параметрами:
```cmd
python tarot_analyzer.py --league "Standard" --min-profit 10
```

### Показать справку:
```cmd
python tarot_analyzer.py --help
```

---

## Полная последовательность команд (копировать по одной)

Откройте командную строку и выполните:

```cmd
cd %USERPROFILE%\Desktop
git clone http://127.0.0.1:50445/git/Hardoffmirror/hmm.git
cd hmm
git checkout claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS
pip install -r requirements.txt
python tarot_analyzer.py
```

---

## Если возникают ошибки

### "git is not recognized"
Git не установлен или не добавлен в PATH. Установите Git для Windows.

### "python is not recognized"
Python не установлен или не добавлен в PATH. Переустановите Python с галочкой "Add Python to PATH".

### "No module named 'requests'" или "No module named 'tabulate'"
Зависимости не установлены. Выполните:
```cmd
pip install requests tabulate
```

### "Failed to load card data"
Проблема с интернет-соединением или poe.ninja недоступен. Попробуйте позже.

---

## Альтернатива: Использование виртуального окружения (рекомендуется)

Это изолирует зависимости проекта:

```cmd
cd hmm
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python tarot_analyzer.py
```

Для выхода из виртуального окружения:
```cmd
deactivate
```

---

## Примеры использования

### Анализ текущей лиги (замените на актуальное название):
```cmd
python tarot_analyzer.py --league "Settlers"
```

### Показать только очень выгодные карты:
```cmd
python tarot_analyzer.py --min-profit 20 --min-roi 100
```

### Показать больше результатов:
```cmd
python tarot_analyzer.py --limit 50
```

### Комбинация всех параметров:
```cmd
python tarot_analyzer.py --league "Settlers" --min-profit 5 --min-roi 30 --limit 30
```
