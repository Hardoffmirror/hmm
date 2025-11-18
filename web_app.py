#!/usr/bin/env python3
"""
PoE Divination Card Price Analyzer - Web Interface
Веб-интерфейс анализатора цен гадальных карт
"""

from flask import Flask, render_template, request, jsonify
import sys
from tarot_analyzer import DivinationCardAnalyzer, PoeNinjaAPI
import traceback

app = Flask(__name__)

# Default settings
DEFAULT_LEAGUE = "Standard"
DEFAULT_MIN_PROFIT = 0
DEFAULT_MIN_ROI = 0
DEFAULT_LIMIT = 50


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def analyze():
    """API endpoint for analysis"""
    try:
        data = request.json
        league = data.get('league', DEFAULT_LEAGUE)
        min_profit = float(data.get('min_profit', DEFAULT_MIN_PROFIT))
        min_roi = float(data.get('min_roi', DEFAULT_MIN_ROI))
        limit = int(data.get('limit', DEFAULT_LIMIT))

        # Create analyzer and run analysis
        analyzer = DivinationCardAnalyzer(league=league)
        opportunities = analyzer.analyze(min_profit=min_profit, min_roi=min_roi)

        # Format results
        results = []
        for card, reward_item, profit, roi in opportunities[:limit]:
            results.append({
                'card_name': card.name,
                'stack_size': card.stack_size,
                'card_price': round(card.chaos_value, 2),
                'total_cost': round(card.total_cost, 2),
                'reward_name': reward_item.name,
                'reward_price': round(reward_item.chaos_value, 2),
                'profit': round(profit, 2),
                'roi': round(roi, 1)
            })

        # Calculate statistics
        total_profit = sum(opp[2] for opp in opportunities[:limit])
        avg_roi = sum(opp[3] for opp in opportunities[:limit]) / len(opportunities[:limit]) if opportunities[:limit] else 0

        return jsonify({
            'success': True,
            'results': results,
            'stats': {
                'total_opportunities': len(opportunities),
                'shown': len(results),
                'total_profit': round(total_profit, 2),
                'avg_roi': round(avg_roi, 1)
            }
        })

    except Exception as e:
        print(f"Error in analyze: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/leagues', methods=['GET'])
def get_leagues():
    """Get list of available leagues from poe.ninja"""
    try:
        leagues = PoeNinjaAPI.get_active_leagues()
        return jsonify({
            'success': True,
            'leagues': leagues
        })
    except Exception as e:
        print(f"Error fetching leagues: {e}")
        # Return default leagues on error
        default_leagues = [
            "Standard",
            "Hardcore",
            "Settlers of Kalguur",
            "Hardcore Settlers of Kalguur",
            "SSF Standard",
            "SSF Hardcore"
        ]
        return jsonify({
            'success': True,
            'leagues': default_leagues
        })


@app.route('/api/divine_rate', methods=['GET'])
def get_divine_rate():
    """Get Divine Orb to Chaos Orb exchange rate"""
    try:
        league = request.args.get('league', DEFAULT_LEAGUE)

        api = PoeNinjaAPI(league)
        currency_data = api.fetch_currency_prices()

        divine_rate = 1.0
        for item in currency_data:
            if item.get('currencyTypeName') == 'Divine Orb':
                divine_rate = item.get('chaosEquivalent', 1.0)
                break

        return jsonify({
            'success': True,
            'divine_to_chaos': round(divine_rate, 2),
            'league': league
        })

    except Exception as e:
        print(f"Error fetching divine rate: {e}")
        return jsonify({
            'success': False,
            'error': str(e),
            'divine_to_chaos': 1.0
        })


if __name__ == '__main__':
    import webbrowser
    import threading

    port = 5000
    url = f'http://127.0.0.1:{port}'

    # Open browser after a short delay
    def open_browser():
        import time
        time.sleep(1.5)
        print(f"\n{'='*60}")
        print(f"Opening browser at {url}")
        print(f"Открываю браузер на {url}")
        print(f"{'='*60}\n")
        webbrowser.open(url)

    threading.Thread(target=open_browser, daemon=True).start()

    print(f"\n{'='*60}")
    print(f"PoE Divination Card Analyzer - Web Interface")
    print(f"Анализатор цен гадальных карт - Веб-интерфейс")
    print(f"{'='*60}")
    print(f"\nStarting server on {url}")
    print(f"Сервер запущен на {url}")
    print(f"\nPress Ctrl+C to stop / Нажмите Ctrl+C для остановки\n")

    app.run(debug=False, host='127.0.0.1', port=port)
