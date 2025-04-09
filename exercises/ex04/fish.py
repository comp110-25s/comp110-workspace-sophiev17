"""File to define Fish class."""

__author__ = "730579326"


class Fish:
    age: int

    def __init__(self):
        """age of each fish starts at 0"""
        self.age = 0
        return None

    def one_day(self):
        """fish age with each day"""
        self.age += 1
        return None
