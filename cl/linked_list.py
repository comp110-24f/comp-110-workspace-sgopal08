"""Lesson"""

from __future__ import annotations

__author__: str = "730662974"


class Node:
    """Class node of comp classes"""

    def __init__(self, val: int, next: Node | None):
        """
        Initializes a Node with a value and a pointer to the next node.

        Parameters:
            val (int): The value stored in the node.
            next (Node | None): The next node in the list, or None if this is the last node.
        """
        self.value = val
        self.next = next
