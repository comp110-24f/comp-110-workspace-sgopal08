"""EX03 - Wordle the game"""

__author__ = "730662974"


def input_guess(secret_len: int) -> str:
    """
    Prompts user for a guess,
    loops until a valid length guess is recieved
    """
    guess = input(f"Enter a {secret_len} character word: ")

    while len(guess) != secret_len:
        guess = input(f"That wasn't {secret_len} chars! Try again: ")

    return guess


def contains_char(secret_word: str, guess_char: str) -> bool:
    """
    Checks if a character is in a string
    returns a bool that specifies if the character is there or not
    """
    assert len(guess_char) == 1

    # loops through secret_word to see if guess_char is in it
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == guess_char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """
    Returns a group of emojis based on
    how similar the guess is to the secret word
    """
    assert len(guess) == len(secret)

    # The string that is being added too when a character is assigned an emoji
    return_emojis: str = ""

    # defines different emojis as variables for readability
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i: int = 0

    # loops through characters in guess to assign it an emoji
    while i < len(secret):
        if guess[i] == secret[i]:
            return_emojis += GREEN_BOX
        elif contains_char(secret_word=secret, guess_char=guess[i]):
            return_emojis += YELLOW_BOX
        else:
            return_emojis += WHITE_BOX
        i += 1

    return return_emojis


def main(secret: str) -> None:
    """
    The entrypoint of the program and main game loop
    """
    turn_num: int = 1

    # uses while loop to go through the game loop 6 times
    while turn_num <= 6:
        print(f"=== Turn {turn_num}/6 ===")
        guess = input_guess(secret_len=len(secret))
        print(emojified(guess=guess, secret=secret))
        if guess == secret:
            print(f"You won in {turn_num}/6 turns!")
            break
        turn_num += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
