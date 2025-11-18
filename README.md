# PoE Divination Card Price Analyzer / Анализатор цен гадальных карт PoE

## Описание / Description

**RU:** Программа анализирует цены на гадальные карты (divination cards) в Path of Exile и сравнивает их с ценами предметов, которые можно получить из этих карт. Показывает наиболее выгодные возможности для арбитража.

**EN:** A program that analyzes prices for divination cards in Path of Exile and compares them with prices of items obtainable from these cards. Shows the most profitable arbitrage opportunities.

## Функции / Features

- 🌐 **Веб-интерфейс** - удобный интерфейс в браузере
- 💻 **CLI версия** - для командной строки
- ⚡ **Автоопределение лиг** - автоматически определяет актуальные лиги из poe.ninja
- 📊 Получение актуальных цен с poe.ninja API
- 💰 Расчет прибыли от покупки карт → получения предмета → продажи
- 📦 Учет стоимости полного набора карт
- 🔍 Фильтрация по минимальной прибыли и ROI
- 📈 Статистика и визуализация результатов
- 🔄 Кнопка обновления списка лиг

## Установка / Installation

### 🪟 Windows
**Подробная инструкция:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md)

**Быстрый старт:**
1. Скачайте и установите [Python](https://www.python.org/downloads/) (отметьте "Add Python to PATH")
2. Скачайте и установите [Git для Windows](https://git-scm.com/download/win)
3. Откройте командную строку (cmd) и выполните:
```cmd
cd %USERPROFILE%\Desktop
git clone <URL_репозитория>
cd hmm
git checkout claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS
pip install -r requirements.txt
python tarot_analyzer.py
```

**Или дважды кликните на файл:** `install_and_run.bat`

### 🐧 Linux / 🍎 macOS
```bash
pip install -r requirements.txt
```

## Использование / Usage

### 🌐 Веб-интерфейс (рекомендуется)

**Windows:**
```cmd
run_web.bat
```
Или:
```cmd
python web_app.py
```

**Linux/macOS:**
```bash
python3 web_app.py
```

Браузер откроется автоматически на `http://127.0.0.1:5000`

### 💻 Командная строка (CLI)

```bash
# Показать топ-20 самых выгодных карт
python tarot_analyzer.py

# Показать карты с минимальной прибыльностью 10 chaos
python tarot_analyzer.py --min-profit 10

# Выбрать лигу
python tarot_analyzer.py --league "Standard"

# Показать больше результатов
python tarot_analyzer.py --limit 50
```

## Требования / Requirements

- Python 3.7+
- requests
- tabulate
- flask (для веб-интерфейса)

## Дополнительная информация / Additional Info

- **[LEAGUES.md](LEAGUES.md)** - Подробная информация о динамическом определении лиг
- **[WINDOWS_INSTALL.md](WINDOWS_INSTALL.md)** - Установка на Windows
- **[UPDATE.md](UPDATE.md)** - Команды для обновления проекта
- **[QUICKSTART.md](QUICKSTART.md)** - Быстрый старт и примеры

## Примечания / Notes

Цены берутся с poe.ninja и могут отличаться от реальных цен на торговой площадке. Используйте данные как ориентир для поиска возможностей.

### Автоматическое определение лиг
Веб-интерфейс автоматически загружает список актуальных лиг с poe.ninja при запуске. Используйте кнопку 🔄 для ручного обновления списка.
