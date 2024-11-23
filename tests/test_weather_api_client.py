"""
Unit tests for the TimeStrategy classes.
"""

import unittest
from datetime import datetime, timedelta, timezone
from src.patterns.time_strategy import SystemTimeStrategy, LocalTimeStrategy


class TestTimeStrategy(unittest.TestCase):
    """
    Unit tests for SystemTimeStrategy and LocalTimeStrategy classes.
    """

    def test_system_time_strategy(self):
        """
        Test if SystemTimeStrategy correctly fetches the current system time.
        """
        strategy = SystemTimeStrategy()
        system_time = strategy.calculate_time()
        # Assert the format of the returned time
        self.assertRegex(system_time, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
        print(f"System time fetched: {system_time}")

    def test_local_time_strategy(self):
        """
        Test if LocalTimeStrategy correctly calculates local time with an offset.
        """
        strategy = LocalTimeStrategy()
        timezone_offset = 3600  # +1 hour offset
        expected_time = (datetime.now(timezone.utc) + timedelta(seconds=timezone_offset)).strftime("%Y-%m-%d %H:%M:%S")
        local_time = strategy.calculate_time(timezone_offset)
        # Assert the local time matches the expected time
        self.assertEqual(local_time, expected_time)
        print(f"Local time calculated: {local_time}")

    def test_system_time_format(self):
        """
        Test if SystemTimeStrategy returns time in the expected format.
        """
        strategy = SystemTimeStrategy()
        system_time = strategy.calculate_time()
        # Check the format of the system time
        self.assertRegex(system_time, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    def test_local_time_format(self):
        """
        Test if LocalTimeStrategy returns time in the expected format.
        """
        strategy = LocalTimeStrategy()
        timezone_offset = -18000  # -5 hours offset (e.g., EST)
        local_time = strategy.calculate_time(timezone_offset)
        # Check the format of the local time
        self.assertRegex(local_time, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    def test_local_time_negative_offset(self):
        """
        Test LocalTimeStrategy with a negative timezone offset (e.g., going back in time).
        """
        strategy = LocalTimeStrategy()
        timezone_offset = -7200  # -2 hours offset
        expected_time = (datetime.now(timezone.utc) + timedelta(seconds=timezone_offset)).strftime("%Y-%m-%d %H:%M:%S")
        local_time = strategy.calculate_time(timezone_offset)
        self.assertEqual(local_time, expected_time)

    def test_local_time_positive_offset(self):
        """
        Test LocalTimeStrategy with a positive timezone offset (e.g., going forward in time).
        """
        strategy = LocalTimeStrategy()
        timezone_offset = 10800  # +3 hours offset
        expected_time = (datetime.now(timezone.utc) + timedelta(seconds=timezone_offset)).strftime("%Y-%m-%d %H:%M:%S")
        local_time = strategy.calculate_time(timezone_offset)
        self.assertEqual(local_time, expected_time)


if __name__ == "__main__":
    unittest.main()
