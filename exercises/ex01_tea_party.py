"""EX01: Tea Party"""

__author__: str = "730662974"


def main_planner(guests: int) -> None:
    """Entrypoint of program."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    tea_total = tea_bags(guests)
    treats_total = treats(guests)
    print("Cost: $" + str(cost(tea_total, treats_total)))


def tea_bags(people: int) -> int:
    """Computes the number of tea bags needed based on number of guests."""
    return people * 2


def treats(people: int) -> int:
    """Computes the number of treats needed based on the number of teas guests drink."""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes cost of tea bags and treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
