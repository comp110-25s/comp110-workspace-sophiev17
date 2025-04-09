"""File to define Fish class."""

__author__ = "730579326"


class Fish:
    age: int

    def __init__(self):
        """Age of each fish starts at 0."""
        self.age = 0
        return None

    def one_day(self):
        """Fish age with each day."""
        self.age += 1
        return None
