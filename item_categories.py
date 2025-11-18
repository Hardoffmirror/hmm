"""
Item categorization system for Path of Exile items
Система категоризации предметов Path of Exile
"""

# Item categories with keywords for detection
ITEM_CATEGORIES = {
    # Currency - Валюта
    'currency_basic': {
        'name': 'Basic Currency / Базовая валюта',
        'keywords': [
            'Orb of Alteration', 'Orb of Alchemy', 'Orb of Chance',
            'Chromatic Orb', 'Jeweller\'s Orb', 'Orb of Fusing',
            'Orb of Scouring', 'Blessed Orb', 'Chaos Orb',
            'Orb of Regret', 'Regal Orb', 'Gemcutter\'s Prism',
            'Cartographer\'s Chisel', 'Glassblower\'s Bauble',
            'Orb of Transmutation', 'Orb of Augmentation',
            'Armourer\'s Scrap', 'Blacksmith\'s Whetstone',
            'Portal Scroll', 'Scroll of Wisdom'
        ]
    },
    'currency_premium': {
        'name': 'Premium Currency / Премиум валюта',
        'keywords': [
            'Divine Orb', 'Exalted Orb', 'Mirror of Kalandra',
            'Orb of Annulment', 'Ancient Orb', 'Harbinger\'s Orb',
            'Orb of Horizons', 'Engineer\'s Orb', 'Infused Engineer\'s Orb',
            'Awakener\'s Orb', 'Crusader\'s Exalted Orb',
            'Redeemer\'s Exalted Orb', 'Hunter\'s Exalted Orb',
            'Warlord\'s Exalted Orb', 'Veiled Chaos Orb',
            'Sacred Orb', 'Exceptional Eldritch Ember',
            'Exceptional Eldritch Ichor'
        ]
    },
    'currency_fragments': {
        'name': 'Fragments & Splinters / Фрагменты и осколки',
        'keywords': [
            'Fragment', 'Splinter', 'Breachstone', 'Blessing',
            'Simulacrum', 'Timeless', 'Crescent', 'Offering',
            'Scarab', 'Invitation', 'Maven\'s Writ'
        ]
    },
    'currency_essence': {
        'name': 'Essences & Fossils / Эссенции и ископаемые',
        'keywords': [
            'Essence', 'Fossil', 'Resonator', 'Deafening', 'Shrieking',
            'Screaming', 'Wailing', 'Weeping', 'Muttering', 'Whispering'
        ]
    },
    'currency_catalyst': {
        'name': 'Catalysts & Oils / Катализаторы и масла',
        'keywords': [
            'Catalyst', 'Oil', 'Anointed', 'Intrinsic', 'Fertile',
            'Prismatic', 'Turbulent', 'Imbued', 'Abrasive', 'Tempering',
            'Tainted', 'Clear Oil', 'Sepia Oil', 'Amber Oil',
            'Verdant Oil', 'Teal Oil', 'Azure Oil', 'Violet Oil',
            'Crimson Oil', 'Black Oil', 'Opalescent Oil', 'Silver Oil',
            'Golden Oil'
        ]
    },
    'currency_vial': {
        'name': 'Vials & Embers / Пузырьки и угли',
        'keywords': [
            'Vial', 'Ember', 'Ichor', 'Eldritch', 'Blood-filled',
            'Tainted', 'Lesser Eldritch', 'Greater Eldritch',
            'Grand Eldritch', 'Exceptional Eldritch', 'Orb of Conflict'
        ]
    },

    # Equipment - Снаряжение
    'ring': {
        'name': 'Rings / Кольца',
        'keywords': ['Ring', 'Two-Stone Ring', 'Prismatic Ring', 'Unset Ring']
    },
    'amulet': {
        'name': 'Amulets / Амулеты',
        'keywords': ['Amulet', 'Talisman']
    },
    'belt': {
        'name': 'Belts / Пояса',
        'keywords': ['Belt', 'Rustic Sash', 'Stygian Vise', 'Heavy Belt',
                     'Leather Belt', 'Cloth Belt', 'Studded Belt']
    },

    # Weapons - Оружие
    'weapon_sword': {
        'name': 'Swords / Мечи',
        'keywords': ['Sword', 'Rapier', 'Foil', 'Sabre', 'Gladius',
                     'Corsair Sword', 'Cutlass', 'Elegant Sword']
    },
    'weapon_axe': {
        'name': 'Axes / Топоры',
        'keywords': ['Axe', 'Hatchet', 'Cleaver', 'Labrys', 'Tomahawk']
    },
    'weapon_mace': {
        'name': 'Maces & Sceptres / Булавы и скипетры',
        'keywords': ['Mace', 'Sceptre', 'Club', 'Gavel', 'Tenderizer']
    },
    'weapon_bow': {
        'name': 'Bows / Луки',
        'keywords': ['Bow', 'Longbow', 'Shortbow', 'Grove Bow', 'Thicket Bow']
    },
    'weapon_staff': {
        'name': 'Staves / Посохи',
        'keywords': ['Staff', 'Quarterstaff', 'Lathi', 'Imperial Staff']
    },
    'weapon_wand': {
        'name': 'Wands / Жезлы',
        'keywords': ['Wand', 'Imbued Wand', 'Opal Wand', 'Prophecy Wand']
    },
    'weapon_dagger': {
        'name': 'Daggers / Кинжалы',
        'keywords': ['Dagger', 'Stiletto', 'Poignard', 'Skean']
    },
    'weapon_claw': {
        'name': 'Claws / Когти',
        'keywords': ['Claw', 'Awl', 'Tiger\'s Paw', 'Imperial Claw']
    },

    # Armour - Доспехи
    'armour_helmet': {
        'name': 'Helmets / Шлемы',
        'keywords': ['Helmet', 'Cap', 'Crown', 'Burgonet', 'Sallet', 'Circlet']
    },
    'armour_body': {
        'name': 'Body Armour / Нагрудники',
        'keywords': ['Body Armour', 'Plate', 'Vest', 'Tunic', 'Robe',
                     'Armour', 'Regalia', 'Vestment', 'Coat', 'Raiment',
                     'Garb', 'Lamellar', 'Brigandine', 'Doublet']
    },
    'armour_gloves': {
        'name': 'Gloves / Перчатки',
        'keywords': ['Gloves', 'Gauntlets', 'Mitts']
    },
    'armour_boots': {
        'name': 'Boots / Ботинки',
        'keywords': ['Boots', 'Greaves', 'Slippers']
    },
    'armour_shield': {
        'name': 'Shields / Щиты',
        'keywords': ['Shield', 'Buckler', 'Kite Shield', 'Tower Shield']
    },
    'armour_quiver': {
        'name': 'Quivers / Колчаны',
        'keywords': ['Quiver', 'Arrow', 'Spike-Point']
    },

    # Other - Прочее
    'jewel': {
        'name': 'Jewels / Самоцветы',
        'keywords': ['Jewel', 'Cobalt Jewel', 'Viridian Jewel', 'Crimson Jewel',
                     'Prismatic Jewel', 'Timeless Jewel', 'Abyss Jewel']
    },
    'map': {
        'name': 'Maps / Карты',
        'keywords': ['Map', 'Synthesised Map', 'Blighted Map', 'Delirium',
                     'Maven\'s', 'Shaper\'s', 'Elder\'s']
    },
    'gem': {
        'name': 'Gems / Камни умений',
        'keywords': ['Gem', 'Support', 'Skill', 'Awakened']
    },
    'flask': {
        'name': 'Flasks / Фласки',
        'keywords': ['Flask', 'Life Flask', 'Mana Flask', 'Hybrid Flask']
    },
    'divination_card': {
        'name': 'Divination Cards / Гадальные карты',
        'keywords': ['Divination Card']
    },
    'unique_accessory': {
        'name': 'Unique Accessories / Уникальные аксессуары',
        'keywords': []  # Will be detected as unique if not in other categories
    },
    'unique_weapon': {
        'name': 'Unique Weapons / Уникальное оружие',
        'keywords': []  # Will be detected as unique if not in other categories
    },
    'unique_armour': {
        'name': 'Unique Armour / Уникальная броня',
        'keywords': []  # Will be detected as unique if not in other categories
    },
    'other': {
        'name': 'Other / Прочее',
        'keywords': []
    }
}


