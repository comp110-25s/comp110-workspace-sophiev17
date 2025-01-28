"""I'm planning a tea party for me and some (333) friends!"""

__author__: str = "730579326"


def main_planner(guests: int) -> None:
    """entire tea party plan"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """number of tea bags we need for everyone"""
    return 2 * people


def treats(people: int) -> int:
    """how many treats we need"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """total cost of tea bags and treats"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
