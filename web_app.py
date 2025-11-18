#!/usr/bin/env python3
"""
PoE Divination Card Price Analyzer - Web Interface
Веб-интерфейс анализатора цен гадальных карт
"""

from flask import Flask, render_template, request, jsonify
import sys
from tarot_analyzer import DivinationCardAnalyzer, PoeNinjaAPI
import traceback
import json
import os

app = Flask(__name__)

# Default settings
DEFAULT_LEAGUE = "Keepers"
DEFAULT_MIN_PROFIT = 0
DEFAULT_MIN_ROI = 0
DEFAULT_LIMIT = 50

# File for storing custom leagues
CUSTOM_LEAGUES_FILE = "custom_leagues.json"

# File for storing hidden cards
HIDDEN_CARDS_FILE = "hidden_cards.json"


def load_hidden_cards():
    """Load hidden cards from file"""
    if os.path.exists(HIDDEN_CARDS_FILE):
        try:
            with open(HIDDEN_CARDS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('hidden_cards', [])
        except Exception as e:
            print(f"Error loading hidden cards: {e}")
            return []
    return []


def save_hidden_cards(hidden_cards):
    """Save hidden cards to file"""
    try:
        with open(HIDDEN_CARDS_FILE, 'w', encoding='utf-8') as f:
            json.dump({'hidden_cards': hidden_cards}, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving hidden cards: {e}")
        return False


def load_custom_leagues():
    """Load custom leagues from file"""
    if os.path.exists(CUSTOM_LEAGUES_FILE):
        try:
            with open(CUSTOM_LEAGUES_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('leagues', [])
        except Exception as e:
            print(f"Error loading custom leagues: {e}")
            return []
    return []


def save_custom_leagues(leagues):
    """Save custom leagues to file"""
    try:
        with open(CUSTOM_LEAGUES_FILE, 'w', encoding='utf-8') as f:
            json.dump({'leagues': leagues}, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving custom leagues: {e}")
        return False


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

        # Load hidden cards to filter them out
        hidden_cards = load_hidden_cards()

        # Filter out hidden cards
        filtered_opportunities = [
            opp for opp in opportunities
            if opp[0].name not in hidden_cards  # opp[0] is the card object
        ]

        # Format results
        results = []
        for card, reward_item, profit, roi in filtered_opportunities[:limit]:
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
        total_profit = sum(opp[2] for opp in filtered_opportunities[:limit])
        avg_roi = sum(opp[3] for opp in filtered_opportunities[:limit]) / len(filtered_opportunities[:limit]) if filtered_opportunities[:limit] else 0

        return jsonify({
            'success': True,
            'results': results,
            'stats': {
                'total_opportunities': len(filtered_opportunities),
                'shown': len(results),
                'total_profit': round(total_profit, 2),
                'avg_roi': round(avg_roi, 1),
                'hidden_count': len(opportunities) - len(filtered_opportunities)
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
    """Get list of available leagues (standard + custom)"""
    try:
        # Get standard leagues
        standard_leagues = [
            "Standard",
            "Hardcore",
            "SSF Standard",
            "SSF Hardcore"
        ]

        # Load custom leagues
        custom_leagues = load_custom_leagues()

        # Combine: custom first (so they appear at top), then standard
        all_leagues = custom_leagues + standard_leagues

        # Remove duplicates while preserving order
        seen = set()
        unique_leagues = []
        for league in all_leagues:
            if league not in seen:
                seen.add(league)
                unique_leagues.append(league)

        return jsonify({
            'success': True,
            'leagues': unique_leagues
        })
    except Exception as e:
        print(f"Error fetching leagues: {e}")
        traceback.print_exc()
        return jsonify({
            'success': True,
            'leagues': ["Standard", "Hardcore"]
        })


@app.route('/api/custom_leagues', methods=['GET'])
def get_custom_leagues():
    """Get list of custom leagues"""
    try:
        leagues = load_custom_leagues()
        return jsonify({
            'success': True,
            'leagues': leagues
        })
    except Exception as e:
        print(f"Error getting custom leagues: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/custom_leagues/add', methods=['POST'])
def add_custom_league():
    """Add a custom league"""
    try:
        data = request.json
        league_name = data.get('league', '').strip()

        if not league_name:
            return jsonify({
                'success': False,
                'error': 'League name cannot be empty'
            }), 400

        # Load existing leagues
        leagues = load_custom_leagues()

        # Check if already exists
        if league_name in leagues:
            return jsonify({
                'success': False,
                'error': 'League already exists'
            }), 400

        # Add new league
        leagues.append(league_name)

        # Save
        if save_custom_leagues(leagues):
            return jsonify({
                'success': True,
                'message': f'League "{league_name}" added',
                'leagues': leagues
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to save leagues'
            }), 500

    except Exception as e:
        print(f"Error adding custom league: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/custom_leagues/remove', methods=['POST'])
def remove_custom_league():
    """Remove a custom league"""
    try:
        data = request.json
        league_name = data.get('league', '').strip()

        if not league_name:
            return jsonify({
                'success': False,
                'error': 'League name cannot be empty'
            }), 400

        # Load existing leagues
        leagues = load_custom_leagues()

        # Check if exists
        if league_name not in leagues:
            return jsonify({
                'success': False,
                'error': 'League not found'
            }), 404

        # Remove league
        leagues.remove(league_name)

        # Save
        if save_custom_leagues(leagues):
            return jsonify({
                'success': True,
                'message': f'League "{league_name}" removed',
                'leagues': leagues
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to save leagues'
            }), 500

    except Exception as e:
        print(f"Error removing custom league: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/hidden_cards', methods=['GET'])
def get_hidden_cards():
    """Get list of hidden cards"""
    try:
        cards = load_hidden_cards()
        return jsonify({
            'success': True,
            'hidden_cards': cards
        })
    except Exception as e:
        print(f"Error getting hidden cards: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/hidden_cards/add', methods=['POST'])
def add_hidden_card():
    """Add a card to hidden list"""
    try:
        data = request.json
        card_name = data.get('card_name', '').strip()

        if not card_name:
            return jsonify({
                'success': False,
                'error': 'Card name cannot be empty'
            }), 400

        # Load existing hidden cards
        hidden_cards = load_hidden_cards()

        # Check if already exists
        if card_name in hidden_cards:
            return jsonify({
                'success': False,
                'error': 'Card already hidden'
            }), 400

        # Add card
        hidden_cards.append(card_name)

        # Save
        if save_hidden_cards(hidden_cards):
            return jsonify({
                'success': True,
                'message': f'Card "{card_name}" hidden',
                'hidden_cards': hidden_cards
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to save hidden cards'
            }), 500

    except Exception as e:
        print(f"Error adding hidden card: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/hidden_cards/remove', methods=['POST'])
def remove_hidden_card():
    """Remove a card from hidden list"""
    try:
        data = request.json
        card_name = data.get('card_name', '').strip()

        if not card_name:
            return jsonify({
                'success': False,
                'error': 'Card name cannot be empty'
            }), 400

        # Load existing hidden cards
        hidden_cards = load_hidden_cards()

        # Check if exists
        if card_name not in hidden_cards:
            return jsonify({
                'success': False,
                'error': 'Card not found in hidden list'
            }), 404

        # Remove card
        hidden_cards.remove(card_name)

        # Save
        if save_hidden_cards(hidden_cards):
            return jsonify({
                'success': True,
                'message': f'Card "{card_name}" restored',
                'hidden_cards': hidden_cards
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to save hidden cards'
            }), 500

    except Exception as e:
        print(f"Error removing hidden card: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/hidden_cards/clear', methods=['POST'])
def clear_hidden_cards():
    """Clear all hidden cards"""
    try:
        if save_hidden_cards([]):
            return jsonify({
                'success': True,
                'message': 'All hidden cards cleared'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to clear hidden cards'
            }), 500

    except Exception as e:
        print(f"Error clearing hidden cards: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


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
