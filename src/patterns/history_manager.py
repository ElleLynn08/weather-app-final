class HistoryManager:
    """
    Manages the storage and retrieval of weather history.
    Implements the Memento Pattern.
    """
    def __init__(self):
        self.history = []

    def save(self, data):
        """
        Save a snapshot of weather data.

        Parameters:
        data (dict): The weather data to save.
        """
        self.history.append(data)

    def get_all(self):
        """
        Retrieve all saved weather data.

        Returns:
        list: A list of saved weather data.
        """
        return self.history

    def clear(self):
        """
        Clears the stored weather history.
        """
        self.history.clear()
