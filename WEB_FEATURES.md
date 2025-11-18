# Web Interface Features / Функции веб-интерфейса

## 📋 Содержание / Table of Contents

1. [Сортировка таблицы / Table Sorting](#table-sorting)
2. [Копирование в буфер / Copy to Clipboard](#copy-to-clipboard)
3. [Ссылки на Trade / Trade Links](#trade-links)
4. [Автоопределение лиг / Auto League Detection](#auto-league-detection)

---

## 📊 Сортировка таблицы / Table Sorting {#table-sorting}

### Как использовать / How to use
**Кликните** на любой заголовок колонки для сортировки.

Click on any column header to sort.

### Функционал / Features
- ⬆️ **Первый клик** - сортировка по возрастанию (A→Z, 0→9)
- ⬇️ **Второй клик** - сортировка по убыванию (Z→A, 9→0)
- 🔄 **Третий клик** - возврат к исходному порядку (по прибыли)

- ⬆️ **First click** - sort ascending (A→Z, 0→9)
- ⬇️ **Second click** - sort descending (Z→A, 9→0)
- 🔄 **Third click** - return to original order (by profit)

### Индикаторы / Indicators
- **⇅** - Колонка может быть отсортирована / Column can be sorted
- **▲** - Сортировка по возрастанию / Sorted ascending
- **▼** - Сортировка по убыванию / Sorted descending

### Сортируемые колонки / Sortable columns
| Колонка / Column | Тип / Type | Описание / Description |
|------------------|------------|------------------------|
| Card / Карта | Текст / String | Название карты / Card name |
| Set / Набор | Число / Number | Размер набора / Set size |
| Price / Цена | Число / Number | Цена за карту / Price per card |
| Total / Всего | Число / Number | Стоимость набора / Set cost |
| Reward / Награда | Текст / String | Название предмета / Item name |
| Reward Price / Цена награды | Число / Number | Цена предмета / Item price |
| Profit / Прибыль | Число / Number | Прибыль / Profit |
| ROI | Число / Number | ROI в % / ROI in % |

### Примеры использования / Use cases
- 🎯 Сортировка по **Profit** чтобы найти самые выгодные карты
- 📈 Сортировка по **ROI** для лучшей рентабельности
- 💰 Сортировка по **Total** для поиска дешевых наборов
- 🔤 Сортировка по **Card** для алфавитного поиска

---

## 📋 Копирование в буфер / Copy to Clipboard {#copy-to-clipboard}

### Как использовать / How to use
**Кликните** на название карты или предмета для копирования в буфер обмена.

Click on card name or item name to copy to clipboard.

### Где кликать / Where to click
- 🎴 **Колонка "Card / Карта"** - копирует название карты
- 🎁 **Колонка "Reward / Награда"** - копирует название предмета

- 🎴 **"Card / Карта" column** - copies card name
- 🎁 **"Reward / Награда" column** - copies item name

### Визуальные эффекты / Visual effects
- ✨ При наведении - золотое свечение
- ✅ При клике - появляется уведомление "Copied! / Скопировано!"
- 🎯 Курсор меняется на "pointer" (рука)

- ✨ On hover - golden glow effect
- ✅ On click - "Copied!" notification appears
- 🎯 Cursor changes to pointer (hand)

### Применение / Use cases
Скопируйте название и вставьте в:
- 🔍 Поиск в игре (Ctrl+F в хранилище)
- 💬 Чат для покупки/продажи
- 📝 Заметки или списки покупок
- 🌐 Поиск в браузере

Copy and paste into:
- 🔍 In-game search (Ctrl+F in stash)
- 💬 Chat for trading
- 📝 Notes or shopping lists
- 🌐 Browser search

---

## 🔍 Ссылки на Trade / Trade Links {#trade-links}

### Где найти / Where to find
Иконка **🔍** рядом с каждым предметом в колонке "Reward / Награда".

**🔍** icon next to each item in "Reward / Награда" column.

### Что делает / What it does
- Открывает официальный trade сайт PoE в новой вкладке
- Автоматически заполняет название предмета
- Автоматически выбирает нужную лигу
- Готовый поиск - просто проверьте результаты!

Opens official PoE trade site in new tab:
- Auto-fills item name
- Auto-selects correct league
- Ready-to-use search - just check results!

### Формат ссылки / Link format
```
https://www.pathofexile.com/trade/search/{league}?q={"query":{"name":"{item_name}","type":""}}
```

### Примеры / Examples

**Карта:** "The Doctor" (8 cards) → **Награда:** "Headhunter"
Клик на 🔍 откроет поиск Headhunter в текущей лиге.

**Card:** "The Doctor" (8 cards) → **Reward:** "Headhunter"
Clicking 🔍 opens Headhunter search in current league.

### Советы / Tips
- 💡 Проверяйте актуальные цены перед покупкой карт
- 📊 Сравнивайте цены в poe.ninja и на trade сайте
- ⏰ Учитывайте, что цены меняются в течение дня
- 🔄 Обновляйте поиск если не нашли результатов

- 💡 Check current prices before buying cards
- 📊 Compare poe.ninja prices with trade site
- ⏰ Remember prices fluctuate during the day
- 🔄 Refresh search if no results found

---

## ⚡ Автоопределение лиг / Auto League Detection {#auto-league-detection}

См. подробную документацию в **[LEAGUES.md](LEAGUES.md)**

See detailed documentation in **[LEAGUES.md](LEAGUES.md)**

### Краткое описание / Quick overview
- 🔄 Автоматическая загрузка списка лиг при запуске
- 💾 Кеширование на 1 час
- 🔄 Кнопка ручного обновления
- 🛡️ Резервный список при ошибках

- 🔄 Automatic league list loading on startup
- 💾 1-hour caching
- 🔄 Manual refresh button
- 🛡️ Fallback list on errors

---

## 🎨 Дизайн и UX / Design & UX

### Цветовая схема / Color scheme
- 🟡 **Золотой (#FFD700)** - акцент, цена в chaos, ссылки
- 🟢 **Зеленый (#4CAF50)** - положительная прибыль, уведомления
- 🔴 **Красный (#F44336)** - отрицательная прибыль, ошибки
- ⚪ **Белый/Серый** - текст, фон таблицы

### Анимации / Animations
- ⚡ Плавные переходы (0.2-0.3s)
- ✨ Эффекты свечения при наведении
- 📈 Масштабирование при клике
- 🌊 Появление/исчезновение уведомлений

### Адаптивность / Responsiveness
- 📱 Мобильная версия (< 768px)
- 💻 Планшеты и десктопы
- 🖥️ Широкие экраны (> 1400px)

---

## ⌨️ Горячие клавиши / Keyboard shortcuts

В будущих версиях планируется:
Planned for future versions:

- `Enter` - запустить анализ / run analysis
- `Ctrl+C` - копировать выделенную строку / copy selected row
- `↑/↓` - навигация по таблице / navigate table
- `Space` - открыть trade ссылку / open trade link

---

## 🐛 Устранение неполадок / Troubleshooting

### Не работает копирование / Copy not working
- Проверьте разрешения браузера для буфера обмена
- Используйте HTTPS или localhost
- Обновите браузер до последней версии

- Check browser clipboard permissions
- Use HTTPS or localhost
- Update browser to latest version

### Сортировка не работает / Sorting not working
- Обновите страницу (F5)
- Очистите кеш браузера
- Проверьте JavaScript в консоли (F12)

- Refresh page (F5)
- Clear browser cache
- Check JavaScript console (F12)

### Trade ссылки не открываются / Trade links don't open
- Проверьте блокировщик всплывающих окон
- Убедитесь что pathofexile.com доступен
- Проверьте правильность названия лиги

- Check popup blocker
- Ensure pathofexile.com is accessible
- Verify league name is correct

---

## 📚 Дополнительные ресурсы / Additional resources

- 📖 [README.md](README.md) - Основная документация / Main documentation
- 🪟 [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) - Установка на Windows / Windows installation
- 🔄 [UPDATE.md](UPDATE.md) - Команды обновления / Update commands
- ⚡ [QUICKSTART.md](QUICKSTART.md) - Быстрый старт / Quick start
- 🌐 [LEAGUES.md](LEAGUES.md) - Автоопределение лиг / Auto league detection
