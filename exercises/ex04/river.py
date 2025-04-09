"""File to define River class."""

__author__ = "730579326"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear

"""importing Fish class"""
"""importing Bear class"""


class River:
    day: int

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking ages to make sure they're not too old."""
        new_fish: list = []
        new_bears: list = []
        for fishy in self.fish:
            if fishy.age <= 3:
                new_fish.append(fishy)
                """if fish are three or younger, add them to the list"""
        for bears in self.bears:
            if bears.age <= 5:
                new_bears.append(bears)
                """if bears are 5 or younger, add them to the lsit"""

        self.fish = new_fish
        """the self.fish list now only contains fish that are 3 or younger"""
        self.bears = new_bears
        """the self.bears list now only contains bears that are 5 or younger"""
        return None

    def bears_eating(self):
        """The bears gotta eat"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Bears are going to get hungry"""
        hungry_bears: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                hungry_bears.append(bear)
        self.bears = hungry_bears
        return None

    def repopulate_fish(self):
        """Freaky fish time"""
        fish_eggs = (len(self.fish) // 2) * 4
        idx: int = 0
        while idx < fish_eggs:
            self.fish.append(Fish())
            idx += 1
        return None

    def repopulate_bears(self):
        """Busy bumbling bears"""
        baby_bears = len(self.bears) // 2
        """number of bears divided by two makes one baby bear per two bears"""
        idx: int = 0
        while idx < baby_bears:
            self.bears.append(Bear())
            """Adds one new bear to the Bear class for each run of the while loop"""
            idx += 1
        return None

    def view_river(self) -> None:
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_week(self):
        """Simulate one week in the river"""
        count_week: int = 0
        while count_week < 7:
            self.one_river_day()
            count_week += 1

    def remove_fish(self, amount: int) -> None:
        """removes fish off the fish list only while there are still fish to remove"""
        popping: int = 0
        while popping < amount:
            self.fish.pop(popping)
            popping += 1

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
