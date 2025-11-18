# PoE Divination Card Price Analyzer / Анализатор цен гадальных карт PoE

## Описание / Description

**RU:** Программа анализирует цены на гадальные карты (divination cards) в Path of Exile и сравнивает их с ценами предметов, которые можно получить из этих карт. Показывает наиболее выгодные возможности для арбитража.

**EN:** A program that analyzes prices for divination cards in Path of Exile and compares them with prices of items obtainable from these cards. Shows the most profitable arbitrage opportunities.

## Функции / Features

- Получение актуальных цен с poe.ninja API
- Расчет прибыли от покупки карт → получения предмета → продажи
- Учет стоимости полного набора карт
- Фильтрация по минимальной прибыли
- Сортировка по ROI (Return on Investment)

## Установка / Installation

```bash
pip install -r requirements.txt
```

## Использование / Usage

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

## Примечания / Notes

Цены берутся с poe.ninja и могут отличаться от реальных цен на торговой площадке. Используйте данные как ориентир для поиска возможностей.
