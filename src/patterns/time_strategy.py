"""
This module defines time calculation strategies for various time contexts.
"""

from datetime import datetime, timezone, timedelta


class TimeStrategy:
    """
    Abstract base class for time calculation strategies.
    """

    def calculate_time(self, data):
        """
        Abstract method to calculate time.

        Parameters:
        data (any): The data needed for time calculation.

        Returns:
        str: The calculated time as a formatted string.
        """
        raise NotImplementedError("Subclasses must implement this method")


class SystemTimeStrategy(TimeStrategy):
    """
    Strategy to fetch the current system time.
    """

    def calculate_time(self, data=None):
        """
        Calculates the current system time.

        Parameters:
        data (None): No additional data is required for system time.

        Returns:
        str: The current system time in "YYYY-MM-DD HH:MM:SS" format.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class LocalTimeStrategy(TimeStrategy):
    """
    Strategy to calculate local time based on a timezone offset.
    """

    def calculate_time(self, timezone_offset):
        """
        Calculates local time using the provided timezone offset.

        Parameters:
        timezone_offset (int): The timezone offset in seconds.

        Returns:
        str: The local time in "YYYY-MM-DD HH:MM:SS" format.
        """
        utc_now = datetime.now(timezone.utc)  # Get current UTC time
        local_time = utc_now + timedelta(seconds=timezone_offset)  # Apply offset
        return local_time.strftime("%Y-%m-%d %H:%M:%S")

