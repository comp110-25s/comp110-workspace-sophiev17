"""My first exercise in COMP110!"""

__author__ = "730579326"


def greet(name: str) -> str:
    """A welcoming first function definition"""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("what is your name?")))
