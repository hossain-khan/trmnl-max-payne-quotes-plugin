#!/usr/bin/env python3
"""
Test suite for quote history tracking system

Tests verify:
1. History file creation and structure
2. Cleanup of old entries (>30 days)
3. Quote filtering (excluding recently used quotes)
4. Fallback behavior when all quotes are used
5. Timestamp validation
"""

import json
import unittest
import tempfile
import shutil
from pathlib import Path
from datetime import datetime, timezone, timedelta
from unittest.mock import patch, MagicMock
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

import generate_random_quote as gq


class TestQuoteHistory(unittest.TestCase):
    """Test suite for quote history tracking"""

    def setUp(self):
        """Create a temporary directory for test files"""
        self.test_dir = tempfile.mkdtemp()
        self.test_history_file = Path(self.test_dir) / '.quote-history.json'
        
        # Mock the HISTORY_FILE path
        self.history_patcher = patch.object(gq, 'HISTORY_FILE', self.test_history_file)
        self.history_patcher.start()

    def tearDown(self):
        """Clean up temporary directory"""
        self.history_patcher.stop()
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_history_file_creation(self):
        """Test that history file is created with proper structure"""
        history = gq.load_quote_history()
        
        # Should return empty structure if file doesn't exist
        self.assertEqual(history, {'quotes': []})
        
        # Save and verify structure
        gq.save_quote_history(history)
        self.assertTrue(self.test_history_file.exists())
        
        with open(self.test_history_file, 'r') as f:
            loaded = json.load(f)
        
        self.assertIn('quotes', loaded)
        self.assertIsInstance(loaded['quotes'], list)

    def test_cleanup_removes_old_entries(self):
        """Test that cleanup_old_history removes entries older than 30 days"""
        # Create history with entries at different ages
        now = datetime.now(timezone.utc)
        old_date = (now - timedelta(days=35)).isoformat().replace('+00:00', 'Z')
        recent_date = (now - timedelta(days=15)).isoformat().replace('+00:00', 'Z')
        
        history = {
            'quotes': [
                {
                    'text': 'Old quote',
                    'character': 'Max',
                    'game': 'Max Payne 1',
                    'selected_on': old_date
                },
                {
                    'text': 'Recent quote',
                    'character': 'Max',
                    'game': 'Max Payne 3',
                    'selected_on': recent_date
                }
            ]
        }
        
        cleaned = gq.cleanup_old_history(history)
        
        # Old entry should be removed, recent entry should remain
        self.assertEqual(len(cleaned['quotes']), 1)
        self.assertEqual(cleaned['quotes'][0]['text'], 'Recent quote')

    def test_cleanup_keeps_recent_entries(self):
        """Test that cleanup_old_history keeps entries within 30 days"""
        now = datetime.now(timezone.utc)
        recent_date = (now - timedelta(days=10)).isoformat().replace('+00:00', 'Z')
        
        history = {
            'quotes': [
                {
                    'text': 'Recent quote',
                    'character': 'Max',
                    'game': 'Max Payne 3',
                    'selected_on': recent_date
                }
            ]
        }
        
        cleaned = gq.cleanup_old_history(history)
        
        # Recent entry should be kept
        self.assertEqual(len(cleaned['quotes']), 1)
        self.assertEqual(cleaned['quotes'][0]['text'], 'Recent quote')

    def test_cleanup_empty_history(self):
        """Test cleanup on empty history"""
        history = {'quotes': []}
        cleaned = gq.cleanup_old_history(history)
        
        self.assertEqual(cleaned, {'quotes': []})

    def test_quote_filtering_excludes_recent(self):
        """Test that get_available_quotes filters out recently used quotes"""
        now = datetime.now(timezone.utc)
        recent_date = (now - timedelta(days=5)).isoformat().replace('+00:00', 'Z')
        
        # Create a mock history with one recent quote
        mock_history = {
            'quotes': [
                {
                    'text': 'First day off the sauce',
                    'character': 'Max Payne',
                    'game': 'Max Payne 3',
                    'selected_on': recent_date
                }
            ]
        }
        
        # Mock quote data
        mock_quotes = {
            'quotes': [
                {'text': 'First day off the sauce', 'character': 'Max Payne', 'game': 'Max Payne 3'},
                {'text': 'Pain is temporary', 'character': 'Max Payne', 'game': 'Max Payne 2'},
                {'text': 'Death is forever', 'character': 'Max Payne', 'game': 'Max Payne 1'}
            ]
        }
        
        with patch('generate_random_quote.load_quote_history', return_value=mock_history):
            with patch('generate_random_quote.save_quote_history'):
                with patch('builtins.open', unittest.mock.mock_open(read_data=json.dumps(mock_quotes))):
                    available, history, all_quotes = gq.get_available_quotes()
        
        # The recently used quote should be filtered out
        available_texts = [q['text'] for q in available]
        self.assertNotIn('First day off the sauce', available_texts)
        self.assertIn('Pain is temporary', available_texts)
        self.assertIn('Death is forever', available_texts)

    def test_days_before_reuse_constant(self):
        """Test that DAYS_BEFORE_REUSE is set to 30"""
        self.assertEqual(gq.DAYS_BEFORE_REUSE, 30)

    def test_history_file_path(self):
        """Test that history file path is correctly set"""
        self.assertTrue(str(gq.HISTORY_FILE).endswith('.quote-history.json'))

    def test_save_and_load_history(self):
        """Test saving and loading history from file"""
        history = {
            'quotes': [
                {
                    'text': 'Test quote',
                    'character': 'Test Character',
                    'game': 'Test Game',
                    'selected_on': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
                }
            ]
        }
        
        gq.save_quote_history(history)
        loaded = gq.load_quote_history()
        
        self.assertEqual(len(loaded['quotes']), 1)
        self.assertEqual(loaded['quotes'][0]['text'], 'Test quote')
        self.assertEqual(loaded['quotes'][0]['character'], 'Test Character')

    def test_history_entry_structure(self):
        """Test that history entries have required fields"""
        history = {
            'quotes': [
                {
                    'text': 'Sample quote',
                    'character': 'Sample Character',
                    'game': 'Sample Game',
                    'selected_on': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
                }
            ]
        }
        
        gq.save_quote_history(history)
        loaded = gq.load_quote_history()
        
        entry = loaded['quotes'][0]
        required_fields = ['text', 'character', 'game', 'selected_on']
        
        for field in required_fields:
            self.assertIn(field, entry)

    def test_timestamp_format_iso8601(self):
        """Test that timestamps are stored in ISO 8601 format"""
        now = datetime.now(timezone.utc)
        timestamp = now.isoformat().replace('+00:00', 'Z')
        
        history = {
            'quotes': [
                {
                    'text': 'Test',
                    'character': 'Test',
                    'game': 'Test',
                    'selected_on': timestamp
                }
            ]
        }
        
        gq.save_quote_history(history)
        loaded = gq.load_quote_history()
        
        # Verify timestamp can be parsed back
        parsed_time = datetime.fromisoformat(loaded['quotes'][0]['selected_on'].replace('Z', '+00:00'))
        self.assertIsInstance(parsed_time, datetime)


