"""4 functions using lists in ex04."""

__author__: str = "730662974"


def all(a: list[int], b: int) -> bool:
    """Return True or False based on if int is equal to every item in list."""
    if len(a) == 0:
        return False
    index: int = 0
    while index < len(a):
        if a[index] != b:
            return False
        index = index + 1
    return True
    # return statement has to be in the first indent, can't be nested in something


def max(input: list[int]) -> int:
    """Tests each item in list and finds its max."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    index: int = 0
    max_number: int = input[index]
    # create max number to make sure the whole index is looped through
    while index < len(input):
        if input[index] > max_number:
            max_number = input[index]
        index = index + 1
    return max_number
    # if statement returns True, then loops until while is False,
    # so until it can't loop,
    # the value returned will be max


def is_equal(a: list[int], b: list[int]) -> bool:
    """Tests to see if one list is fully (deep) equal to another."""
    index: int = 0
    if len(a) == 0 and len(b) == 0:
        return True
    if len(a) == len(b):
        # only under condition if the len of both lists are equal or else won't run
        while index < len(a):
            if a[index] == b[index]:
                return True
            index = index + 1
    return False


def extend(a: list[int], b: list[int]) -> None:
    """Add each item of list b to list a."""
    index: int = 0
    while index < len(b):
        a.append(b[index])
        # can't append a whole list, has to loop through index to add each item
        index = index + 1
