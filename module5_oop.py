class NumberCollection:
    def __init__(self, size):
        """Initialize the collection with expected size."""
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        self.size = size
        self.numbers = []

    def insert_number(self, number):
        """Insert a number into the collection."""
        if len(self.numbers) < self.size:
            self.numbers.append(number)
        else:
            raise IndexError("Cannot insert more numbers than specified size.")

    def search_number(self, target):
        """Search for target number and return 1-based index or -1."""
        for index, number in enumerate(self.numbers):
            if number == target:
                return index + 1  # Convert to 1-based index
        return -1


def main():
