class NumberCollection:
    def __init__(self, size: int):
        """
        Initialize the collection with a fixed size.
        """
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        self.size = size
        self.numbers = []

    def insert_number(self, number: int) -> None:
        """
        Insert a number into the collection.
        """
        if len(self.numbers) >= self.size:
            raise IndexError("Cannot insert more numbers than the defined size.")
        self.numbers.append(number)

    def search_number(self, target: int) -> int:
        """
        Search for target in the collection.
        Returns 1-based index if found, otherwise -1.
        """
        for index, number in enumerate(self.numbers):
            if number == target:
                return index + 1
        return -1
