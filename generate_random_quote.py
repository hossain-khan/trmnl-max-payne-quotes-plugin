#!/usr/bin/env python3
"""
Generate a random Max Payne quote from quotes.json
This script can be used to create the random-quote.json file for the API

Quote History Tracking:
- Maintains a history of recently selected quotes in .quote-history.json
- Prevents the same quote from appearing again within 30 days (1 month) (configurable)
- Automatically cleans up old entries to keep the history file small
"""

import json
import random
from pathlib import Path
from datetime import datetime, timezone, timedelta

HISTORY_FILE = Path(__file__).parent / '.quote-history.json'
DAYS_BEFORE_REUSE = 30  # Don't show the same quote within this many days (1 month)

def load_quote_history():
    """Load the quote selection history"""
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'quotes': []}

def save_quote_history(history):
    """Save the quote selection history"""
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def cleanup_old_history(history):
    """Remove entries older than DAYS_BEFORE_REUSE days"""
    cutoff_date = (datetime.now(timezone.utc) - timedelta(days=DAYS_BEFORE_REUSE)).isoformat().replace('+00:00', 'Z')
    history['quotes'] = [entry for entry in history['quotes'] if entry['selected_on'] > cutoff_date]
    return history

def get_available_quotes():
    """Get quotes that haven't been selected in the last DAYS_BEFORE_REUSE days"""
    quotes_file = Path(__file__).parent / 'quotes.json'
    
    with open(quotes_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'quotes' not in data or not data['quotes']:
        raise ValueError("No quotes found in quotes.json")
    
    # Load and cleanup history
    history = load_quote_history()
    history = cleanup_old_history(history)
    save_quote_history(history)
    
    # Get recently selected quote texts
    recent_quote_texts = set(entry['text'] for entry in history['quotes'])
    
    # Filter out recently selected quotes
    available = [q for q in data['quotes'] if q['text'] not in recent_quote_texts]
    
    # If all quotes have been recently used, clear history and use all quotes
    if not available:
        print("⚠️  All quotes have been recently used, clearing history...")
        history['quotes'] = []
        save_quote_history(history)
        available = data['quotes']
    
    return available, history, data['quotes']

def get_random_quote():
    """Get a random quote from available quotes (not recently shown)"""
    available, history, _ = get_available_quotes()
    return random.choice(available), history

def save_random_quote():
    """Save a random quote to api/random-quote.json and track it in history"""
    quote, history = get_random_quote()
    
    # Add updated_on timestamp
    quote['updated_on'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    
    # Add this quote to history
    history['quotes'].append({
        'text': quote['text'],
        'character': quote['character'],
        'game': quote['game'],
        'selected_on': quote['updated_on']
    })
    
    # Keep only recent entries (cleanup)
    history = cleanup_old_history(history)
    save_quote_history(history)
    
    # Create api directory if it doesn't exist
    api_dir = Path(__file__).parent / 'api'
    api_dir.mkdir(exist_ok=True)
    
    # Save the random quote
    output_file = api_dir / 'random-quote.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(quote, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Random quote saved to {output_file}")
    print(f"\n📜 Quote: \"{quote['text'][:80]}...\"")
    print(f"🎮 Game: {quote['game']}")
    print(f"👤 Character: {quote['character']}")
    print(f"🕒 Updated: {quote['updated_on']}")
    print(f"📊 Quote history: {len(history['quotes'])} recent quotes tracked")

def display_all_quotes():
    """Display all quotes from quotes.json"""
    quotes_file = Path(__file__).parent / 'quotes.json'
    
    with open(quotes_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"\n🎮 Max Payne Quotes Database")
    print(f"{'='*60}\n")
    
    for i, quote in enumerate(data['quotes'], 1):
        print(f"Quote #{i}")
        print(f"Text: {quote['text']}")
        print(f"Character: {quote['character']}")
        print(f"Game: {quote['game']}")
        print(f"{'-'*60}\n")
    
    print(f"Total quotes: {len(data['quotes'])}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--list':
        display_all_quotes()
    else:
        save_random_quote()
