#!/bin/bash
# Примеры использования / Usage examples

echo "=== PoE Divination Card Analyzer Examples ==="
echo ""

echo "1. Анализ стандартной лиги / Analyze Standard league:"
echo "   python tarot_analyzer.py"
echo ""

echo "2. Анализ текущей лиги (измените на актуальную) / Analyze current league:"
echo "   python tarot_analyzer.py --league 'Settlers'"
echo ""

echo "3. Показать только карты с прибылью > 10 chaos / Show only cards with profit > 10 chaos:"
echo "   python tarot_analyzer.py --min-profit 10"
echo ""

echo "4. Показать только карты с ROI > 50% / Show only cards with ROI > 50%:"
echo "   python tarot_analyzer.py --min-roi 50"
echo ""

echo "5. Показать топ-50 карт / Show top 50 cards:"
echo "   python tarot_analyzer.py --limit 50"
echo ""

echo "6. Комбинация фильтров / Combination of filters:"
echo "   python tarot_analyzer.py --league 'Standard' --min-profit 5 --min-roi 20 --limit 30"
echo ""

echo "Для справки / For help:"
echo "   python tarot_analyzer.py --help"
