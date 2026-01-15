#!/usr/bin/env python3
"""
Generate a random Max Payne quote from quotes.json
This script can be used to create the random-quote.json file for the API
"""

import json
import random
from pathlib import Path
from datetime import datetime, timezone

def get_random_quote():
    """Get a random quote from quotes.json"""
    quotes_file = Path(__file__).parent / 'quotes.json'
    
    with open(quotes_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'quotes' not in data or not data['quotes']:
        raise ValueError("No quotes found in quotes.json")
    
    return random.choice(data['quotes'])

def save_random_quote():
    """Save a random quote to api/random-quote.json"""
    quote = get_random_quote()
    
    # Add updated_on timestamp
    quote['updated_on'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    
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
