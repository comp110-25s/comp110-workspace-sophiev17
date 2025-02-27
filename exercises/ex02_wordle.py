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
        """each letter in the given word will be checked for the specific letter only while the index is less than the searched string"""
    return False


def emojified(guess: str, secret: str) -> str:
    """Calling contains_char function to produce emojis give the colored wordle hints"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji_result: str = ""
    while i < len(guess):
        """the while loop will continue for each letter in the guess until the index equals the length."""
        if guess[i] == secret[i]:
            emoji_result = emoji_result + GREEN_BOX
            """if the indexed letter in the guess is the same as the indexed letter in the secret word, then a green box will be added to the string in that spot"""
        elif contains_char(secret, guess[i]):
            emoji_result = emoji_result + YELLOW_BOX
            """if there isn't already a green box assigned, the indexed letter in the guess matches any of the letters in the secret, then a yellow box will be added to the string in that spot"""
        else:
            emoji_result = emoji_result + WHITE_BOX
            """if there isn't already a green or yellow box added to the string for the indexed letter in the guess, then a white box will be added to the string"""
        i = i + 1
        """the loop isn't infinite since the index value increases each time the loop is accessed"""
    return emoji_result


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
        """the while loop checks the length of the guess compared to the secret using the input_guess and if it's the same length, it'll run the emojified function which checks each letter and gives a resulting emoji as long as it has been six turns or less"""
    print("X/6 - Sorry, try again tomorrow!")
    """this only prints if all 6 turns have been used and they never guessed the secret word"""


if __name__ == "__main__":
    main(secret="codes")
