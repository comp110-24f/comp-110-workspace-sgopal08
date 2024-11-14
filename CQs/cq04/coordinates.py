__author__ = "730662974"

"""each variable gets written with each other"""

__author__ = "730550999"


def get_coords(xs: str, ys: str) -> None:
    x_index: int = 0
    y_index: int = 0
    while x_index < len(xs):
        x_value = xs[x_index]
        y_index = 0
        while y_index < len(ys):
            y_value = ys[y_index]
            print("(" + x_value + ", " + y_value + ")")
            y_index += 1
        x_index += 1
    return None
