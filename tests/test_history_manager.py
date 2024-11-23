"""
Unit tests for the HistoryManager class.
"""

import unittest
from src.patterns.history_manager import HistoryManager


class TestHistoryManager(unittest.TestCase):
    """
    Unit tests for the HistoryManager class.
    """

    def test_save_single_history_entry(self):
        """
        Test saving a single history entry and retrieving it.
        """
        manager = HistoryManager()
        history_entry = {
            "city": "Paris",
            "date": "2024-11-23",
            "description": "Light rain",
            "temp": 55,
        }
        manager.save(history_entry)
        history = manager.get_all()

        self.assertEqual(len(history), 1)  # Ensure one entry was saved
        self.assertEqual(history[0], history_entry)  # Ensure saved entry matches
        print("Test passed: Single history entry saved and retrieved successfully.")

    def test_save_multiple_history_entries(self):
        """
        Test saving multiple history entries and retrieving them.
        """
        manager = HistoryManager()
        entries = [
            {"city": "Paris", "date": "2024-11-23", "description": "Light rain", "temp": 55},
            {"city": "London", "date": "2024-11-22", "description": "Cloudy", "temp": 50},
        ]
        for entry in entries:
            manager.save(entry)

        history = manager.get_all()

        self.assertEqual(len(history), 2)  # Ensure two entries were saved
        self.assertEqual(history, entries)  # Ensure saved entries match
        print("Test passed: Multiple history entries saved and retrieved successfully.")

    def test_clear_history(self):
        """
        Test clearing all saved history.
        """
        manager = HistoryManager()
        entries = [
            {"city": "Paris", "date": "2024-11-23", "description": "Light rain", "temp": 55},
            {"city": "London", "date": "2024-11-22", "description": "Cloudy", "temp": 50},
        ]
        for entry in entries:
            manager.save(entry)

        manager.clear()
        history = manager.get_all()

        self.assertEqual(len(history), 0)  # Ensure history is cleared
        print("Test passed: History cleared successfully.")

    def test_save_duplicate_entries(self):
        """
        Test saving duplicate history entries.
        """
        manager = HistoryManager()
        entry = {"city": "Paris", "date": "2024-11-23", "description": "Light rain", "temp": 55}
        manager.save(entry)
        manager.save(entry)  # Save duplicate

        history = manager.get_all()

        self.assertEqual(len(history), 2)  # Ensure duplicate entries are saved
        print("Test passed: Duplicate history entries handled successfully.")


if __name__ == "__main__":
    unittest.main()
