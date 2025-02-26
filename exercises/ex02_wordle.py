"""Making my own game of wordle"""

__author__ = "730579326"


def contains_char(searched_string: str, check_letter: str) -> bool:
    """looking for a single character from a string"""
    assert len(check_letter) == 1, f"len('{check_letter}') is not 1"
    i: int = 0
    while i < len(searched_string):
        if searched_string[i] == check_letter:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Calling contains_char function to produce emojis give the colored wordle hints"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    result: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            result = result + GREEN_BOX
        if contains_char(secret, guess[i]):
            result = result + YELLOW_BOX
        if contains_char(secret, guess[i]):
            result = result + WHITE_BOX
        i = i + 1
    return result


def input_guess(expected_length: int) -> str:
    """Guessing the length of the word first"""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        result: str = emojified(guess, secret)
        print(result)
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn = turn + 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
