__author__ = "730662974"


def main() -> None:
    print(concat(word1, word2))


word1: str = "happy"
word2: str = "tuesday"


def concat(string1: str, string2: str) -> str:
    return string1 + string2


if __name__ == "__main__":
    main()
