# Dynamic League Detection / Динамическое определение лиг

## Описание / Description

**RU:** Программа автоматически определяет доступные лиги из poe.ninja API при запуске веб-интерфейса.

**EN:** The program automatically detects available leagues from poe.ninja API when launching the web interface.

## Как это работает / How it works

### Автоматическая загрузка / Automatic loading
При открытии веб-интерфейса программа:
1. Подключается к poe.ninja API
2. Проверяет список возможных лиг (Standard, Settlers, Hardcore и т.д.)
3. Определяет какие лиги активны
4. Заполняет выпадающий список доступными лигами

When opening the web interface, the program:
1. Connects to poe.ninja API
2. Checks list of possible leagues (Standard, Settlers, Hardcore, etc.)
3. Determines which leagues are active
4. Populates the dropdown with available leagues

### Кеширование / Caching
- Список лиг кешируется на **1 час**
- Это уменьшает нагрузку на poe.ninja API
- Кеш автоматически обновляется по истечении времени

League list is cached for **1 hour**:
- This reduces load on poe.ninja API
- Cache automatically refreshes after expiration

### Ручное обновление / Manual refresh
Нажмите кнопку **🔄** рядом с "League / Лига" чтобы:
- Принудительно обновить список лиг
- Получить свежие данные с poe.ninja
- Обойти кеш

Click the **🔄** button next to "League / Лига" to:
- Force refresh the league list
- Get fresh data from poe.ninja
- Bypass cache

### Резервный список / Fallback
Если API недоступен, используются лиги по умолчанию:
- Standard
- Hardcore
- Settlers
- Hardcore Settlers
- SSF Standard
- SSF Hardcore

If API is unavailable, default leagues are used:
- Standard
- Hardcore
- Settlers
- Hardcore Settlers
- SSF Standard
- SSF Hardcore

## Технические детали / Technical details

### API Endpoint
```
GET /api/leagues
```

Возвращает / Returns:
```json
{
  "success": true,
  "leagues": [
    "Standard",
    "Hardcore",
    "Settlers",
    "Hardcore Settlers",
    ...
  ]
}
```

### Python функция / Python function
```python
from tarot_analyzer import PoeNinjaAPI

# Получить список актуальных лиг
leagues = PoeNinjaAPI.get_active_leagues()
print(leagues)
```

### Обнаружение лиг / League detection
Программа проверяет следующие лиги:
- Standard
- Hardcore
- Settlers
- Hardcore Settlers
- Affliction
- Hardcore Affliction
- Necropolis
- Hardcore Necropolis
- SSF Standard
- SSF Hardcore
- SSF Settlers
- SSF Hardcore Settlers

И автоматически добавляет те, которые активны в poe.ninja.

The program checks the following leagues and automatically adds active ones from poe.ninja.

## Преимущества / Benefits

✅ Всегда актуальный список лиг
✅ Автоматическое обновление при новых лигах
✅ Кеширование для производительности
✅ Ручное обновление при необходимости
✅ Резервный вариант при недоступности API

✅ Always up-to-date league list
✅ Automatic updates for new leagues
✅ Caching for performance
✅ Manual refresh when needed
✅ Fallback when API unavailable