def categorize_item(item_name: str) -> str:
    """
    Categorize an item based on its name
    Определить категорию предмета по названию

    Args:
        item_name: Name of the item

    Returns:
        Category key (e.g., 'currency_basic', 'ring', 'weapon_sword')
    """
    item_lower = item_name.lower()

    # Check each category
    for category_key, category_data in ITEM_CATEGORIES.items():
        keywords = category_data.get('keywords', [])
        for keyword in keywords:
            if keyword.lower() in item_lower:
                return category_key

    # Default category
    return 'other'


def get_category_display_name(category_key: str) -> str:
    """
    Get display name for a category
    Получить отображаемое название категории

    Args:
        category_key: Category key

    Returns:
        Display name
    """
    return ITEM_CATEGORIES.get(category_key, {}).get('name', 'Other / Прочее')


def get_all_categories() -> dict:
    """
    Get all categories with their display names
    Получить все категории с отображаемыми названиями

    Returns:
        Dictionary of category_key: display_name
    """
    return {key: data['name'] for key, data in ITEM_CATEGORIES.items()}


def get_category_groups() -> dict:
    """
    Get categories grouped by type
    Получить категории, сгруппированные по типам

    Returns:
        Dictionary of group_name: [category_keys]
    """
    return {
        'Currency / Валюта': [
            'currency_basic',
            'currency_premium',
            'currency_fragments',
            'currency_essence',
            'currency_catalyst',
            'currency_vial'
        ],
        'Accessories / Аксессуары': [
            'ring',
            'amulet',
            'belt'
        ],
        'Weapons / Оружие': [
            'weapon_sword',
            'weapon_axe',
            'weapon_mace',
            'weapon_bow',
            'weapon_staff',
            'weapon_wand',
            'weapon_dagger',
            'weapon_claw'
        ],
        'Armour / Доспехи': [
            'armour_helmet',
            'armour_body',
            'armour_gloves',
            'armour_boots',
            'armour_shield',
            'armour_quiver'
        ],
        'Other / Прочее': [
            'jewel',
            'map',
            'gem',
            'flask',
            'divination_card',
            'unique_accessory',
            'unique_weapon',
            'unique_armour',
            'other'
        ]
    }
