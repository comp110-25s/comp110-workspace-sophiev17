"""File to define River class."""

__author__ = "730579326"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


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
        new_fish: list = []
        new_bears: list = []
        for fishy in self.fish:
            if fishy.age <= 3:
                new_fish.append(fishy)
        for bears in self.bears:
            if bears.age <= 5:
                new_bears.append(bears)

        self.fish = new_fish
        self.bears = new_bears
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        hungry_bears: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                hungry_bears.append(bear)
        self.bears = hungry_bears
        return None

    def repopulate_fish(self):
        fish_eggs = (len(self.fish) // 2) * 4
        idx: int = 0
        while idx < fish_eggs:
            self.fish.append(Fish())
            idx += 1
        return None

    def repopulate_bears(self):
        baby_bears = len(self.bears) // 2
        idx: int = 0
        while idx < baby_bears:
            self.bears.append(Bear())
            idx += 1
        return None

    def view_river(self) -> None:
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

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

    def one_river_week(self):
        """Simulate one week in the river"""
        count_week: int = 0
        while count_week <= 7:
            self.one_river_day()
            count_week += 1

    def remove_fish(self, amount: int) -> None:
        popping: int = 0
        while popping < amount:
            self.fish.pop(popping)
            popping += 1
