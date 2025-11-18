# Быстрый старт / Quick Start

## Установка / Installation

1. Клонируйте репозиторий / Clone the repository:
```bash
git clone <repository-url>
cd hmm
```

2. (Опционально) Создайте виртуальное окружение / (Optional) Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или / or
venv\Scripts\activate  # Windows
```

3. Установите зависимости / Install dependencies:
```bash
pip install -r requirements.txt
```

## Первый запуск / First Run

Запустите анализатор с параметрами по умолчанию:
Run analyzer with default parameters:

```bash
python tarot_analyzer.py
```

Это покажет топ-20 самых выгодных гадальных карт в стандартной лиге.
This will show top 20 most profitable divination cards in Standard league.

## Примеры / Examples

### Анализ текущей лиги
**ВАЖНО:** Замените "Standard" на название текущей лиги (например, "Settlers", "Affliction" и т.д.)

```bash
python tarot_analyzer.py --league "Settlers"
```

### Фильтр по минимальной прибыли
Показать только карты, где прибыль от полного набора больше 10 chaos:

```bash
python tarot_analyzer.py --min-profit 10
```

### Фильтр по ROI
Показать только карты с рентабельностью выше 50%:

```bash
python tarot_analyzer.py --min-roi 50
```

### Комбинация параметров
Найти карты в текущей лиге с прибылью >5 chaos и ROI >20%, показать топ-30:

```bash
python tarot_analyzer.py --league "Settlers" --min-profit 5 --min-roi 20 --limit 30
```

## Понимание результатов / Understanding Results

Таблица показывает:
The table shows:

- **Карта / Card**: Название гадальной карты
- **Набор / Set**: Количество карт в наборе
- **Цена/шт / Price**: Цена одной карты
- **Всего / Total**: Стоимость полного набора
- **Награда / Reward**: Предмет, который можно получить
- **Цена награды / Reward Price**: Цена предмета-награды
- **Прибыль / Profit**: Чистая прибыль (цена награды - стоимость набора)
- **ROI**: Рентабельность инвестиций в процентах

## Советы / Tips

1. **Актуальная лига**: Всегда используйте название текущей лиги для лучших результатов
2. **Ликвидность**: Учитывайте, что не все предметы легко продать
3. **Комиссии**: Помните про комиссии торговой площадки
4. **Обновление данных**: API poe.ninja обновляется периодически, запускайте анализ регулярно
5. **Фильтры**: Используйте --min-profit и --min-roi чтобы отфильтровать невыгодные варианты

## Troubleshooting

### ModuleNotFoundError
Если видите ошибку про отсутствующие модули - установите зависимости:
```bash
pip install -r requirements.txt
```

### Нет результатов / No results
- Проверьте правильность названия лиги
- Попробуйте уменьшить --min-profit и --min-roi
- Убедитесь что есть подключение к интернету

### API errors
- poe.ninja может быть временно недоступен
- Попробуйте повторить запрос через некоторое время
