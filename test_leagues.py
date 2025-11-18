#!/usr/bin/env python3
"""
Тест для определения правильных названий лиг на poe.ninja
Test script to find correct league names on poe.ninja
"""

import requests
import time

def test_league(league_name):
    """Test if a league exists on poe.ninja"""
    try:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        url = "https://poe.ninja/api/data/currencyoverview"
        params = {"league": league_name, "type": "Currency"}

        response = session.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            lines = data.get("lines", [])
            return True, len(lines)
        else:
            return False, response.status_code
    except Exception as e:
        return False, str(e)

# Список возможных названий лиг для тестирования
possible_leagues = [
    # Вариации Keepers of the Flame
    "Keepers of the Flame",
    "Keepers",
    "Keeper of the Flame",
    "The Keepers of the Flame",

    # Settlers (старая лига)
    "Settlers of Kalguur",
    "Settlers",

    # Другие недавние лиги
    "Necropolis",
    "Affliction",
    "Ancestor",
    "Crucible",
    "Sanctum",

    # Permanent лиги
    "Standard",
    "Hardcore",
    "SSF Standard",
    "SSF Hardcore",
]

print("="*80)
print("Проверка лиг на poe.ninja / Testing leagues on poe.ninja")
print("="*80)
print()

found_leagues = []

for league in possible_leagues:
    print(f"Тестирую / Testing: {league:35s} ... ", end="", flush=True)

    success, result = test_league(league)

    if success:
        print(f"✓ НАЙДЕНА / FOUND ({result} currencies)")
        found_leagues.append(league)
    else:
        print(f"✗ Не найдена / Not found ({result})")

    # Небольшая задержка между запросами
    time.sleep(0.5)

print()
print("="*80)
print(f"Найдено активных лиг / Found active leagues: {len(found_leagues)}")
print("="*80)
print()

if found_leagues:
    print("Список активных лиг / Active leagues list:")
    for league in found_leagues:
        print(f"  - {league}")
else:
    print("Ни одной лиги не найдено! / No leagues found!")
    print("Возможные причины / Possible reasons:")
    print("  - poe.ninja временно недоступен / poe.ninja is temporarily down")
    print("  - Проблемы с интернетом / Internet connection issues")
    print("  - API изменился / API has changed")

print()
print("="*80)
