"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730662974"


def input_word() -> str:
    # Part 1
    """User inputs a word and function checks to see if it's valid."""
    word: str = input("Enter a 5-character word: ")

    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """User inputs a letter"""
    # Part 3
    letter: str = input("Enter a single character:")

    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character")
        exit()


def contains_char(word: str, letter: str) -> None:
    # Part 3 & 4
    """Checks to see if given letter is in the input word."""
    count: int = 0

    print("Searching for " + letter + " in " + word)

    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1

    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1

    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1

    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1

    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    if count == 0:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    """Main function."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
