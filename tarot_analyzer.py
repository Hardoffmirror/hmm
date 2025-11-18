#!/usr/bin/env python3
"""
PoE Divination Card Price Analyzer
Анализатор цен гадальных карт Path of Exile
"""

import argparse
import requests
import sys
from typing import Dict, List, Optional, Tuple
from tabulate import tabulate
from dataclasses import dataclass


@dataclass
class DivinationCard:
    """Divination card data model"""
    name: str
    stack_size: int  # Number of cards needed for a full set
    reward: str  # Item/reward description
    chaos_value: float  # Price per card in chaos orbs
    total_cost: float  # Cost to buy full set

    def __repr__(self):
        return f"{self.name} ({self.stack_size}x) -> {self.reward}"


@dataclass
class ItemPrice:
    """Item price data"""
    name: str
    chaos_value: float
    item_type: str


class PoeNinjaAPI:
    """Client for poe.ninja API"""

    BASE_URL = "https://poe.ninja/api/data"
    LEAGUES_CACHE = None
    LEAGUES_CACHE_TIMESTAMP = 0

    # Item type categories for API
    ITEM_TYPES = [
        "Currency",
        "Fragment",
        "DivinationCard",
        "Artifact",
        "Oil",
        "Incubator",
        "UniqueWeapon",
        "UniqueArmour",
        "UniqueAccessory",
        "UniqueFlask",
        "UniqueJewel",
        "SkillGem",
        "ClusterJewel",
        "Map",
        "BlightedMap",
        "BlightRavagedMap",
        "Invitation",
        "Scarab",
        "BaseType",
        "HelmetEnchant",
        "Memory",
        "Essence",
        "Fossil",
        "Resonator",
        "Beast",
        "Vial",
        "Tattoo",
        "Omen",
        "Coffin",
        "Allflame"
    ]

    def __init__(self, league: str = "Standard"):
        self.league = league
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'PoE-Divination-Card-Analyzer/1.0'
        })

    def fetch_divination_cards(self) -> List[Dict]:
        """Fetch all divination card prices"""
        try:
            url = f"{self.BASE_URL}/itemoverview"
            params = {
                "league": self.league,
                "type": "DivinationCard"
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("lines", [])
        except Exception as e:
            print(f"Error fetching divination cards: {e}")
            return []

    def fetch_item_prices(self, item_type: str) -> List[Dict]:
        """Fetch item prices for a specific type"""
        try:
            url = f"{self.BASE_URL}/itemoverview"
            params = {
                "league": self.league,
                "type": item_type
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("lines", [])
        except Exception as e:
            # Silent fail for item types that don't exist
            return []

    def fetch_currency_prices(self) -> List[Dict]:
        """Fetch currency prices (uses different endpoint)"""
        try:
            url = f"{self.BASE_URL}/currencyoverview"
            params = {
                "league": self.league,
                "type": "Currency"
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("lines", [])
        except Exception as e:
            return []

    def build_item_price_map(self) -> Dict[str, ItemPrice]:
        """Build a comprehensive map of all item prices"""
        price_map = {}

        print("Загрузка цен предметов... / Loading item prices...")

        # Fetch currency first
        currencies = self.fetch_currency_prices()
        for item in currencies:
            name = item.get("currencyTypeName", "")
            chaos_value = item.get("chaosEquivalent", 0)
            if name and chaos_value:
                price_map[name.lower()] = ItemPrice(
                    name=name,
                    chaos_value=chaos_value,
                    item_type="Currency"
                )

        # Fetch all other item types
        for item_type in self.ITEM_TYPES:
            if item_type == "DivinationCard":
                continue

            items = self.fetch_item_prices(item_type)
            for item in items:
                name = item.get("name", "")
                base_type = item.get("baseType", "")
                chaos_value = item.get("chaosValue", 0)

                # Store by name and base type
                if name and chaos_value:
                    price_map[name.lower()] = ItemPrice(
                        name=name,
                        chaos_value=chaos_value,
                        item_type=item_type
                    )
                if base_type and chaos_value and base_type != name:
                    price_map[base_type.lower()] = ItemPrice(
                        name=base_type,
                        chaos_value=chaos_value,
                        item_type=item_type
                    )

        print(f"Загружено цен: {len(price_map)} / Loaded prices: {len(price_map)}")
        return price_map

    @staticmethod
    def get_active_leagues() -> List[str]:
        """
        Fetch list of active leagues from poe.ninja
        Returns a list of league names with caching
        """
        import time

        # Cache for 30 minutes (1800 seconds)
        current_time = time.time()
        cache_duration = 1800

        if (PoeNinjaAPI.LEAGUES_CACHE is not None and
            current_time - PoeNinjaAPI.LEAGUES_CACHE_TIMESTAMP < cache_duration):
            print(f"Using cached leagues: {PoeNinjaAPI.LEAGUES_CACHE}")
            return PoeNinjaAPI.LEAGUES_CACHE

        try:
            session = requests.Session()
            session.headers.update({'User-Agent': 'PoE-Divination-Card-Analyzer/1.0'})

            print("Detecting active leagues from poe.ninja...")
            print("-" * 50)

            # List of known possible leagues (UPDATE THIS when new league starts!)
            # Current as of December 2024
            possible_leagues = [
                # Current challenge league (update these when new league starts!)
                "Settlers of Kalguur",
                "Hardcore Settlers of Kalguur",

                # Permanent leagues
                "Standard",
                "Hardcore",

                # SSF variants
                "SSF Settlers of Kalguur",
                "SSF Hardcore Settlers of Kalguur",
                "SSF Standard",
                "SSF Hardcore",
            ]

            active_leagues = []

            # Test each league by fetching currency data
            for league in possible_leagues:
                try:
                    url = f"{PoeNinjaAPI.BASE_URL}/currencyoverview"
                    params = {"league": league, "type": "Currency"}
                    print(f"Testing: {league}...", end=" ")
                    response = session.get(url, params=params, timeout=5)

                    if response.status_code == 200:
                        data = response.json()
                        lines = data.get("lines", [])
                        # League is active if it has currency data
                        if lines and len(lines) >= 5:
                            active_leagues.append(league)
                            print(f"✓ ACTIVE ({len(lines)} currencies)")
                        else:
                            print(f"✗ No data ({len(lines)} items)")
                    else:
                        print(f"✗ HTTP {response.status_code}")
                except Exception as e:
                    print(f"✗ Error: {e}")
                    continue

            print("-" * 50)
            print(f"Found {len(active_leagues)} active leagues")

            # If no leagues found, return permanent leagues as fallback
            if not active_leagues:
                print("WARNING: No leagues detected! Using fallback list.")
                active_leagues = ["Standard", "Hardcore", "Settlers of Kalguur"]

            # Update cache
            PoeNinjaAPI.LEAGUES_CACHE = active_leagues
            PoeNinjaAPI.LEAGUES_CACHE_TIMESTAMP = current_time

            return active_leagues

        except Exception as e:
            print(f"Error fetching leagues: {e}")
            import traceback
            traceback.print_exc()

            # Return fallback leagues
            return ["Standard", "Hardcore", "Settlers of Kalguur", "SSF Standard"]


class DivinationCardAnalyzer:
    """Analyzer for divination card profitability"""

    def __init__(self, league: str = "Standard"):
        self.api = PoeNinjaAPI(league)
        self.league = league

    def analyze(self, min_profit: float = 0, min_roi: float = 0) -> List[Tuple[DivinationCard, ItemPrice, float, float]]:
        """
        Analyze divination cards for profitability

        Returns list of tuples: (card, reward_item, profit, roi_percent)
        """
        print(f"\nАнализ гадальных карт для лиги: {self.league}")
        print(f"Analyzing divination cards for league: {self.league}\n")

        # Fetch data
        card_data = self.api.fetch_divination_cards()
        if not card_data:
            print("Не удалось загрузить данные карт / Failed to load card data")
            return []

        print(f"Найдено карт: {len(card_data)} / Found cards: {len(card_data)}")

        # Build item price map
        item_prices = self.api.build_item_price_map()

        # Analyze each card
        opportunities = []

        for card_info in card_data:
            card = DivinationCard(
                name=card_info.get("name", ""),
                stack_size=card_info.get("stackSize", 1),
                reward=card_info.get("explicitModifiers", [{}])[0].get("text", "Unknown"),
                chaos_value=card_info.get("chaosValue", 0),
                total_cost=0
            )

            # Calculate total cost for full set
            card.total_cost = card.chaos_value * card.stack_size

            if card.total_cost == 0:
                continue

            # Try to find reward item price
            reward_price = self._find_reward_price(card.reward, item_prices)

            if reward_price and reward_price.chaos_value > 0:
                profit = reward_price.chaos_value - card.total_cost
                roi = (profit / card.total_cost) * 100 if card.total_cost > 0 else 0

                if profit >= min_profit and roi >= min_roi:
                    opportunities.append((card, reward_price, profit, roi))

        # Sort by profit (descending)
        opportunities.sort(key=lambda x: x[2], reverse=True)

        return opportunities

    def _find_reward_price(self, reward_text: str, item_prices: Dict[str, ItemPrice]) -> Optional[ItemPrice]:
        """Try to find item price from reward text"""
        if not reward_text:
            return None

        reward_lower = reward_text.lower()

        # Direct match
        if reward_lower in item_prices:
            return item_prices[reward_lower]

        # Try to extract item name from reward text
        # Common patterns: "X", "X (rarity)", etc.
        for item_name in item_prices:
            if item_name in reward_lower:
                return item_prices[item_name]

        return None


def format_chaos(value: float) -> str:
    """Format chaos value with icon"""
    return f"{value:.2f}c"


def main():
    parser = argparse.ArgumentParser(
        description="PoE Divination Card Price Analyzer / Анализатор цен гадальных карт"
    )
    parser.add_argument(
        "--league", "-l",
        default="Standard",
        help="League name (default: Standard)"
    )
    parser.add_argument(
        "--min-profit", "-p",
        type=float,
        default=0,
        help="Minimum profit in chaos orbs (default: 0)"
    )
    parser.add_argument(
        "--min-roi", "-r",
        type=float,
        default=0,
        help="Minimum ROI percentage (default: 0)"
    )
    parser.add_argument(
        "--limit", "-n",
        type=int,
        default=20,
        help="Number of results to show (default: 20)"
    )

    args = parser.parse_args()

    try:
        analyzer = DivinationCardAnalyzer(league=args.league)
        opportunities = analyzer.analyze(min_profit=args.min_profit, min_roi=args.min_roi)

        if not opportunities:
            print("\nНет выгодных возможностей / No profitable opportunities found")
            return

        # Display results
        print(f"\n{'='*100}")
        print(f"Найдено выгодных возможностей: {len(opportunities)} / Found opportunities: {len(opportunities)}")
        print(f"Показано топ-{min(args.limit, len(opportunities))} / Showing top-{min(args.limit, len(opportunities))}")
        print(f"{'='*100}\n")

        table_data = []
        for card, reward_item, profit, roi in opportunities[:args.limit]:
            table_data.append([
                card.name,
                f"{card.stack_size}x",
                format_chaos(card.chaos_value),
                format_chaos(card.total_cost),
                reward_item.name,
                format_chaos(reward_item.chaos_value),
                format_chaos(profit),
                f"{roi:.1f}%"
            ])

        headers = [
            "Карта / Card",
            "Набор / Set",
            "Цена/шт / Price",
            "Всего / Total",
            "Награда / Reward",
            "Цена награды / Reward Price",
            "Прибыль / Profit",
            "ROI"
        ]

        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        # Summary statistics
        total_profit = sum(opp[2] for opp in opportunities[:args.limit])
        avg_roi = sum(opp[3] for opp in opportunities[:args.limit]) / len(opportunities[:args.limit])

        print(f"\n{'='*100}")
        print(f"Суммарная потенциальная прибыль / Total potential profit: {format_chaos(total_profit)}")
        print(f"Средний ROI / Average ROI: {avg_roi:.1f}%")
        print(f"{'='*100}\n")

    except KeyboardInterrupt:
        print("\n\nПрервано пользователем / Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nОшибка / Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