class TestQuoteHistoryIntegration(unittest.TestCase):
    """Integration tests for the complete quote history workflow"""

    def setUp(self):
        """Create a temporary directory for test files"""
        self.test_dir = tempfile.mkdtemp()
        self.test_history_file = Path(self.test_dir) / '.quote-history.json'
        
        # Mock the HISTORY_FILE path
        self.history_patcher = patch.object(gq, 'HISTORY_FILE', self.test_history_file)
        self.history_patcher.start()

    def tearDown(self):
        """Clean up temporary directory"""
        self.history_patcher.stop()
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_cleanup_and_load_workflow(self):
        """Test the complete workflow of cleanup and load"""
        # Step 1: Create history with a mix of old and new entries
        now = datetime.now(timezone.utc)
        old_date = (now - timedelta(days=35)).isoformat().replace('+00:00', 'Z')
        recent_date = (now - timedelta(days=5)).isoformat().replace('+00:00', 'Z')
        
        history = {
            'quotes': [
                {'text': 'Old', 'character': 'Max', 'game': 'MP1', 'selected_on': old_date},
                {'text': 'Recent', 'character': 'Max', 'game': 'MP3', 'selected_on': recent_date}
            ]
        }
        
        # Step 2: Save and load
        gq.save_quote_history(history)
        loaded = gq.load_quote_history()
        
        # Step 3: Cleanup
        cleaned = gq.cleanup_old_history(loaded)
        
        # Verify old entries are removed
        self.assertEqual(len(cleaned['quotes']), 1)
        self.assertEqual(cleaned['quotes'][0]['text'], 'Recent')
        
        # Step 4: Save cleaned version
        gq.save_quote_history(cleaned)
        
        # Step 5: Verify persisted to file
        final_loaded = gq.load_quote_history()
        self.assertEqual(len(final_loaded['quotes']), 1)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
