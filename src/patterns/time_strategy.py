from datetime import datetime, timezone, timedelta

class TimeStrategy:
    """
    Interface for different time strategies.
    """
    def calculate_time(self, data):
        raise NotImplementedError("Subclasses must implement this method")


class SystemTimeStrategy(TimeStrategy):
    """
    Strategy to get the current system time.
    """
    def calculate_time(self, data=None):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class LocalTimeStrategy(TimeStrategy):
    """
    Strategy to calculate local time based on timezone offset.
    """
    def calculate_time(self, timezone_offset):
        utc_now = datetime.now(timezone.utc)  # Current UTC time
        local_time = utc_now + timedelta(seconds=timezone_offset)
        return local_time.strftime("%Y-%m-%d %H:%M:%S")
