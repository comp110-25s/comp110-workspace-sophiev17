"""File to define Bear class."""

__author__ = "730579326"


class Bear:
    """We have bears!"""

    age: int
    hunger_score: int

    def __init__(self):
        """Age and hunger score of all bears start at 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Age inc and hunger score dec each day (lower score == more hungry)."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Hunger score inc with more fish (bears are less hungry with more food)."""
        self.hunger_score += num_fish
        return None
